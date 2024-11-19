number = int(input("Enter a number :- "))
temp = number
rev = 0
# for numbers
while (temp>0):
    reminder = temp % 10    #last digit
    rev = rev * 10 + reminder #concat/reverse
    temp = temp // 10 #subtracting last_digit
if rev == number :
    print("Given number is a palindrome :- "+str(number))
else:
    print("Given number is not a palindrome :- " + str(number))
