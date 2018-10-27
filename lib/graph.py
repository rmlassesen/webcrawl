import matplotlib.pyplot as plt
import networkx as nx
from collections import Mapping

def nest_replace(dictionary, url_indexes, url_index_count):
    new_dict = {}
    for key, value in dictionary.items():
        if not key in url_indexes:
            url_index_count += 1
            url_indexes[key] = url_index_count
            new_dict[url_index_count] = None

        if isinstance(value, dict):
            new_dict[url_index_count], url_indexes, url_index_count = nest_replace(value, url_indexes, url_index_count)

    return new_dict, url_indexes, url_index_count


def make_graph(dict_nest, figuresize):
    url_indexes = {}
    url_index_count = 0

    dict_nest, url_indexes, url_index_count = nest_replace(dict_nest, url_indexes, url_index_count)

    G = nx.DiGraph()
    q = list(dict_nest.items())

    while q:
        value, dictionary = q.pop()
        for new_value, new_dictionary in dictionary.items():
            G.add_edge(value, new_value)
            if isinstance(new_dictionary, Mapping):
                q.append((new_value, new_dictionary))

    plt.figure(1, figsize=(figuresize))
    nx.draw(G, with_labels=True)

    return plt, url_indexes, url_index_count