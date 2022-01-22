# Monocarp is playing a computer game once again. He is a wizard apprentice, who only knows a single spell.
# Luckily, this spell can damage the monsters.
# The level he's currently on contains n monsters.
# The i-th of them appears ki seconds after the start of the level and has hi health points.
# As an additional constraint, hi≤ki for all 1≤i≤n. All ki are different.
# Monocarp can cast the spell at moments which are positive integer amounts of second after the start of the level: 1,2,3,… The damage of the spell is calculated as follows.
# If he didn't cast the spell at the previous second, the damage is 1. Otherwise, let the damage at the previous second be x.
# Then he can choose the damage to be either x+1 or 1. A spell uses mana: casting a spell with damage x uses x mana.
# Mana doesn't regenerate.
# To kill the i-th monster, Monocarp has to cast a spell with damage at least hi at the exact moment the monster appears, which is ki.
# Note that Monocarp can cast the spell even when there is no monster at the current second.
# The mana amount required to cast the spells is the sum of mana usages for all cast spells. Calculate the least amount of mana required for Monocarp to kill all monsters.
# It can be shown that it's always possible to kill all monsters under the constraints of the problem.

#solution:
import sys
input=sys.stdin.readline
for _ in range(int(input())):
    n=int(input())+1
    sec=tuple([0]+list(map(int,input().split())))
    health=tuple([0]+list(map(int,input().split())))
    temp=0
    mana=[]
    target=health[-1]
    for i in range(n-1,0,-1):
        target=max(target,health[i])
        if(sec[i]-sec[i-1]>=target):
            mana.append(target+temp)
            temp=0
            target=0
        else:
            temp+=sec[i]-sec[i-1]
            target=target-(sec[i]-sec[i-1])
    ans=0
    for i in mana:
        ans+=(i * (i + 1)) // 2
    print(ans)