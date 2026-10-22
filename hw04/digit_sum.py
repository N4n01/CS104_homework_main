d_sum = 0

try :
    num = int(input("Enter a number(no negatives): "))
    if num < 0 :
        print("Please no negatives.")
    else : 
        while num > 0 :
            digit = num % 10
            d_sum += digit
            num = num // 10
            #print(f"{digit}, {d_sum}, {num}") #For testing code.
        print(f"Digit sum: {d_sum}")
except ValueError :
    print("Invalid value")


'''Old Code:
d1 = num // 100
d2 = (num-d1*100) // 10
d3 = (num-d1*100) % 10
print("Digit sum: ", d1+d2+d3)
'''