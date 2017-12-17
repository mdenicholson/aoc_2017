import string

with open("input_day_16") as f:
    inputs = f.readlines()[0]

def do_spin(input_list, spin_size):
    return input_list[-spin_size:] + input_list[:-spin_size]

def do_exchange(input_list, A, B):
    output_list = input_list[:]
    output_list[A], output_list[B] = input_list[B], input_list[A]
    return output_list

def do_partner(input_list, A, B):
    output_list = input_list[:]
    A_index, B_index = input_list.index(A), input_list.index(B)
    output_list[A_index], output_list[B_index] = input_list[B_index], input_list[A_index]
    return output_list

test_input = ["a","b","c","d","e"]

def do_move(input_list, move_command):
    if move_command[0] == "s":
        return do_spin(input_list,int(move_command.replace("s","")))
    elif move_command[0] == "x":
        A,B = map(int,move_command.replace("x","").split("/"))
        return do_exchange(input_list,A,B)
    elif move_command[0] == "p":
        A,B = move_command[1:].split("/")
        return do_partner(input_list,A,B)
    else:
        raise Exception("Input not parsed properly")

original_string = list(string.ascii_lowercase)[:16]
latest_string = original_string[:]

for command in inputs.split(","):
    latest_string = do_move(latest_string, command)

print "Answer to part 1:", latest_string

i = 1

list_of_solutions = [original_string]
while i < 1000:
    list_of_solutions.append(latest_string)
    for command in inputs.split(","):
        latest_string = do_move(latest_string, command)
    if latest_string in list_of_solutions:
        print "Repeat at i: ", i
        print "Repeat was:", latest_string
        break
    i += 1

repeat_frequency = i

representative_rotations = 1000000000 % repeat_frequency
print "Number of rotations:", representative_rotations
print list_of_solutions[representative_rotations]

