import sys

read = sys.stdin.readline

T = int(read())

for i in range(T):
    a,b = map(int,read().split())
    print(f"Case #{i+1}: {a+b}")
