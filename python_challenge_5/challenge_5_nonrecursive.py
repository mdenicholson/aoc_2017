
def process_instruction(current_position,instructions,steps):
    new_position = current_position + instructions[current_position] 
    new_instructions = instructions[:]
    new_instructions[current_position] += 1
    if new_position in range(0,len(instructions)):
        return process_instruction(new_position,new_instructions,steps+1)
    else:
        return steps + 1

with open("input_day_5") as f:
    instructions = [int(x.strip()) for x in f.readlines() if x.strip() != '']
    print(process_instruction(0,instructions,0))
