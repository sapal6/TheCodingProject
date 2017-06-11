# There are 3 types of loops
#  While loop
#  For loop
#  Nested loops

# we shall decide wether the invading aliens are autobots or decepticons

aliens = input() # ask for user input

while aliens == "Autobots":
    print("you are one of the good guys")
    break
    print("you are just aliens")


# Let's run the code
    # When the input is Autobots it matches the required conditions and hence it returns a True so the code goes into infinite loop
# Now we shall provide a way for the code to break out of the infinite loop when the user input returns a True
# We will use a "break" statement which instructs teh code to break out of the loop once the print statement is executed


# We can use negative conditions for entering the while loop

while aliens is not "Autobots":  # resolves to False when the user inputs a wrong condition
   print("You are one of the bad guys")  # control enters the loop and print the statement when a false condition is returned
   break


# If statement can also be included inside a while statment to have more control over a decision making scenario


while aliens is not "Autobots":
    print(
        "Who is your leader : ")  # ask for user input
    leader = input()
    if leader == "Megatron":  # if resolves to True
        print(
            "You are one of the bad guys")  # print this statement and exit
    break