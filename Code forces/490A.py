# The School №0 of the capital of Berland has n children studying in it.
#  All the children in this school are gifted: some of them are good at programming, some are good at maths, others are good at PE (Physical Education).
#  Hence, for each child we know value ti:
#  ti=1, if the i-th child is good at programming,
#  ti=2, if the i-th child is good at maths,
#  ti=3, if the i-th child is good at PE
# Each child happens to be good at exactly one of these three subjects.
# The Team Scientific Decathlon Olympias requires teams of three students.
#  The school teachers decided that the teams will be composed of three children that are good at different subjects.
#  That is, each team must have one mathematician, one programmer and one sportsman.
#  Of course, each child can be a member of no more than one team.
# What is the maximum number of teams that the school will be able to present at the Olympiad?
#  How should the teams be formed for that?
#
#
#
#  solution:

n=int(input())
x=list(map(int,input().split()))
ones=[]
twos=[]
threes=[]
for i in range(n):
    if(x[i]==1):
        ones.append(i)
    elif(x[i]==2):
        twos.append(i)
    else:
        threes.append(i)
print(min(len(ones),len(twos),len(threes)))
for i in range(min(len(ones),len(twos),len(threes))):
    print(ones[i]+1,twos[i]+1,threes[i]+1)
