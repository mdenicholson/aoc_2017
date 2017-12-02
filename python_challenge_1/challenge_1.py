import os

input_file = "input_file"
#input_file = "test_input"

with open(input_file) as input_captcha_file:
    input_captcha = input_captcha_file.read().rstrip()
    i=0
    sum=0
    input_length = len(input_captcha)
    while i < input_length-1:
        if input_captcha[i] == input_captcha[i+1]:
            sum+=int(input_captcha[i])
        i+=1
    if input_captcha[i] == input_captcha[0]:
        sum+=int(input_captcha[i])
    print("First part: " + str(sum))


    i=0
    sum=0
    doubled_input_captcha = input_captcha + input_captcha
    while i < input_length:
        if input_captcha[i] == doubled_input_captcha[i+input_length / 2]:
            sum+=int(input_captcha[i])
        i+=1
    print("Second part: " + str(sum))
