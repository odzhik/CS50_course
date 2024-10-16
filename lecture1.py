# name = input("What is your name? ").strip().title()
# # print("Hello, " + name) 

# # print("Hello, ", end = "")
# # print(name)              / output: Hello, Olzhas

# # print("Hello, \"friend\"  ")    \"string\"  output: Hello, "friend"

# # print(f"Hello, {name}")           #f "{var}"

# # name = name.strip().title()    # strip() removes whitespaces
# first, last = name.split(" ")

# print(f"Hello, {first}")

# x = int(input("What is x? "))
# y = int(input("What is y? "))
# print(x + y)
# print(int(input("What is x? ")) + int(input("What is y? ")))


# x = float(input("What is x? "))
# y = float(input("What is y? "))
# z = (x / y)
# # print(round(z))

# print(f"{z:.10f}")

def hello(to):
    print("hello", to)



name = input("What is your name: ")
hello(name)