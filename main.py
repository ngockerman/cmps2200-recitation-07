from collections import defaultdict

def make_undirected_graph(edge_list):
    """ Makes an undirected graph from a list of edge tuples. """
    graph = defaultdict(set)
    for e in edge_list:
        graph[e[0]].add(e[1])
        graph[e[1]].add(e[0])
    return graph


def reachable(graph, start_node):
    """
    Returns:
      the set of nodes reachable from start_node
    """
    result = set([start_node])
    frontier = set([start_node])
    while len(frontier) != 0:
        ###TODO
        node = frontier.pop() ## removes and returns node to visit next
        for neighbor in graph[node]: # loops through all neighbors of node
            if neighbor not in result: # if we have not visited this node yet, marks it as visited and adds to fronteir to visit its neighbors later
                result.add(neighbor)
                fronteir.add(neighbor)
    return result





def connected(graph):
    ### TODO
    if not graph: # base case if graph is empty
        return True
    start = next(iter(graph)) # selects starting node 
    return len(reachable(graph, start)) == len(graph) # returns True if number of reachable nodes from starting node is the same as the total nodes in the graph and vice versa




def n_components(graph):
    """
    Returns:
      the number of connected components in an undirected graph
    """
    ### TODO
    visited = set() # initializes set to keep track of nodes assigned to connected component
    count = 0 # initializes variable to count total number of connected components
    for node in graph: # iterates through all nodes in the graph
        if node not in visited:
            component = reachable(graph, node) # if not already visited, finds all nodes connected and marks them as visited
            visited.update(component)
            count += 1 # accounts for new connected component
    return count

