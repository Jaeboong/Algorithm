#import random
#import sys
#sys.stdin = open("input.txt", "r")

T = int(input())


for test_case in range(1, T + 1):
    testcase = int(input())
    score = list(map(int, input().split()))
    #score = [random.randint(1,100) for _ in range (1000)]
    arr = [0]*101
    for s in score:
        arr[s] += 1
    maxes = [i for i in range(len(arr)) if arr[i] == max(arr)]
    print(f"#{test_case}",max(maxes))
