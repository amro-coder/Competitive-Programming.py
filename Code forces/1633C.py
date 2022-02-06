# Monocarp is playing a computer game. In this game, his character fights different monsters.
#
# A fight between a character and a monster goes as follows.
# Suppose the character initially has health hC and attack dC; the monster initially has health hM and attack dM.
# The fight consists of several steps:
#
# the character attacks the monster, decreasing the monster's health by dC;
# the monster attacks the character, decreasing the character's health by dM;
# the character attacks the monster, decreasing the monster's health by dC;
# the monster attacks the character, decreasing the character's health by dM;
# and so on, until the end of the fight.
# The fight ends when someone's health becomes non-positive (i. e. 0 or less).
# If the monster's health becomes non-positive, the character wins, otherwise the monster wins.
#
# Monocarp's character currently has health equal to hC and attack equal to dC.
# He wants to slay a monster with health equal to hM and attack equal to dM.
# Before the fight, Monocarp can spend up to k coins to upgrade his character's weapon and/or armor;
# each upgrade costs exactly one coin, each weapon upgrade increases the character's attack by w,
# and each armor upgrade increases the character's health by a.
#
# Can Monocarp's character slay the monster if Monocarp spends coins on upgrades optimally?

#solution:
import sys, math
input = sys.stdin.readline
def can_we(hc, dc):
    char = math.ceil(hm / dc)
    monster = math.ceil(hc / dm)
    if (char <= monster):
        return True
    else:
        return False

for _ in range(int(input())):
    hc, dc = map(int, input().split())
    hm, dm = map(int, input().split())
    k, w, a = map(int, input().split())
    for i in range(k + 1):
        if (can_we(hc + (a * i), dc + ((k - i) * w))):
            print("YES")
            break
    else:
        print("NO")