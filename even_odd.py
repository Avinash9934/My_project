#check even odd

def even_no(num):
    if num % 2 == 0:
        print(f"{num} is even numner")
    else:
        print(f"{num} is odd number")

inp=int(input("Enter a number:"))
even_no(inp)
