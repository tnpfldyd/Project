import sys

sys.stdin = open("_신용카드만들기2.txt")

T = int(input())
for i in range(1, T+1):
    card_number = input()
    result = []
    for j in card_number:
        if j != '-':
            result.append(j)
    if result[0] in '34569' and len(result) == 16:
        print('#'+str(i), 1)
    else:
        print('#'+str(i), 0)