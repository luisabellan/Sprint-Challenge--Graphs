from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

from utils import Stack, Queue

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []






# create graph 
graph = {}
for i in range(len(world.rooms)):
 
    room = player.current_room.id
    graph[room] = {}
    edges = player.current_room.get_exits()
    # print(f'edges:{edges}')
    # populate edges values with '?' s
    for i in range(len(edges)):
        graph[room][edges[i]] = '?'
        # graph[room][edges[i]] = edges[i]

# print(graph)

def explore ():

    room_north = player.current_room.get_room_in_direction('n')
    room_south = player.current_room.get_room_in_direction('s')
    room_east = player.current_room.get_room_in_direction('e')
    room_west = player.current_room.get_room_in_direction('w')
    print(room_north)
    print(room_south)
    print(room_east)
    print(room_west)
    

# explore()
player.travel('n')



"""
Print each vertex in depth-first order
beginning from starting_room.
"""
# Create an empty stack and add the starting_room
stack = Stack()
stack.push(player.current_room)
# Create an empty set to track visited verticies
visited_rooms = set()

# while the stack is not empty:
while stack.size() > 0:
    # get current vertex (pop from stack)
    current_room = stack.pop()
    # Check if the current vertex has not been visited:
    if current_room not in visited_rooms:
        # print the current vertex
        # print(f'current_room: {current_room}')
        # Mark the current vertex as visited
        # Add the current vertex to a visited_set
        if type(current_room) == int:
            visited_rooms.add(current_room)


        # push up all the current vertex's neighbors (so we can visit them next)
        def get_neighbors(room):
            neighbors = []
            if type(room) != int:
                exits = room.get_exits()

          

            
                for exit in exits:
                    if exit == 'n':
                        neighbors.append(room.get_room_in_direction('n').id)
                    elif exit == 's':
                        neighbors.append(room.get_room_in_direction('s').id)
                    elif exit == 'w':
                        neighbors.append(room.get_room_in_direction('w').id)
                    elif exit == 'e':
                        neighbors.append(room.get_room_in_direction('e').id)

           
                print(f'neighbors: {neighbors}')
                print(f'exits: {exits}')
            return neighbors

        for neighbor_room in get_neighbors(current_room):
            stack.push(neighbor_room)
    # print(None)




# print(f'traversal_path:{traversal_path}')
# print(f'graph: {graph}')
# exits = player.current_room.get_exits()
# print(f'exits:{exits}')
print(f'visited_rooms:{visited_rooms}')
# print(f'current_room:{player.current_room.id}')
# print(f'current_room:{current_room}')


# def bft(self, starting_room):
#     """
#     Print each vertex in breadth-first order
#     beginning from starting_room.
#     """
#     # Create an empty queue and enqueue the starting_room
#     queue = Queue()
#     queue.enqueue({
#         'current_room': starting_room,
#         'path': [starting_room]
#     })
#     # Create an empty set to track visited verticies
#     visited_rooms = set()

#     # while the queue is not empty:
#     while queue.size() > 0:
#         # get current vertex (dequeue from queue)
#         # get current vertex PATH (dequeue from queue)
#         current_obj = queue.dequeue()
#         current_path = current_obj['path']
#         # set the current vertex to the LAST element of the PATH
#         current_room = current_obj['current_room']
#         # Check if the current vertex has not been visited:
#         if current_room not in visited_rooms:
#             # print the current vertex
#             print(current_room)
#             # Mark the current vertex as visited
#             # Add the current vertex to a visited_set
#             visited_rooms.add(current_room)

#             # queue up all the current vertex's neighbors (so we can visit them next)
#             for neighbor_room in self.get_neighbors(current_room):
#                 new_path = list(current_path)
#                 new_path.append(neighbor_room)

#                 queue.enqueue({
#                     'current_room': neighbor_room,
#                     'path': new_path
#                 })
#     return None


# print(dft(player.current_room))


# TRAVERSAL TEST - DO NOT MODIFY
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(
        f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
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
#

