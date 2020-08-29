from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

from utils import Stack,Queue

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
map_file = "maps/test_loop.txt"
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
visited = {}
visited[player.current_room.id] = player.current_room.get_exits()

# ['e', 'e', 'w', 'w', 'w', 'e', 's', 's', 'w', 'e', 'n', 'n', 'n', 's'

# print(visited)
# player.travel('n')
# print(player.current_room)
# player.travel('n')
# print(player.current_room)

print(f'number of rooms: {len(world.rooms)}')
# print(player.current_room)


# traverse the rooms
while len(world.rooms) > len(visited):
    # if room not visited
    if player.current_room.id not in visited:
        # added as visited
        visited[player.current_room.id] = player.current_room.get_exits()
        # print(visited)
    if len(visited[player.current_room.id]) > 0:
        next_move = visited[player.current_room.id].pop()
        # print(next_move)
        player.travel(next_move)
        traversal_path.append(next_move)
        print(traversal_path)














# def dft(starting_vertex):
#     """
#     Print each vertex in depth-first order
#     beginning from starting_vertex.
#     """
#     # Create an empty stack and add the starting_vertex
#     stack = Stack()
#     stack.push(starting_vertex) 
#     # Create an empty set to track visited verticies
#     visited_vertices = set()
#     # while the stack is not empty:
#     while stack.size() > 0:
#         # get current vertex (pop from stack)
#         current_vertex = stack.pop()
#         # Check if the current vertex has not been visited:
#         if current_vertex not in visited_vertices:
#             # print the current vertex
#             print(current_vertex)
#             # Mark the current vertex as visited
#             # Add the current vertex to a visited_set
#             visited_vertices.add(current_vertex)


#             # push up all the current vertex's neighbors (so we can visit them next)
#             # for neighbor_vertex in self.get_neighbors(current_vertex):
#             #     stack.push(neighbor_vertex)


#         return None

# rooms = {

#     0 : {

#         'n': '',
#         's': '', 
#         'w': '',
#         'e': ''
#     }
# } 





   
            



    # def bft(self, starting_vertex):
    #     """
    #     Print each vertex in breadth-first order
    #     beginning from starting_vertex.
    #     """
    #     # Create an empty queue and enqueue the starting_vertex 
    #     queue = Queue()
    #     queue.enqueue({ 
    #         'current_vertex': starting_vertex,
    #         'path': [starting_vertex]        
    #     })
    #     # Create an empty set to track visited verticies
    #     visited_vertices = set()

    #     # while the queue is not empty:
    #     while queue.size() > 0:
    #         # get current vertex (dequeue from queue)
    #         # get current vertex PATH (dequeue from queue)
    #         current_obj = queue.dequeue()
    #         current_path = current_obj['path']
    #         # set the current vertex to the LAST element of the PATH
    #         current_vertex = current_obj['current_vertex']
    #         # Check if the current vertex has not been visited:
    #         if current_vertex not in visited_vertices:
    #             # print the current vertex
    #             print(current_vertex)
    #             # Mark the current vertex as visited
    #             # Add the current vertex to a visited_set
    #             visited_vertices.add(current_vertex)

    #             # queue up all the current vertex's neighbors (so we can visit them next)
    #             for neighbor_vertex in self.get_neighbors(current_vertex):
    #                 new_path = list(current_path)
    #                 new_path.append(neighbor_vertex)

    #                 queue.enqueue({
    #                     'current_vertex': neighbor_vertex,
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
