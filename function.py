def call(name):
    print(f"Hello, {name}!")    
    print("Welcome to the program.")

call("Alice")
call("Bob")
call("Charlie")

def make_full_name(first_name, last_name):
    full_name = first_name + " " + last_name
    return full_name

full_name = make_full_name("tyme", "principal")
print(full_name)


def add(a, b):
    return a + b
a=input("enter a number")
b=input("enter a number")
answer = add(int(a), int(b))
print(answer)

