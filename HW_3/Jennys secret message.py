def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    else: 
        return "Hello,{name}!".format(name=name)
greets = greet("Johnny")
print(greets)