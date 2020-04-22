def get_pareto_result(schedules):
    pareto_list = list()

    if schedules is not None:
        for s1 in schedules:
            defeat = False

            for s2 in schedules:
                if s1.id != s2.id:
                    if (s2.makespan <= s1.makespan and s2.total_cost < s1.total_cost and s2.rel_inverse < s1.rel_inverse and s2.degree_of_imbalance < s1.degree_of_imbalance and s2.energy < s1.energy) or (s2.total_cost <= s1.total_cost and s2.makespan < s1.makespan and s2.rel_inverse < s1.rel_inverse and s2.degree_of_imbalance < s1.degree_of_imbalance and s2.energy < s1.energy) or (s2.rel_inverse <= s1.rel_inverse and s2.total_cost < s1.total_cost and s2.makespan < s1.makespan and s2.degree_of_imbalance < s1.degree_of_imbalance and s2.energy < s1.energy) or (s2.energy <= s1.energy and s2.total_cost < s1.total_cost and s2.makespan < s1.makespan and s2.degree_of_imbalance < s1.degree_of_imbalance and s2.rel_inverse < s1.rel_inverse) or (s2.degree_of_imbalance <= s1.degree_of_imbalance and s2.total_cost < s1.total_cost and s2.makespan < s1.makespan and s2.rel_inverse < s1.rel_inverse and s2.energy < s1.energy):
                        defeat = True
                        break

            if defeat is False:
                pareto_list.append(s1)

    return pareto_list
