import numpy as np
import random


def generate_random_an(size, num_tran):
    if num_tran > size * size:
        num_tran = size * size
    transition_set = []
    for i in range(num_tran):
        head = random.randint(1, size)
        temp = list(range(1, size + 1))
        sign = random.choice([1, -1])
        temp.remove(head)
        head = head * sign
        sign = random.choice([1, -1])
        dice = random.choice(temp)
        body = [sign * dice]
        temp.remove(dice)
        next_transition = 1
        while next_transition > 0.2 and temp:
            next_transition = random.random()
            sign = random.choice([1, -1])
            dice = random.choice(temp)
            body.append(sign * dice)
            temp.remove(dice)
        trans = [head, body]
        mark = False
        for j in transition_set:
            if head == j[0] and set(body) > set(j[1]):
                mark = True
                break
        if mark:
            continue
        if [-head, body] not in transition_set:
            transition_set.append(trans)
    return transition_set


def generate_random_continuous_model(num_var):  # change rate is limited in [-1,-0.5][0.5,1]
    eq = np.zeros((num_var, num_var))
    for i in range(num_var):
        next_var = 1
        var_set = list(range(num_var))
        var_set.pop(i)
        while next_var > 0.2 and var_set:
            next_var = random.random()
            sign = random.choice([1, -1])
            dice = random.choice(var_set)
            eq[i][dice] = sign * (0.5 + random.random() / 2)
            var_set.remove(dice)
    return eq


def evolve(initial_state, period, eq, noise):
    time_series = np.zeros((len(initial_state), period + 1))
    for i in range(len(initial_state)):
        time_series[i][0] = initial_state[i]
    for j in range(period):
        for i in range(len(initial_state)):
            temp = time_series[i][j]
            for k in range(len(initial_state)):
                temp = temp + time_series[k][j] * eq[i][k] + (random.random() - 0.5) * 2 * noise
            time_series[i][j + 1] = temp
    return time_series
