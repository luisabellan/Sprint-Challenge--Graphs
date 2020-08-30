from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

from utils import Stack,Queue

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = [] 

# create graph
visited = {} 
for i in range(len(world.rooms)):
    visited[i] = {} 
# TODO populate graph


# print(f'visited: {visited}')


def get_neighbors(id):
    # finish this
    neighbors = []
    for i in visited[id]:
        neighbors.append(visited[id][i])
    # print(f"neighbors: {neighbors}")
    return neighbors
    
 

# Create an empty stack and add the starting_vertex
stack = Stack()
stack.push(player.current_room.id) 
# print(stack.stack)
# Create an empty set to track visited verticies
visited_vertices = set()
# while the stack is not empty:
while stack.size() > 0:
    # get current vertex (pop from stack)
    current_vertex = stack.pop()
    # Check if the current vertex has not been visited:
    if current_vertex not in visited_vertices:
        # print the current vertex
        # print(current_vertex)
        # Mark the current vertex as visited
        # Add the current vertex to a visited_set
        visited_vertices.add(current_vertex)


        # push up all the current vertex's neighbors (so we can visit them next)
        for neighbor_vertex in get_neighbors(current_vertex):
            stack.push(neighbor_vertex)


    # print(f'stack: {stack.stack}')
print(f'visited_verices:{visited_vertices}')
print(f'visited:{visited}')

    








# TRAVERSAL TEST - DO NOT MODIFY
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



######
# UNCOMMENT TO WALK AROUND
######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
