# factorial
def fact(num):
    n=1
    while num:
        n=n*num
        num=num-1
    return n
num=int(input("Enter a number:"))
print(fact(num))
