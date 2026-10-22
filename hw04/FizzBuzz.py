for i in range (1, 101) :
    if (i % 3 == 0 or "3" in str(i)) and (i % 5 == 0 or "5" in str(i)) :
        print("FizzBuzz")
    elif i % 3 == 0 or "3" in str(i):
        print('Fizz')
    elif i % 5 == 0 or "5" in str(i):
            print('Buzz')
    else :
         print(i)



#Unused older code line:    if i % 15 == 0 or ("3" in str(i) and "5" in str(i)):
