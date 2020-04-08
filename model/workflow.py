import copy

class Workflow:
    id = 0
    workflow = list()
    makespan = 0
    total_cost = 0
    exe_time = dict()
    comp_time = dict()
    cost = dict()

    def __init__(self):
        self.id = 0
        self.workflow = list()
        self.makespan = 0
        self.total_cost = 0
        self.exe_time = dict()
        self.comp_time = dict()
        self.cost = dict()

    def add_to_workflow(self, task, resource):
        self.workflow.append((task, resource))

    def task_to_resource_dict(self):
        task_to_resource_dict = dict()

        for (task, resource) in self.workflow:
            task_to_resource_dict[task] = resource

        return task_to_resource_dict

    def calculate_makespan(self, tasks_dict, resources_dict, dag_dict):
        exe_time = dict()
        task_to_resource_dict = self.task_to_resource_dict()
        comp_time = dict()

        for (task, resource) in self.workflow:
            exe_time[task] = float(tasks_dict[task].runtime/resources_dict[resource].cu)
            transfer_time = 0
            for predecessor in tasks_dict[task].predecessor_tasks:
                if task_to_resource_dict[predecessor] != resource:
                    transfer_time = max(transfer_time, dag_dict[predecessor][task])
            exe_time[task] = exe_time[task] + transfer_time/(1024*1024*1024.0)

        self.exe_time = copy.deepcopy(exe_time)


        for (task, resource) in self.workflow:
            if len(tasks_dict[task].predecessor_tasks) == 0:
                comp_time[task] = exe_time[task]
            else:
                max_time = 0
                for predecessor in tasks_dict[task].predecessor_tasks:
                    max_time = max(max_time, comp_time[predecessor] + exe_time[task])

                comp_time[task] = max_time
        self.makespan = max(comp_time.values())
        self.comp_time = copy.deepcopy(comp_time)

    def calculate_cost(self, tasks_dict, resources_dict, dag_dict):
        cost = dict()
        task_to_resource_dict = self.task_to_resource_dict()

        for (task, resource) in self.workflow:
            c1 = self.exe_time[task] * resources_dict[resource].price
            c2 = 0
            c3 = (sum([x.size for x in tasks_dict[task].input_files])/(1024*1024*1024.0) + sum([x.size for x in tasks_dict[task].output_files])/(1024*1024*1024.0)) * resources_dict[resource].price
            cost[task] = c1 + c2 + c3

        self.cost = copy.deepcopy(cost)
        self.total_cost = sum(cost.values())

    def schedule(self, id, tasks_dict, resources_dict, dag_dict):
        self.id = id
        self.calculate_makespan(tasks_dict, resources_dict, dag_dict)
        self.calculate_cost(tasks_dict, resources_dict, dag_dict)

    def print(self, resources_dict):
        print("ID: {}, Makespan: {}, Cost: {}".format(self.id, self.makespan, self.total_cost))
        for (task, resource) in self.workflow:
            print(task, resources_dict[resource].type)

    def get_sorted_workflow(self):
        t = copy.deepcopy(self.workflow)
        t.sort(key = lambda x: x[0])
        return [x[1] for x in t]
