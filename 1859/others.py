#import sys
#sys.stdin = open("input.txt", "r")
T = int(input())
 
for test_case in range(1, T+1):
    N = int(input())    
    values = list(map(int, input().split()))
 
    sum = 0
    max_values = 0
 
    for i in range(N - 1, -1, -1) :
        if values[i] < max_values : 
            sum += max_values - values[i]
        else :
            max_values = values[i]
     
         
    print(f"#{test_case} {sum}")