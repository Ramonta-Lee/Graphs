class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        
        else:
            raise IndexError("Vertex does not exist")

    def get_parents(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]


data = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

def earliest_ancestor(ancestors, starting_node):
    g = Graph()

    # loop through data
    for i in ancestors:
        parent = i[1]
        child = i[0]
        # add child/parent nodes to graph
        g.add_vertex(parent)
        g.add_vertex(child)
        # add edges to nodes
        g.add_edge(parent, child)

    # keep track of paths    
    path_list = []

    # keep track of what is being traversed
    stack = Stack()
    # push starting_node on to stack
    stack.push([starting_node])
    # store visited nodes
    visited = set()
    # traverse the stack
    while stack.size() > 0:
        # store list in path
        path = stack.pop()
        cur_node = path[-1]
        # if the current node hasn't been visited
        if cur_node not in visited:
            # print(cur_node, path)
            # add path to list of paths
            path_list.append(path)
            # add it to visited
            visited.add(cur_node)
            # get neighbors of node
            for parent in g.get_parents(cur_node):
                new_path = list(path)
                new_path.append(parent)
                stack.push(new_path)

    print(path_list)
    if len(path_list) == 1:
     return -1
    else:
       i = 0
       j = 1
       correct_list = []
       
       while j < len(path_list):
        if len(path_list[i]) == len(path_list[j]):

         if path_list[i][-1] < path_list[j][-1]:
          correct_list = path_list[i]

         else:
          correct_list = path_list[j]

        else:
         # that last path in the list of paths will hold the earliest ancestor
         correct_list = path_list[j]

        i += 1
        j += 1

       return correct_list[-1]

# def earliest_ancestor(ancestors, starting_node):
#     new_graph = Graph()

#     for each in ancestors:
#         parent = each[0]
#         child = each[1]

#         new_graph.add_vertex(parent)
#         new_graph.add_vertex(child)

#         new_graph.add_edge(child, parent) # adding in this direction goes up the graph

#     path_list = [] # keeps track of the paths
#     stack = Stack() # for traversing
#     stack.push([starting_node])
#     visited = set() # keeps track of nodes visited
#     while stack.size() > 0:
#         path = stack.pop()
#         current = path[-1]
#         if current not in visited:
#             path_list.append(path)
#             visited.add(current)
#             for parent in new_graph.get_parents(current):
#                 # copy of list so far
#                 new_paths = list(path)
#                 # add neighbors to new_path
#                 new_paths.append(parent)
#                 # add lists to stack for travel
#                 stack.push(new_paths)

#     print("path_list", path_list)  


earliest_ancestor(data, 8)

        
        



