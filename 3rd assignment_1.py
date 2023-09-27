while True:
    try:
        hours = int(input("Enter your work hour: "))
    except:
        print("\nEnter a valid number")
        break
    try:
        rate = float(input("Enter payment rate per hour:"))
    except:
        print("Enter the correct value")
        break
    salary = hours * rate
    if (hours > 40):
        overtime = hours - 40
        overtime_salary = overtime * (rate * 1.5)
        total_salary = salary + overtime_salary - (overtime * rate)
        print("Your salary is ",total_salary)
        break
    elif (hours <= 40):
        print("Your salary is ",salary)
        break