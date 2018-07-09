from random import randint


def random_reconstruct(lcg_edges, start_node):
    new_lcg_edges = {}
    to_visit = [start_node]
    if start_node not in lcg_edges:
        return None
    while to_visit:
        for i in to_visit:
            if len(lcg_edges[i]) >= 1:
                choose = lcg_edges[i][randint(0, len(lcg_edges[i]) - 1)]
                new_lcg_edges[i] = [choose]
                new_lcg_edges[choose] = list(choose[0])
                to_visit.extend(choose[0])
            else:
                new_lcg_edges[i] = []
            to_visit.remove(i)
    return new_lcg_edges
