#functions can return different values using if statements

def check_age(name,age):
    if age >= 21:
        return name + " is over 21"
    else:
        return name + " is under 21"

result = check_age("Sam", 15)
print(result)
result = check_age("Alex", 25)
print(result)