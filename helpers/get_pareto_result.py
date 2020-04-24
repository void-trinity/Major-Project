def check_non_dominated(s1, s2, objectives):
    if objectives == 3:
        return ((s2.makespan <= s1.makespan and s2. total_cost < s1.total_cost and s2.degree_of_imbalance < s1.degree_of_imbalance) or (s2.makespan < s1.makespan and s2. total_cost <= s1.total_cost and s2.degree_of_imbalance < s1.degree_of_imbalance) or (s2.makespan < s1.makespan and s2. total_cost < s1.total_cost and s2.degree_of_imbalance <= s1.degree_of_imbalance))

    elif objectives == 4:
        return ((s2.makespan <= s1.makespan and s2. total_cost < s1.total_cost and s2.degree_of_imbalance < s1.degree_of_imbalance and s2.rel_inverse < s1.rel_inverse) or (s2.makespan < s1.makespan and s2. total_cost <= s1.total_cost and s2.degree_of_imbalance < s1.degree_of_imbalance and s2.rel_inverse < s1.rel_inverse) or (s2.makespan < s1.makespan and s2. total_cost < s1.total_cost and s2.degree_of_imbalance <= s1.degree_of_imbalance and s2.rel_inverse < s1.rel_inverse) or (s2.makespan < s1.makespan and s2. total_cost < s1.total_cost and s2.degree_of_imbalance < s1.degree_of_imbalance and s2.rel_inverse <= s1.rel_inverse))
    
    elif objectives == 5:
        return ((s2.makespan <= s1.makespan and s2. total_cost < s1.total_cost and s2.degree_of_imbalance < s1.degree_of_imbalance and s2.rel_inverse < s1.rel_inverse and s2.energy < s1.energy) or (s2.makespan < s1.makespan and s2. total_cost <= s1.total_cost and s2.degree_of_imbalance < s1.degree_of_imbalance and s2.rel_inverse < s1.rel_inverse and s2.energy < s1.energy) or (s2.makespan < s1.makespan and s2. total_cost < s1.total_cost and s2.degree_of_imbalance <= s1.degree_of_imbalance and s2.rel_inverse < s1.rel_inverse and s2.energy < s1.energy) or (s2.makespan < s1.makespan and s2. total_cost < s1.total_cost and s2.degree_of_imbalance < s1.degree_of_imbalance and s2.rel_inverse <= s1.rel_inverse and s2.energy < s1.energy) or (s2.makespan < s1.makespan and s2. total_cost < s1.total_cost and s2.degree_of_imbalance < s1.degree_of_imbalance and s2.rel_inverse < s1.rel_inverse and s2.energy <= s1.energy))

    

def get_pareto_result(schedules, objectives):
    pareto_list = list()

    if schedules is not None:
        for s1 in schedules:
            defeat = False

            for s2 in schedules:
                if s1.id != s2.id:
                    if(check_non_dominated(s1, s2, objectives)):  
                        defeat = True
                        break

            if defeat is False:
                pareto_list.append(s1)

    return pareto_list
