import sys

sys.stdin = open("_소득불균형.txt")

T = int(input())
for i in range(1, T+1):
    person = int(input())
    score = list(map(int, input().split()))
    s_p = sum(score) / person
    result = []
    for j in score:
        if j <= s_p:
            result.append(j)
    print('#'+str(i), len(result))