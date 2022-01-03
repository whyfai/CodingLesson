"""
The problem of picking peaches. 
Zhang San was in a shipwreck at sea and lived on a deserted island. 
He could only pick peaches and eat. 
I picked a few peaches on the first day and ate half of them immediately. 
It was not enough, so I ate one more, and the next morning I ate half of the remaining peaches and ate one more. 
After that, every morning I ate half and one of the remaining halves of the previous day. 
When I wanted to eat again in the morning of the 10th day, I saw that there was only one peach left. 
Please design a program to find out how many peaches Zhang San picked on the first day.
"""

peaches = 1
days = 9

print("Day 10: 1")

for i in range(9):
    peaches += 1
    peaches *= 2
    print(f"Day {days}: {peaches}")
    days -= 1

print(f"Zhang San picked {peaches} peaches on the first day.")