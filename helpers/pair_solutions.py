import math

def get_dist(s1, s2):
    dist = float(math.sqrt(math.pow((s1.makespan-s2.makespan),2) + math.pow((s1.total_cost-s2.total_cost),2) + math.pow((s1.rel_inverse-s2.rel_inverse),2)))
    return dist

def pair_solutions(S1, S2):
    pairs = list()

    if len(S1) <= len(S2):
        for s1 in S1:
            min_dist = -1
            id = 0
            for s2 in S2:
                dist = get_dist(s1, s2)
                if min_dist == -1 or dist < min_dist:
                    min_dist = dist
                    id = s2

            pairs.append((s1, id))
    else:
        for s2 in S2:
            min_dist = -1
            id = 0
            for s1 in S1:
                dist = get_dist(s1, s2)
                if min_dist == -1 or dist < min_dist:
                    min_dist = dist
                    id = s1

            pairs.append((id, s2))

    return pairs
