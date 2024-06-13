'''import math
def calculate_square_root(a):
    try:
        assert a > 0, "Integer must be postive"
        return math.sqrt(a)
    except AssertionError:
        a = abs(a)
        return math.sqrt(a)
print(calculate_square_root(-9))'''

user = input("Enter your bill: \n")
user_2 = input("Enter number of people: \n")
try:
    bill_per_user = int(user)/ int(user_2)
    print(f"Bill per member is {bill_per_user}")
except ValueError:
    print("Enter only numerical values!")
except TypeError:
    print("Enter only numerical values!")


