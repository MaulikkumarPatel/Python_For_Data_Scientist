# def prime_checker(number):
#     is_prime = True
#     for i in range(2, number):
#         if number % i == 0:
#             is_prime = False
#     if is_prime:
#         print("It's a prime number.")
#     else:
#         print("It's not a prime number.")
#
#
# n = int(input("Check this number: "))
# prime_checker(number=n)


def prime_checker(number="n"):
    if n == 2 or n == 3:
        print("It's a prime number.")
    elif n % 2 == 0 or n % 3 == 0:
        print("It's not a prime number.")
    else:
        print("It's a prime number.")


n = int(input("Check this number: "))
prime_checker(number=n)
