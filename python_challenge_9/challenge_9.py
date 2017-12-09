
with open("input_day_9") as f:
    input_data = f.read()

def parse_inputs(input_data):
    garbage = False
    cancel = False
    total_score = 0
    current_score = 0
    garbage_count = 0
    for character in input_data:
        print character, garbage, cancel, total_score, current_score
        if cancel:
            cancel = False
            continue
        if character == "!":
            cancel = True
            continue
        if character == "<":
            if garbage == True:
                garbage_count += 1
            garbage = True
            continue
        if character == ">":
            garbage = False
            continue
        if garbage:
            garbage_count += 1
            continue
        if character == "{":
            current_score += 1
        if character == "}":
            total_score += current_score
            current_score -= 1
    return total_score, garbage_count

print parse_inputs(input_data)


