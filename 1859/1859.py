import sys
sys.stdin = open("input.txt", "r")

T = int(input())
profit = [0] * (T+1)  # 충분한 크기로 초기화

for i in range(1, T + 1):
    N = int(input())
    price = list(map(int, input().split()))
    head = 0
    profit[i] = 0
    tail = price.index(max(price))
    while head < N:
        for head in range(head, tail):
            profit[i] += price[tail] - price[head]
        head = tail + 1
        if head < N:  # 남은 가격이 있는지 확인
            tail = head + price[head:].index(max(price[head:]))
        else:
            break

for i in range(1, T + 1):
    print(f"#{i} {profit[i]}")




