import math

def sort_by_objective(schedule_list, objective):
    distance_dict = dict()
    values = list()

    if objective == 'makespan':
        schedule_list.sort(key = lambda x: x.makespan)
        values = [x.makespan for x in schedule_list]
    elif objective == 'cost':
        schedule_list.sort(key = lambda x: x.total_cost)
        values = [x.total_cost for x in schedule_list]
    elif objective == 'degree_of_imbalance':
        schedule_list.sort(key = lambda x: x.degree_of_imbalance)
        values = [x.degree_of_imbalance for x in schedule_list]

    first_item = schedule_list[0]
    last_item = schedule_list[-1]

    first_value = values[0]
    last_value = values[-1]

    i = 1
    distance_dict = dict()

    while i < len(schedule_list)-1:
        if last_value-first_value != 0:
            dist = math.fabs((values[i+1] - values[i-1]) / (last_value - first_value))
        else:
            dist = 0

        distance_dict[schedule_list[i].id] =  dist
        i = i + 1

    return distance_dict, first_item, last_item

def crowding_distance_sort(schedule_list, K):
    makespan_distance_dict, first_item_makespan, last_item_makespan = sort_by_objective(schedule_list, 'makespan')
    cost_distance_dict, first_item_cost, last_item_cost = sort_by_objective(schedule_list, 'cost')
    degree_of_imbalance_distance_dict, first_item_degree_of_imbalance, last_item_degree_of_imbalance = sort_by_objective(schedule_list, 'degree_of_imbalance')

    crowding_distance = list()

    makespan_dis_id_list = list(makespan_distance_dict.keys())
    cost_dis_id_list = list(cost_distance_dict.keys())
    degree_of_imbalance_id_list = list(degree_of_imbalance_distance_dict.keys())

    for id in makespan_dis_id_list:
        if id in cost_dis_id_list and id in degree_of_imbalance_id_list:
            distance = makespan_distance_dict[id] + cost_distance_dict[id] + degree_of_imbalance_distance_dict[id]
            crowding_distance.append((id, distance))

    sorted_crowding_distance = sorted(crowding_distance, key=lambda d: d[1], reverse=True)

    prior_list = []
    result = list()

    for item in [first_item_makespan, last_item_makespan, first_item_cost, last_item_cost, first_item_degree_of_imbalance, last_item_degree_of_imbalance]:
        exit = False

        for i in prior_list:
            if first_item_makespan.id == i.id:
                exit = True
                break

        if exit is False:
            prior_list.append(item)

    if K >= len(prior_list):
        result.extend(prior_list)
        left_num = K - len(prior_list)
        j = 0
        while j < left_num and j < len(sorted_crowding_distance):
            individual_id = sorted_crowding_distance[j][0]

            for s in schedule_list:
                if s.id == individual_id:
                    result.append(s)
                    break
            j = j + 1
    else:
        result = prior_list[:K]
    return result
