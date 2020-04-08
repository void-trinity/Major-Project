import matplotlib.pyplot as plt
from config.config import K
from helpers.init_resources import init_resources
from helpers.init_tasks import init_tasks
from helpers.init_task_dag import init_task_dag
from helpers.moheft import moheft
from helpers.pair_solutions import pair_solutions

total_resources = 30
total_resources2 = 60
total_resources3 = 120


filename = 'Montage_25.xml'


print("----Generating Resources Dict1----")
resources_dict = init_resources(total_resources)
print("----Generating Resources Dict2----")
resources_dict2 = init_resources(total_resources2)
print("----Generating Resources Dict3----")
resources_dict3 = init_resources(total_resources3)

print("----Generating Tasks Dict----")
tasks_dict = init_tasks(filename = filename)

print("----Generating Dag Dict----")
dag_dict = init_task_dag(tasks_dict)

print("----Running Moheft1----")
S1 = moheft(tasks_dict, resources_dict3, dag_dict)
# print("----Running Moheft2----")
# S2 = moheft(tasks_dict, resources_dict2, dag_dict)

# pairs = pair_solutions(S1, S2)
#
t1 = list()
# t2 = list()
#
# for (x, y) in pairs:
#     t1.append(x.get_sorted_workflow())
#     t2.append(y.get_sorted_workflow())
#
# print(t1)
# print(t2)
#
# print("----Running Moheft3----")
# S3 = moheft(tasks_dict, resources_dict3, dag_dict)
# t3 = list()
#
for s in S1:
    t1.append(s.get_sorted_workflow())

print(t1)

x_data = list()
y_data = list()
s_list = list()
for s in S1:
    x_data.append(s.makespan)
    y_data.append(s.total_cost)



plt.plot(x_data, y_data, 'ro')
plt.savefig('{}-{}-{}.png'.format(filename, K, total_resources))
