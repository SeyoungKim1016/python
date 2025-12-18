T = int(input())
results = []
for _ in range(T):
    A,B = map(int, input().split())
    results.append(A+B)
for i in range(T):
    print(f"Case #{i +1}: {A} + {B} = {results[i]}")
    
//T = int(input())

for i in range(1, T+1):
    A, B = map(int, input().split())
    print("Case #" + str(i) + ":", A, "+", B, "=", A+B)//