from helpers.hv import HyperVolume

def calculate_hv(workflows):
    reference_point = [1.1, 1.1, 1.1, 1.1, 1.1]
    
    hv = HyperVolume(reference_point)
    max_makespan = 0
    max_cost = 0
    max_dib = 0
    max_rel_inv = 0
    max_energy = 0
    fronts = list()

    for workflow in workflows:
        fronts.append(list())
        max_makespan = max(max_makespan, max([x.makespan for x in workflow]))
        max_cost = max(max_cost, max([x.total_cost for x in workflow]))
        max_dib = max(max_dib, max([x.degree_of_imbalance for x in workflow]))
        max_rel_inv = max(max_rel_inv, max([x.rel_inverse for x in workflow]))
        max_energy = max(max_energy, max([x.energy for x in workflow]))
    
    
    

    for i in range(len(workflows)):
        for s in workflows[i]:
            fronts[i].append([s.makespan/max_makespan, s.total_cost/max_cost, s.degree_of_imbalance/max_dib, s.rel_inverse/1, s.energy/max_energy])

    volumes = list()

    for front in fronts:
        volumes.append(hv.compute(front))

    return volumes