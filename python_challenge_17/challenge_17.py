
step = 366

current_buffer = [0]
current_position = 0
i = 1 

while i <= 2017:
    current_position = (current_position + step + 1) % i 
    current_buffer.insert(current_position, i)
    i += 1
index = current_buffer.index(2017)
print "Area around 2017 for part 1:", current_buffer[index-3:index+3]

current_buffer = [0]
current_position = 0
i = 1

while i <= 50000000:
    current_position = (current_position + step + 1) % i
    if current_position == current_buffer.index(0):
        current_buffer.insert(current_position + 1, i)
        print "Matched!. Current buffer: ", current_buffer
    if i % 1000000 == 0:
        print i
    i += 1

index = current_buffer.index(0)
print "Answer for part 2:", current_buffer[1]

