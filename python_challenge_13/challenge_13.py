from copy import deepcopy

test_input = {'0': 3,'1': 2,'4': 4,'6': 4}

challenge_input = {}

with open("input_day_13") as f:
    for line in f:
        depth, line_range = line.split(": ")
        challenge_input[depth] = int(line_range.strip())


class Firewall_layer:
    def __init__(self,depth, layer_range, scanner):
        self.depth = int(depth)
        self.range = layer_range
        self.position = 1
        if scanner: self.direction = 1
        else: self.direction = 0
        self.scanner = scanner

def total_range(current_input):
    if type(current_input) is list:
        return max(map(int,[x.depth for x in current_input]))+1
    elif type(current_input) is dict:
        return max(map(int,current_input.keys()))+1

def generate_state(current_input):
    current_state = []

    for i in range(total_range(current_input)):
        if str(i) in current_input:
            new_layer = Firewall_layer(i,current_input[str(i)], True)
        else:
            new_layer = Firewall_layer(i,0, False)
        current_state.append(new_layer)
    return current_state

def iterate_scanner_time(current_state):
    for current_layer in current_state:
        if current_layer.direction == 1 and current_layer.position == current_layer.range:
            current_layer.direction = -1
        elif current_layer.direction == -1 and current_layer.position == 1:
            current_layer.direction = 1
        current_layer.position += current_layer.direction
        #print "Currently operating on:", current_layer.depth, " and position is :", current_layer.position, " and direction is ", current_layer.direction
    return current_state

def print_state(current_state):
    for layer in current_state:
        print "Layer: {0}, Position: {1}, Range: {2}, Direction: {3}".format(layer.depth, layer.position, layer.range, layer.direction)
    print ""


def run_pass(current_state):
    total_severity = 0
    for my_position in range(total_range(current_state)):
        if current_state[my_position].position == 1:
            #print "Got caught at ", my_position
            total_severity += current_state[my_position].depth * current_state[my_position].range
            if current_state[my_position].depth == 0:
                total_severity += 1
        else:
            pass
            #print "Not caught for ", my_position, " - scanner was at ", current_state[my_position].position
        #print "My position: ", my_position
        #print_state(current_state)
        current_state = iterate_scanner_time(current_state)
    return total_severity


min_severity = 1000
i = 0

current_state = generate_state(challenge_input)

while min_severity > 0:
    new_state = deepcopy(current_state)
    new_severity = run_pass(new_state)
    #print new_severity
    if new_severity < min_severity:
        min_severity = new_severity
        print "New min at ", i, " severity ", new_severity
    if i % 10000 == 0:
        print i
    if i > 10000000:
        break
    current_state = iterate_scanner_time(current_state)
    i += 1
