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
    elif objective == 'reliability':
        schedule_list.sort(key = lambda x: x.rel_inverse)
        values = [x.rel_inverse for x in schedule_list]
    elif objective == 'energy':
        schedule_list.sort(key = lambda x: x.energy)
        values = [x.energy for x in schedule_list]

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

def crowding_distance_sort(schedule_list, K, objectives):
    makespan_distance_dict, first_item_makespan, last_item_makespan = sort_by_objective(schedule_list, 'makespan')
    cost_distance_dict, first_item_cost, last_item_cost = sort_by_objective(schedule_list, 'cost')
    degree_of_imbalance_distance_dict, first_item_degree_of_imbalance, last_item_degree_of_imbalance = sort_by_objective(schedule_list, 'degree_of_imbalance')
    reliability_distance_dict, first_item_rel, last_item_rel = sort_by_objective(schedule_list, 'reliability')
    energy_distance_dict, first_item_energy, last_item_energy = sort_by_objective(schedule_list, 'energy')

    objectives_id_list = list()
    boundary_items_list = list()
    crowding_distance = list()

    objectives_id_list.append(list(makespan_distance_dict.keys()))
    objectives_id_list.append(list(cost_distance_dict.keys()))
    objectives_id_list.append(list(degree_of_imbalance_distance_dict.keys()))
    boundary_items_list.append(first_item_makespan)
    boundary_items_list.append(last_item_makespan)
    boundary_items_list.append(first_item_cost)
    boundary_items_list.append(last_item_cost)
    boundary_items_list.append(first_item_degree_of_imbalance)
    boundary_items_list.append(last_item_degree_of_imbalance)

    if objectives > 3:
        objectives_id_list.append(list(reliability_distance_dict.keys()))
        boundary_items_list.append(first_item_rel)
        boundary_items_list.append(last_item_rel)
        if objectives > 4:
            objectives_id_list.append(list(energy_distance_dict.keys()))
            boundary_items_list.append(first_item_energy)
            boundary_items_list.append(last_item_energy)



    for id in objectives_id_list[0]:
        present = True
        for i in range(1, len(objectives_id_list)):
            if id not in objectives_id_list[i]:
                present = False
                break
        if present == True:
            distance = makespan_distance_dict[id] + cost_distance_dict[id]  + degree_of_imbalance_distance_dict[id]
            if objectives > 3:
                distance += reliability_distance_dict[id]
                if objectives > 4:
                    distance += energy_distance_dict[id]
            crowding_distance.append((id, distance))


    sorted_crowding_distance = sorted(crowding_distance, key=lambda d: d[1], reverse=True)

    prior_list = []
    result = list()

    # for item in [first_item_makespan, last_item_makespan, first_item_cost, last_item_cost, first_item_rel, last_item_rel, first_item_degree_of_imbalance, last_item_degree_of_imbalance, first_item_energy, last_item_energy]:
    #     if item.id not in [x.id for x in prior_list]:
    #         prior_list.append(item)

    for item in boundary_items_list:
        if item.id not in [x.id for x in prior_list]:
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
