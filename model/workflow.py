import copy
import statistics
import math
from config.config import n, b
import numpy as np

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
            max_time = 0
            for predecessor in tasks_dict[task].predecessor_tasks:
                if self.task_to_resource_dict[predecessor] != resource:
                    max_time = max(max_time, dag_dict[predecessor][task]/(1024.0*1024*1024))
            processing_time[task] += max_time

        for (task, resource) in self.workflow:
            if len(tasks_dict[task].predecessor_tasks) == 0:
                finish_time[task] = processing_time[task]
            else:
                finish_time[task] = processing_time[task] + max([finish_time[x] for x in tasks_dict[task].predecessor_tasks])
            self.billing_time[resource] += finish_time[task]

        self.makespan = max(finish_time.values())
        self.processing_time = copy.deepcopy(processing_time)


    def calculate_cost(self, tasks_dict, resources_dict, dag_dict):
        cost = dict()

        for (task, resource) in self.workflow:
            c1 = self.processing_time[task] * resources_dict[resource].price
            c2 = (sum([x.size for x in tasks_dict[task].input_files])/(1024*1024*1024.0) + sum([x.size for x in tasks_dict[task].output_files])/(1024*1024*1024.0)) * resources_dict[resource].price
            cost[task] = c1 + c2

        self.cost = copy.deepcopy(cost)
        self.total_cost = sum(cost.values())
        



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
        reliability = dict()
        for task in self.processing_time:
            reliability[task] = 1 - float(np.exp(-np.power(self.processing_time[task]/n, b)))

        rel = 1.0
        for task in reliability:
            rel = rel * reliability[task]

        self.rel_inverse = rel


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
        print("ID: {}\nMakespan: {}\nCost: {}\nReliability: {}\nDegree of Imbalance: {}".format(self.id, self.makespan, self.total_cost, self.rel_inverse, self.degree_of_imbalance))
