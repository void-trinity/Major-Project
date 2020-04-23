import matplotlib.pyplot as plt

def plot(S, filename, type, K):
    makespan_x = list()
    makespan_y = list()

    cost_x = list()
    cost_y = list()

    rel_inverse_x = list()
    rel_inverse_y = list()

    deg_of_imb_x = list()
    deg_of_imb_y = list()

    energy_x = list()
    energy_y = list()

    S = sorted(S, key = lambda x: x.id)


    for i in range(len(S)):
        makespan_x.append(i)
        makespan_y.append(S[i].makespan)
        cost_x.append(i)
        cost_y.append(S[i].total_cost)
        rel_inverse_x.append(i)
        rel_inverse_y.append(S[i].rel_inverse)
        deg_of_imb_x.append(i)
        deg_of_imb_y.append(S[i].degree_of_imbalance)
        energy_x.append(i)
        energy_y.append(S[i].energy)


    plt.plot(makespan_x, makespan_y, 'ro')
    plt.show()
    plt.close()

    plt.plot(cost_x, cost_y, 'ro')
    plt.show()
    plt.close()

    plt.plot(rel_inverse_x, rel_inverse_y, 'ro')
    plt.show()
    plt.close()

    plt.plot(deg_of_imb_x, deg_of_imb_y, 'ro')
    plt.show()
    plt.close()

    plt.plot(energy_x, energy_y, 'ro')
    plt.show()
    plt.close()