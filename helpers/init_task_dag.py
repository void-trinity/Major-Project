def get_weight(successor_input_files, task_output_files):
    weight = 0
    for input_file in successor_input_files:
        for output_file in task_output_files:
            if input_file.name == output_file.name:
                weight = weight + max(input_file.size, output_file.size)

    return weight

def init_task_dag(tasks_dict):
    dag_dict = dict()

    for task in tasks_dict:
        temp = dict()
        for successor in tasks_dict[task].successor_tasks:
            temp[successor] = get_weight(tasks_dict[successor].input_files, tasks_dict[task].output_files)
        dag_dict[task] = temp

    return dag_dict
