from config.config import K
from helpers.init_resources import init_resources
from helpers.init_tasks import init_tasks
from helpers.init_task_dag import init_task_dag
from helpers.moheft import moheft
from helpers.pair_solutions import pair_solutions
from helpers.plot import plot
from helpers.validate_solution import validate_solution

total_resources = 60


filename = 'Inspiral_100.xml'


print("----Generating Resources Dict1----")
resources_dict = init_resources(total_resources)

print("----Generating Tasks Dict----")
tasks_dict = init_tasks(filename = filename)

print("----Generating Dag Dict----")
dag_dict = init_task_dag(tasks_dict)

print("----Running Moheft1----")
S1 = moheft(tasks_dict, resources_dict, dag_dict, K)
print("----Running Moheft2----")
S2 = moheft(tasks_dict, resources_dict, dag_dict, K+100)
print("----Running Moheft3----")
S3 = moheft(tasks_dict, resources_dict, dag_dict, K+200)

pairs = pair_solutions(S1, S2)

t1 = list()
t2 = list()

for (x, y) in pairs:
    t1.append(x.get_sorted_workflow())
    t2.append(y.get_sorted_workflow())

print('----Writing input training----')
f = open('training_dataset/{}-{}-input_training.txt'.format(filename, K), 'w')
f.write('{}'.format(t1))
f.close()
print('----Writing output training----')
f = open('training_dataset/{}-{}-output_training.txt'.format(filename, K), 'w')
f.write('{}'.format(t2))
f.close()

plot(S1, filename, 'input_training', K)
plot(S2, filename, 'output_training', K+100)
plot(S3, filename, 'moheft_output', K+200)

S4 = validate_solution(filename, tasks_dict, resources_dict, dag_dict, S2, 3*K)

plot(S4, filename, 'output_validation', K+200)