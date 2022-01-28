# from 1 to n
n=int(input())
temp = n % 4
if (temp == 0):
    print(n)
elif (temp == 1):
    print(1)
elif (temp == 2):
    print(n + 1)
else:
    print(0)