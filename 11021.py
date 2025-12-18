T = int(input())
results = []
for _ in range(T):
    A,B = map(int, input().split())
    results.append(A+B)
for i in range(T):
    print(f"Case #{i +1}: {results[i]}")