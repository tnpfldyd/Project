import sys

sys.stdin = open("_직사각형길이찾기.txt")

T = int(input())
for i in range(1, T+1):
    line = list(map(int, input().split()))
    line4 = (min(line) + max(line)) * 2
    x = line4 - sum(line)
    print('#'+str(i), x)