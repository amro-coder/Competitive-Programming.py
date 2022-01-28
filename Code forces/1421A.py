# In order to celebrate Twice's 5th anniversary, Tzuyu and Sana decided to play a game.
#
# Tzuyu gave Sana two integers a and b and a really important quest.
#
# In order to complete the quest, Sana has to output the smallest possible value of (a⊕x) + (b⊕x) for any given x.
# where ⊕ denotes the bitwise XOR operation.

# solution:
for _ in range(int(input())):
    a,b=map(int,input().split())
    print(a^b)