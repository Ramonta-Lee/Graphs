"""
DFS
The farthest distance from the input individual = earliest ancestor

If there is more than one earliest then take the smaller NUMERIC ID


If the input individual has no parents, the function should RETURN -1.

Given a list of Tuples = matrix
ancestors [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

1. make EDGES between nodes
2. trace path upward to last node (longest path)
3. store path lengths and compare them to get the earliest ancestor
"""

def earliest_ancestor(ancestors, starting_node):
    graph = {}

    # make edges between nodes:
    for each in ancestors:
        # iterate over the tuples
        if each[1] in graph:
            # if the 1st elem of the tup
            # is in the graph
            # add the 2nd elem 
            # 
            graph[each[1]].append(each[0])
        
        else:
            graph[each[1]] = [each[0]]
    """
    Now I have a matrix with the nodes[0] from the tuple as keys
    The connections those nodes have (values) are in a list  for each key in the matrix
    The keys are the parents and the children are the values

    we want to see which keys have the values of the starting node(example: 6):
    (k) 5: (v) [6,7], 3: [6]
    5 and 3 become next starting_node
    1: [3], 2: [3], 4: [5, 8]
    1, 2, 4 become next starting_node
    10: [1]
    """
    key_list = []
    key_list.append([starting_node])
    # get the neighbors of starting_node
    # check the key and compare the value to the starting_node
    # if the key matches the starting_node then add to a list
    # they become the next starting_node
    # keep going until key is None
    for key in graph:
        print("key", key)
        for value in graph[key]:
            print("value", value)
            if value == key_list[0]:
                key_list.append(key)
    
            
    # print("key", key_list)

    if starting_node not in graph:
        return -1

    # Next phase:
    # DFS Traversal
    # implement while loop to build path to earliest ancestor
    # pop off from the key_list
    # return the last value from the path as that should be the earliest ancestor

    paths = []
    while len(key_list) > 0:
        path = key_list.pop()
        node = path[-1]
        if node in graph:
            for i in graph[node]:
                print("i", i)
                new_path = list(path)
                new_path.append(i)
                key_list.append(new_path)
        else:
            paths.append(path)
    print("paths", paths, "new_path: ", new_path)
        


    return print("key_list", key_list, "graph", graph, "new_path", new_path[0])

# test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
# earliest_ancestor(test_ancestors, 10)

   

#     ancestors = reverse_graph(ancestors)
#     print("ancestors", ancestors)
#     graph = {}
#     for edge in ancestors:
#         if edge[0] in graph:
#             graph[edge[0]].append(edge[1])
#         else:
#             graph[edge[0]] = [edge[1]]
#     print("graph", graph)

#     if starting_node not in graph:
#         return -1

#     q = []
#     q.append([starting_node])
#     paths = []
#     # path = [[starting_node]]
#     while len(q)> 0:
#         path = q.pop()
#         node = path[-1]
#         if node in graph:
#             for i in graph[node]:
#                 new_path = list(path)
#                 new_path.append(i)
#                 q.append(new_path)
#         else:
#             paths.append(path)
#     print(paths)

#     longer_path = {}
#     for path in paths:
#         if len(path) not in longer_path:
#             longer_path[len(path)] = path
#         elif path[-1] < longer_path[len(path)][-1]:
#             longer_path[len(path)] = path
#     print("longer path", longer_path)
#     return longer_path[max(longer_path)][-1]

# def reverse_graph(ancestors):
#     reverse = []
#     for i in ancestors:
#         reverse.append((i[1],i[0]))
#     print("reverse", reverse)
#     return reverse

