n = int(input())
min = 0
count = 0
noCount = 0
for i in range(n):
    f = int(input())
    if min == 0:
        min = f
    elif f < min:
        min = f
        count = 0
        count += 1
    elif min == f:
        count += 1
print(count + 1)