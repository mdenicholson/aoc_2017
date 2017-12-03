input_file = "input_day_2"

with open(input_file) as input_checksum_file:
    input_array = []
    for line in input_checksum_file.readlines():
        line_array = line.split()
        line_array[-1] = line_array[-1].strip()
        line_array = map(int, line_array)
        input_array.append(line_array)
    
checksum = 0
for line in input_array:
    line_min = min(line)
    line_max = max(line)
    checksum += (int(line_max) - int(line_min))
print("Checksum for first part: " + str(checksum))

# Brute Force
checksum_2 = 0
for line in input_array:
    for entry_1 in line:
        for entry_2 in line[:]:
            if entry_1 % entry_2 == 0 and entry_1 != entry_2:
                checksum_2 += entry_1 / entry_2
print("Checksum for second part: " + str(checksum_2))

