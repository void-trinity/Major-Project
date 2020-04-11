import matplotlib.pyplot as plt

def plot(S, filename, type, K):
    makespan_x = list()
    makespan_y = list()

    cost_x = list()
    cost_y = list()

    rel_inverse_x = list()
    rel_inverse_y = list()

    S = sorted(S, key = lambda x: x.id)


    for i in range(len(S)):
        makespan_x.append(i)
        makespan_y.append(S[i].makespan)
        cost_x.append(i)
        cost_y.append(S[i].total_cost)
        rel_inverse_x.append(i)
        rel_inverse_y.append(S[i].rel_inverse)




    plt.plot(makespan_x, makespan_y)
    plt.savefig('graphs/{}-{}-{}-makespan.png'.format(filename, K, type))
    plt.close()

    plt.plot(cost_x, cost_y)
    plt.savefig('graphs/{}-{}-{}-cost.png'.format(filename, K, type))
    plt.close()

    plt.plot(rel_inverse_x, rel_inverse_y)
    plt.savefig('graphs/{}-{}-{}-rel_inv.png'.format(filename, K, type))
    plt.close()
