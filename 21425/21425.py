'''
아래의 구문은 input.txt 를 read only 형식으로 연 후,
앞으로 표준 입력(키보드) 대신 input.txt 파일로부터 읽어오겠다는 의미의 코드입니다.
여러분이 작성한 코드를 테스트 할 때, 편의를 위해서 input.txt에 입력을 저장한 후,
아래 구문을 이용하면 이후 입력을 수행할 때 표준 입력 대신 파일로부터 입력을 받아올 수 있습니다.
따라서 테스트를 수행할 때에는 아래 주석을 지우고 이 구문을 사용하셔도 좋습니다.
아래 구문을 사용하기 위해서는 import sys가 필요합니다.
단, 채점을 위해 코드를 제출하실 때에는 반드시 아래 구문을 지우거나 주석 처리 하셔야 합니다.
'''


import sys
sys.stdin = open("input.txt", "r")
result = []

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for _ in range(1, T + 1):
    A, B, N = map(int, input().split())
    count = 0
    while(A <= N and B <= N):
        if(A < B):
            A += B
        else:
            B += A
        count += 1
    result.append(count)

for _ in range(len(result)):
    print(result[_])
