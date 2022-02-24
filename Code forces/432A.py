# The Saratov State University Olympiad Programmers Training Center (SSU OPTC) has n students.
#  For each student you know the number of times he/she has participated in the ACM ICPC world programming championship.
#  According to the ACM ICPC rules, each person can participate in the world championship at most 5 times.
# The head of the SSU OPTC is recently gathering teams to participate in the world championship.
#  Each team must consist of exactly three people, at that, any person cannot be a member of two or more teams.
#  What maximum number of teams can the head make if he wants each team to participate in the world championship with the same members at least k times?

n,k=map(int,input().split())
x=list(map(int,input().split()))
members=0
for i in x:
    if(i+k<=5):
        members+=1
print(members//3)
