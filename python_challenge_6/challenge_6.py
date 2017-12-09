
with open("input_day_6") as f:
    data = map(int,f.readlines()[0].split())

print data

def identify_maximum(input_scenario):
    maximum = [(i,j) for i,j in enumerate(input_scenario) if j == max(input_scenario)]
    maximum_trimmed = maximum[0]
    return maximum_trimmed

def reallocate_data(input_scenario):
    maximum_trimmed = identify_maximum(input_scenario)
    quantity_to_redistribute = maximum_trimmed[1]
    number_of_cells = len(input_scenario)
    current_position = maximum_trimmed[0] 
    input_scenario[maximum_trimmed[0]] = 0
    while quantity_to_redistribute > 0:
        current_position += 1
        if current_position >= number_of_cells:
            current_position = 0
        input_scenario[current_position] += 1
        quantity_to_redistribute -= 1
    return input_scenario

data_list = []
i = 0
while True:
    i += 1
    data_list.append(data[:])
    data = reallocate_data(data)
    if data in data_list:
        print data, data_list
        first_occurance = [x for x in enumerate(data_list) if x[1] == data][0][0]
        break

print i
print i - first_occurance
