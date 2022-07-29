import sys

sys.stdin = open("_최빈수구하기.txt")

T = int(input())
for i in range(1, T+1):
    cnt = int(input())
    
    result = {}
    A = list(map(int, input().split()))
    for j in A:
        if j not in result:
            result[j] = 1
        else:
            result[j] += 1
    sort_result = sorted(result.items(), key = lambda x : (-x[1], -x[1]))
    print('#'+str(cnt), sort_result[0][0])