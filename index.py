# input_num = int(input("Enter some num "))


# def fizz_or_brizz(input_value):
#     if input_value % 3 == 0 and input_value % 5 == 0:
#         return "frizzbrizz"
#     elif input_value % 3 == 0:
#         return "fizz"
#     elif input_value % 5 == 0:
#         return "brizz"


# print(fizz_or_brizz(input_num))

# input_year = int(input("Enter year: "))


# def year(input_year):
#     if input_year % 4 == 0 and input_year % 100 != 0 and input_year % 400:
#         return "high year"
#     else:
#         return "not high year"


# print(year(input_year))


# def check_triangle(a, b, c):
#     sides = [(a, b, c), (b, c, a), (c, a, b)]

#     for x, y, z in sides:
#         if x + y > z:
#             print(f"sum of {x} {y} > {z}")
#         else:
#             print(f"sum of {x} {y} < {z}")
#             return

#     if a == b == c:
#         print("triangle all sides ==")
#     elif a == b or b == c or a == c:
#         print("2 sides ==")
#     else:
#         print("different sides")


# print(check_triangle(4, 2, 3))

# ================================ Registration =============================

from typing import Dict, Union

users: Dict[str, Dict[str, Union[int, str]]] = {}


def user_login() -> str:
    while True:
        try:
            user = input("please enter your login: ").strip()
            if user == "":
                raise ValueError("Input can not be empty")
        except ValueError as e:
            print("Warning!", e)
        return user


def user_age() -> int:
    while True:
        try:
            user_age = input("please enter your age: ")
            age = int(user_age)
            if age <= 0:
                raise ValueError("You can not be alive with less 0 years old")
            elif age < 18:
                print("You can not sign up, age must more then 17")
                continue
            return age
        except ValueError as e:
            print("Warning!", e)


def user_password() -> str:
    while True:
        try:
            user_password = input("Please create your password: ").strip()
            if user_password == "":
                raise ValueError("Please, enter your password for future sign in")
            return user_password
        except ValueError as e:
            print("Warning!", e)


def sign_up() -> None:
    print("=== Sign up ===")
    login = user_login()
    age = user_age()
    password = user_password()

    users[login] = {"age", age, "password", password}
    print(f"User {login} successfully registered")


def check_login() -> bool:
    print("=== Login ===")
    login = input("Please enter your login").strip()
    password = input("Please enter your password").strip()

    if login in users and users[login]["password"] == password:
        print(f"Welcome {login}, you are {users[login]['age']} years old")
        return True
    else:
        print("Invalid login or password")
        return False


if __name__ == "__main__":
    sign_up()
    check_login()
    print("\nRegistered users:", users)
