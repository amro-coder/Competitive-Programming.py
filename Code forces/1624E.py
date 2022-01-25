# Masha meets a new friend and learns his phone number — s.
# She wants to remember it as soon as possible.
# The phone number — is a string of length m that consists of digits from 0 to 9.
# The phone number may start with 0.
# Masha already knows n phone numbers (all numbers have the same length m).
# It will be easier for her to remember a new number if the s is represented as segments of numbers she already knows.
# Each such segment must be of length at least 2, otherwise there will be too many segments and Masha will get confused.
#
# For example, Masha needs to remember the number: s= '12345678' and she already knows n=4 numbers: '12340219', '20215601', '56782022', '12300678'.
# You can represent s as a 3 segment: '1234' of number one, '56' of number two, and '78' of number three.
# There are other ways to represent s.
#
# Masha asks you for help, she asks you to break the string s into segments of length 2 or more of the numbers she already knows.
# If there are several possible answers, print any of them.
#
# solution:
import sys
from collections import defaultdict
input=sys.stdin.readline
for _ in range(int(input())):
	empty=input()
	n,m=map(int,input().split())
	phones=[]
	for __ in range(n):
		phones.append(tuple(input()))
	s=tuple([" "]+list(input().strip()))
	twos=defaultdict(tuple,{phones[i][j:j+2]:(i+1,j+1) for i in range(n) for j in range(m-1)})
	threes=defaultdict(tuple,{phones[i][j:j+3]:(i+1,j+1) for i in range(n) for j in range(m-2)})
	dp=[False]*(m+1)
	dp[0]=True
	path=[[] for _ in range(m+1)]
	for i in range(m+1):
		if(dp[i]):
			if(i+2<=m):
				if(twos[s[i+1:i+3]]):
					dp[i + 2] = True
					path[i + 2]=[twos[s[i+1:i+3]][1],twos[s[i+1:i+3]][1]+1,twos[s[i+1:i+3]][0],i]
			if (i + 3 <= m):
				if (threes[s[i + 1:i + 4]]):
					dp[i + 3] = True
					path[i + 3]=[threes[s[i + 1:i + 4]][1], threes[s[i + 1:i + 4]][1] + 2, threes[s[i + 1:i + 4]][0], i]
	if(dp[-1]):
		ans=[]
		i=m
		while(i>0):
			ans.append([path[i][0],path[i][1],path[i][2]])
			i=path[i][-1]
		ans.reverse()
		print(len(ans))
		for i in ans:
			print(*i)
	else:
		print(-1)