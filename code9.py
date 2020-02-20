#Ask 9

# getting the input number
number = float(input("Give a number: "))
sum = 0
steps = 0
number = number*3+1
while number >= 10 or number <= -10:
    # printing the number after process cycle
    print (number)
    if steps > 0:
        number = number*3+1
    if number > 0:
        number = str(number)
        for i in range(len(number)):
            if number[i] != ".":
                sum += int(number[i])
    elif number < 0:
        number = str(number)
        for i in range(1, len(number)):
            if number[i] != ".":
                sum -= int(number[i])
    number = sum
    steps += 1
    sum = 0
# printing the one digit number
print(number)