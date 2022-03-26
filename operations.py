def Armstrong(a):
    b = 0
    c = a
    while c > 0:
        digit = c % 10
        b += digit ** 3
        c //= 10
    if a == b:
        return True
    else:
        return False
def divisible(x):
    if x%5==0:
        return True
    else:
        return False
def largest(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c
def even(a):
    if a%2==0:
        return True
    else:
        return False
# x = int(input("Enter the number for armstrong"))
# a = Armstrong(x)
# print(a)
# y = int(input("Enter for divisible"))
# b = divisible(y)
# print(b)
# m = int(input("Enter num1 :"))
# n = int(input("Enter num2 :"))
# o = int(input("Enter num3 :"))
# result = largest(m,n,o)
# print("largest is "result)