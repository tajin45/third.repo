number = 0
sum = 0
count = 0
average = 0
while True:
    number = input(">")
    if number == "done":
        break    
    try:
        input_number = float(number)
        sum = sum + input_number
        count = count + 1
    except:
        print("Enter only numbers or type done to end")
        if count == 0:
            print("You cannot proceed")
            break
average = sum / count
print("Sum of the number is ",sum)
print("Count of the numbers is ",count)
print("Average of the number is ",average)
