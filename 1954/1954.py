import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T+1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]
    state = "right"
    i = 0
    j = 0
    count = 0
    while count < N*N:      
        if count == N*N-1:
            count += 1
            arr[i][j] = count
        elif state == "right":
            if j < N-1 and arr[i][j+1] == 0:
                count += 1
                arr[i][j] = count
                j += 1
            elif j == N-1 or arr[i][j+1] != 0:
                state = "down"
        elif state == "down":
            if i < N-1 and arr[i+1][j] == 0:
                count += 1
                arr[i][j] = count
                i += 1
            elif i == N-1 or arr[i+1][j] != 0:
                state = "left"
        elif state == "left":
            if j > 0 and arr[i][j-1] == 0:
                count += 1
                arr[i][j] = count
                j -= 1
            elif j == 0 or arr[i][j-1] != 0:
                state = "up"
        elif state == "up":
            if i > 0 and arr[i-1][j] == 0:
                count += 1
                arr[i][j] = count
                i -= 1
            elif i == 0 or arr[i-1][j] != 0:    
                state = "right"
        if count == N*N:
            print(f"#{test_case}")
            for row in arr:
                print(*row)
            break





    
