b_rank = dict()

def get_b_rank(tasks_dict, task):
    rank = 0
    if len(tasks_dict[task].successor_tasks) > 0:
        rank = 1
    for successor in tasks_dict[task].successor_tasks:
        rank = max(rank, get_b_rank(tasks_dict, successor)+1)
    b_rank[task] = rank
    return rank

def calculate_b_rank(tasks_dict):
    for task in tasks_dict:
        b_rank[task] = -1

    for task in tasks_dict:
        if b_rank[task] == -1:
            get_b_rank(tasks_dict, task)

    rank_list = list()

    for (x, y) in sorted(b_rank.items(), key = lambda kv:(kv[1], kv[0])):
        rank_list.append(x)

    return rank_list[::-1]
