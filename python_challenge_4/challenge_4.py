
input_file = "input_day_4_2"

def check_validity_part_1(line):
    validity = 1
    for i in line.split():
        if line.count(i) != 1:
            validity = 0
    return validity

def check_validity_part_2(line):
    validity = 1
    line_array = line.split()
    print line_array
    letters_array = [sorted(list(x)) for x in line_array]
    print letters_array
    for word in letters_array:
        if letters_array.count(word) != 1:
            validity = 0
    return validity


with open(input_file) as f:
    valid_passphrases = 0
    for line in f.readlines():
        valid_passphrases += check_validity_part_2(line)

    print valid_passphrases

