# Simple calculator
def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def divide(num1, num2):
    return num1 // num2

def multiply(num1, num2):
    return num1*num2

while True:
    
    while True:
        user_input=input("What math calc u wanna do among ('add','subtract','divide','multiply'))? ").split()
        if len(user_input)==1:
            if user_input[0] not in ["add","subtract","divide","multiply"]:
                print("Invalid input", user_input[0])
                break
        else:
            print("Invalid input")
            break
        print("Enter the nummbers...")
        num1 = input("number 1: ")
        num2 = input("number 2: ")
        try:
            num1 = int(num1)
            num2 = int(num2)
            match user_input[0]:
                case "add":
                    print("Added value: ", add(num1, num2))
                    break
                case "subtract":
                    print("Subtracted value: ", subtract(num1, num2))
                    break
                case "divide":
                    print("Divided value: ", divide(num1, num2))
                    break
                case "multiply":
                    print("Multiplied value: ", multiply(num1, num2))
                    break
                    
        except:
            print("Please enter valid number")
        
    
    while True:
        yesNo = input("Do u wanna continue? (yes/no)?")
        if yesNo == "no":
            exit()
        elif yesNo != "no" and yesNo != "yes":
            print("please enter valid value")
        else:
            break