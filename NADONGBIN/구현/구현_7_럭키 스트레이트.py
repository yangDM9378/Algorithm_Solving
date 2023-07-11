"""
입력예시
123402

7755
"""

n=int(input())
half = len(str(n))//2
dhls = 0
dh = 0
for i in range(half):
    dhls += int(str(n)[i])

for j in range(half,len(str(n))):
    dh += int(str(n)[j])

if dhls == dh:
    print('LUCKY')
else:
    print('READY')