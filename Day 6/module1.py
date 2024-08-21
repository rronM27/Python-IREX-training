

string_lenth=len("Hello World")
list_length=len([5,6,2,4,8])
tuple_length=len((5,6,2,4,8))
print(string_lenth)
print(list_length)
print(tuple_length)


def add(x,y):
    return x + y

def contatinate(x,y):
    return str(x)+str(y)

def operate(operation,x,y):
    return operation(x,y)


print(operate(add,5,6))
