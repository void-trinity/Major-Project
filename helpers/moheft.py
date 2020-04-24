from helpers.calculate_b_rank import calculate_b_rank
from model.workflow import Workflow
from helpers.crowding_distance_sort import crowding_distance_sort
import copy
from helpers.get_pareto_result import get_pareto_result

def moheft(tasks_dict, resources_dict, dag_dict, K, objectives):
    b_rank = calculate_b_rank(tasks_dict)

    schedules = list()

    for i in range(K):
        schedules.append(Workflow())

    for i in range(len(b_rank)):
        print("----Running iteration {}----".format(i+1))
        temp_list = list()

        if len(schedules) > 0:
            for s in schedules:
                for resource in resources_dict:
                    temp = copy.deepcopy(s)
                    temp.add_to_workflow(task = b_rank[i], resource = resource)
                    temp_list.append(temp)

        else:
            for resource in resources_dict:
                temp = copy.deepcopy(s)
                temp.add_to_workflow(task = b_rank[i], resource = resource)
                temp_list.append(temp)

        counter = 0
        for s in temp_list:
            s.schedule(counter, tasks_dict, resources_dict, dag_dict)
            counter = counter + 1
        schedules = crowding_distance_sort(temp_list, K, objectives)

    return get_pareto_result(schedules, objectives)
