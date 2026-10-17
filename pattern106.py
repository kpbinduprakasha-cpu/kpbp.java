while True:
    age = input("Enter your age: ")
    
    if age.isdigit():  
        print(f"Got it, you are {age}.")
        break          
        
    print("Invalid input. Please type a number.")
