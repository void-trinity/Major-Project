import copy
import statistics
import math
from config.config import n, b

class Workflow:
    id = 0
    workflow = list()
    processing_time = dict()
    makespan = 0
    total_cost = 0
    cost = dict()
    degree_of_imbalance = 0.0
    task_to_resource_dict = dict()
    billing_time = dict()
    rel_inverse = 1.0

    def __init__(self):
        self.id = 0
        self.workflow = list()
        self.makespan = 0
        self.total_cost = 0
        self.processing_time = dict()
        self.cost = dict()
        self.degree_of_imbalance = 0
        self.task_to_resource_dict = dict()
        self.billing_time = dict()
        self.rel_inverse = 1.0

    def add_to_workflow(self, task, resource):
        self.workflow.append((task, resource))
        self.task_to_resource_dict[task] = resource
        self.billing_time[resource] = 0

    def calculate_makespan(self, tasks_dict, resources_dict, dag_dict):
        processing_time = dict()
        start_time = dict()
        finish_time = dict()

        for (task, resource) in self.workflow:
            processing_time[task] = float(tasks_dict[task].runtime / resources_dict[resource].cu)
            if len(tasks_dict[task].predecessor_tasks) > 0:
                start_time[task] = max([finish_time[x] for x in tasks_dict[task].predecessor_tasks])
            else:
                start_time[task] = 0

            transfer_bytes = 0
            for t in dag_dict[task]:
                if t in self.task_to_resource_dict and self.task_to_resource_dict[t] != resource:
                    transfer_bytes = transfer_bytes + dag_dict[task][t]

            finish_time[task] = start_time[task] + processing_time[task] + transfer_bytes/(1024.0*1024*1024)
            self.billing_time[resource] = self.billing_time[resource] + finish_time[task]

        self.makespan = max(finish_time.values())
        self.processing_time = copy.deepcopy(processing_time)


    def calculate_cost(self, tasks_dict, resources_dict, dag_dict):
        total_cost = 0.0
        
        for resource in self.billing_time:
            total_cost = total_cost + self.billing_time[resource] * resources_dict[resource].price

        transfer_bytes = 0.0
        for (task, resource) in self.workflow:
            for t in dag_dict[task]:
                if t in self.task_to_resource_dict and self.task_to_resource_dict[t] != resource:
                    transfer_bytes = transfer_bytes + dag_dict[task][t]
            
        total_cost = total_cost + transfer_bytes / (1024*1024*1024.0) * 0.01

        self.total_cost = total_cost
        



    def calculate_degree_of_imbalance(self, resources_dict):
        degree_of_imbalance = dict()

        for resource in resources_dict:
            degree_of_imbalance[resource] = 0

        for (task, resource) in self.workflow:
            degree_of_imbalance[resource] = degree_of_imbalance[resource] + self.processing_time[task]

        dib_min = min(list(degree_of_imbalance.values()))
        dib_max = max(list(degree_of_imbalance.values()))
        dib_avg = statistics.mean(degree_of_imbalance.values())

        self.degree_of_imbalance = (dib_max-dib_min)/dib_avg


    def calculate_reliability(self):
        reliability = 1.0
        for task in self.processing_time:
            reliability = reliability * math.exp(pow((-self.processing_time[task]/n), b))

        self.rel_inverse = 1 / reliability


    def schedule(self, id, tasks_dict, resources_dict, dag_dict):
        self.id = id
        self.calculate_makespan(tasks_dict, resources_dict, dag_dict)
        self.calculate_cost(tasks_dict, resources_dict, dag_dict)
        self.calculate_degree_of_imbalance(resources_dict)
        self.calculate_reliability()

    def get_sorted_workflow(self):
        t = copy.deepcopy(self.workflow)
        t.sort(key = lambda x: x[0])
        return [x[1] for x in t]

    def print(self, resources_dict):
        print("ID: {}\nMakespan: {}\nCost: {}\nReliability: {}\nDegree of Imbalance: {}".format(self.id, self.makespan, self.total_cost, self.reliability, self.degree_of_imbalance))
