# 8. Scope
message = "a"
# if we commented this variable
# it will return None  when we call the function, also if we remove the comment
# we will get a shadow name message form outer scope ,local variable is not used

def greet(name):
    # message = "b"
    global message
    # global message
    message = "b"


greet("Mosh")
print(message, message )
