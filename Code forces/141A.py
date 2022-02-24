# So, the New Year holidays are over. Santa Claus and his colleagues can take a rest and have guests at last.
# When two "New Year and Christmas Men" meet, thear assistants cut out of cardboard the letters from the guest's name and the host's name in honor of this event.
# Then the hung the letters above the main entrance.
# One night, when everyone went to bed, someone took all the letters of our characters' names.
# Then he may have shuffled the letters and put them in one pile in front of the door.
#
# The next morning it was impossible to find the culprit who had made the disorder.
# But everybody wondered whether it is possible to restore the names of the host and his guests from the letters lying at the door?
# That is, we need to verify that there are no extra letters, and that nobody will need to cut more letters.
#
# Help the "New Year and Christmas Men" and their friends to cope with this problem.
# You are given both inscriptions that hung over the front door the previous night,
# and a pile of letters that were found at the front door next morning.


a=input().strip()
b=input().strip()
c=input().strip()
from collections import defaultdict
count=defaultdict(int)
for i in a:
    count[i]+=1
for i in b:
    count[i]+=1
for i in c:
    count[i]-=1
for key,value in count.items():
    if(value!=0):
        print("NO")
        break
else:
    print("YES")