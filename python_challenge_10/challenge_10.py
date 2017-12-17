test_input_list = range(0,4)
test_input_lengths = [3,4,1,5]
input_list = range(0,255)
input_lengths = [88,88,211,106,141,1,78,254,2,111,77,255,90,0,54,205]

print test_input_list
print input_list

skip_size = 0

def process_hash(input_list, current_skip_size, input_length, current_position):
    reverse_list = input_list[current_position:current-position + input_length].reverse()
    full_reverse_list = 
