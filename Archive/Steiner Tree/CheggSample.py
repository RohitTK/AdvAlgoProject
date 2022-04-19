from itertools import chain

from networkx.utils import pairwise, not_implemented_for
import networkx as nx

_all_ = ["metric_closure", "steiner_tree"]


#[docs]@not_implemented_for("directed")

def metric_closure(G, weight="weight"):
    M = nx.Graph()

    Gnodes = set(G)

    # check for connected graph while processing first node
    all_paths_iter = nx.all_pairs_dijkstra(G, weight=weight)
    u, (distance, path) = next(all_paths_iter)
    if Gnodes - set(distance):
        msg = "G is not a connected graph. metric_closure is not defined."
        raise nx.NetworkXError(msg)
    Gnodes.remove(u)
    for v in Gnodes:
        M.add_edge(u, v, distance=distance[v], path=path[v])

    # first node done -- now process the rest
    for u, (distance, path) in all_paths_iter:
        Gnodes.remove(u)
    for v in Gnodes:
        M.add_edge(u, v, distance=distance[v], path=path[v])

    return M

#[docs]@not_implemented_for("directed")
def steiner_tree(G, terminal_nodes, weight="weight"):
    # H is the subgraph induced by terminal_nodes in the metric closure M of G.
    M = metric_closure(G, weight=weight)
    H = M.subgraph(terminal_nodes)
    # Use the 'distance' attribute of each edge provided by M.
    mst_edges = nx.minimum_spanning_edges(H, weight="distance", data=True)
    # Create an iterator over each edge in each shortest path; repeats are okay
    edges = chain.from_iterable(pairwise(d["path"]) for u, v, d in mst_edges)
    # For multigraph we should add the minimal weight edge keys
    if G.is_multigraph():
        edges = (
        (u, v, min(G[u][v], key=lambda k: G[u][v][k][weight])) for u, v in edges
        )
        T = G.edge_subgraph(edges)
        return T