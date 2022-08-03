import sys

sys.stdin = open("_문자열의거울상.txt")

T = int(input())
for i in range(1, T+1):
    Text = input()
    result = ""
    for j in Text:
        if j == 'b':
            j = 'd'
            result += j
        elif j == 'd':
            j = 'b'
            result += j
        elif j == 'p':
            j = 'q'
            result += j
        elif j == 'q':
            j = 'p'
            result += j
    print('#'+str(i), result[::-1])
        