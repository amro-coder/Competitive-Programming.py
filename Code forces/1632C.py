# Igor is in 11th grade. Tomorrow he will have to write an informatics test by the strictest teacher in the school, Pavel Denisovich.
#
# Igor knows how the test will be conducted: first of all, the teacher will give each student two positive integers a and b (a<b).
# After that, the student can apply any of the following operations any number of times:
#
# a:=a+1 (increase a by 1),
# b:=b+1 (increase b by 1),
# a:=a | b (replace a with the bitwise OR of a and b).

# To get full marks on the test, the student has to tell the teacher the minimum required number of operations to make a and b equal.
#
# Igor already knows which numbers the teacher will give him.
# Help him figure out what is the minimum number of operations needed to make a equal to b.

#solution:
import sys
input=sys.stdin.readline
for _ in range(int(input())):
    a,b=map(int,input().split())
    ans=b-a
    for i in range(b,b+(b-a)+1):
        ans=min(ans,(a|i)-b+1)
    for i in range(a,b+1):
        ans=min(ans,(i-a)+((i|b)-b+1))
    print(ans)



