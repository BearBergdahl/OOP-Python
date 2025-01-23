# try - except
"""

while True:
    try:
        x = int(input("Enter the first number: "))
        print()
        y = int(input("Input the second number: "))
        print(x/y)
        break
    except (ValueError) as ve:
        print("You have to use a number...")
    except (ZeroDivisionError) as ze:
        print("No division by zero, second number can't be 0.")

# Assert

def my_logical_fail():
    a_true = True
    my_str = input("Give me a word please: \n")
    if my_str or a_true:
        print(my_str)
    assert not my_str == '' and not my_str == None, 'whoopsie no content in string'

my_logical_fail()
"""

containers_for_data = []
try:
    with open("./Exceptions/mynicedatafile.data",'r') as datasource:
        containers_for_data = datasource.readlines()
except(FileNotFoundError) as fe:
    print("Missing file")

for a_container in containers_for_data:
    print(a_container)
