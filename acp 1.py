def check_age(age):
    print("Age is between 10 and 20." if 10 <= age <= 20 else "Age is NOT between 10 and 20.")

# Example usage
try:
    user_age = int(input("Enter your age: "))
    check_age(user_age)
except ValueError:
    print("Invalid input. Please enter a number.")

 
 
         

