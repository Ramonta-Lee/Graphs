import random
from room import Room
from player import Player
from world import World

from world import World

from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)


# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = [] # need the letters
visited = {} # a dict with key of room id and values of 
directions = {"n": "s", "s": "n", "e": "w", "w":"e" }
path = []

visited[player.current_room.id] = player.current_room.get_exits()
# print("v", len(visited[0]))
# while len(visited[0])  > 0:
#     if player.current_room.id not in visited:
#         visited[player.current_room.id] = player.current_room.get_exits()
#         prev_dir = path[-1]

#         visited[player.current_room.id].remove(prev_dir)



# until the all rooms visited
# (-1 to subtrack from the graph for the room we are already in)
while len(visited) < len(room_graph) - 1: 
    # if the current room hasn't been visited
    if player.current_room.id not in visited:
        # add current exits
        visited[player.current_room.id] = player.current_room.get_exits()
        # store the previous location
        previous_direction = path[-1]
        # remove option because we have already visited the previous room
        visited[player.current_room.id].remove(previous_direction)
    
    while len(visited[player.current_room.id]) == 0:
        # remove the last direction (back track)
        previous_direction = path.pop()

        # record the room as you backtrack
        traversal_path.append(previous_direction)

        # move back
        player.travel(previous_direction)

    # remove unexplored directions from starting_room
    move = visited[player.current_room.id].pop(0)

    # add to the travesal path
    # print("prev_path", path)
    traversal_path.append(move)
    # print("traversal_path", traversal_path)
    # print("visited", visited)

    # add to "how we got here". (the breadcrumbs)
    # print("directions", directions)
    path.append(directions[move])

    # to move to the next room and get its info
    player.travel(move)




# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
