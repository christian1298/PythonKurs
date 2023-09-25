def my_and(a,b):
    return a and b

def my_or(a,b):
    return a or b

print("Adam" or False and "Eva")
print(("Adam" or False) and "Eva")
print("Adam" or (False and "Eva"))
print(5*"-")
print(my_or(my_and(False, "Eva"), "Adam"))
print(my_and(my_or("Adam", False), "Eva"))
print(my_or(my_and(False, "Eva"), "Adam"))