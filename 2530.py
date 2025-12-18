A, B, C = map(int, input().split())
D = int(input())
C = C + D

while A >= 24:
    A = A-24
while B >= 60:
    A += 1
    B = B-60
while C >= 60:
    B += 1
    C = C-60

print(A,B,C)