import math
import numpy as np

def side_length(x):
    return (np.ceil(math.sqrt(x)) // 2 )* 2 + 1

def start_offset(x):
    return ((side_length(x) - 1) / 2)

def ring_start_number(x):
    return (side_length(x) - 2)**2

def manhattan_distance(x):
    # Calculate manhattan distance by identifying how far out the ring is
    # and how far around the ring each point is
    offset = math.fabs((x - ring_start_number(x)) % (side_length(x) - 1) - (side_length(x)-1)/2) 
    return offset + (side_length(x)-1)/2

def provide_data(x):
    print("Number: {0}. Side length: {1}. Start offset: {2}. Manhattan Distance: {3}".format(
            x,side_length(x),start_offset(x),manhattan_distance(x)))

provide_data(1024)
provide_data(325489)



# Below here started working on part 2, but unfinished as yet
size = 1000
output_array = np.zeros(shape=(size,size))
current_position = [size/2, size/2]
output_array[current_position[0],current_position[1]]=1

def current_value(position,array):
    sum_of_nearby = 0
    for i in range(-1,2):
        for j in range(-1,2):
            if i != 0 and j != 0:
                sum_of_nearby += array[position + i, position + j]
    return sum_of_nearby
    
    
def increment_position(position,array):
    pass

def choose_next_cell(position,offset):
    normalised_position = [position[0] - offset, position[1] - offset]



