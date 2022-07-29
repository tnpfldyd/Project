import sys

sys.stdin = open("_신용카드만들기1.txt")

T = int(input())
for i in range(1, T+1):
    card_number = list(map(int, input().split()))
    result = 0
    for j in range(len(card_number)):
        if j % 2 == 0:
            result += card_number[j] * 2
        if j % 2 == 1:
            result += card_number[j]
    if result % 10 != 0:
        result = 10 - result % 10
    else:
        result = 0
    print('#'+str(i), result)