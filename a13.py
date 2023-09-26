def my_and(a,b):
    if a and b: return b
    else: return False

def my_or(a,b):
    if a or b:
        if a: return a
        else: return b
    else: return b

# print("Adam" or False and "Eva")
# print(("Adam" or False) and "Eva")
# print("Adam" or (False and "Eva"))
# print(5*"-")
# print(my_or(my_and(False, "Eva"), "Adam"))
# print(my_and(my_or("Adam", False), "Eva"))
# print(my_or(my_and(False, "Eva"), "Adam"))

def my_and2(a,b):
    if a: return b
    return a

def my_or2(a,b):
    if a: return a
    return b


print("Adam" or False and "Eva")
print(("Adam" or False) and "Eva")
print("Adam" or (False and "Eva"))
print(5*"-")
print(my_or2(my_and2(False, "Eva"), "Adam"))
print(my_and2(my_or2("Adam", False), "Eva"))
print(my_or2(my_and2(False, "Eva"), "Adam"))
