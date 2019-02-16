def simplerec(number):
    if number > high_num:
        return high_num
    if number % 15 == 0:
        print ("Fizz Buzz")
    elif number % 5 == 0:
        print ("Buzz")
    elif number % 3 == 0:
        print("Fizz")
    else:
        print(number)
    simplerec(number + 1)

low_num = 1
high_num = 100
simplerec(low_num)
