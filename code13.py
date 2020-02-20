#Ask 13

# getting the input card number 
digits = input("Give a credit card number(16 digits) :")

# checking that the digits of the input card number is 16
while len(digits) != 16:
    digits = input("Give a credit card number(16 digits) :")

# process to determine the validity of the card
numbers = []
for i in range(16):
    numbers.append(int(digits[i]))
for i in range(14, -1, -2):
    numbers[i] *= 2
    if numbers[i] >= 10:
        numbers[i] -= 9

# adding up the digits of the card number
sum = 0
for i in range(16):
    sum += numbers[i]

# printing
if sum%10 == 0:
    print("The input card number could be valid")
else:
    print("The input card number is not valid")