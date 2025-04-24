N = int(input())
for i in range(N):
    try:
        X, Y = map(int, input().split())
        print(X / Y)     
    except ZeroDivisionError:
        print("divisao impossivel")
