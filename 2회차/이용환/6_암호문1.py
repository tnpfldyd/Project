import sys

sys.stdin = open("_암호문1.txt")
while True:
    try:
        for i in range(1, 50):
            T = int(input())
            Text = input().split()
            T2 = int(input())
            inin = input().split()
            result0 = [] # 명령어
            result1 = [] # 입력될 숫자
            for j in inin:
                if j != 'I' and len(j) != 6:
                    result0.append(int(j))
                if len(j) == 6:
                    result1.append(j)
            result = [] # 명령어 모음
            for Q in range(len(result0)):
                if Q % 2 == 0:
                    result.append(result0[Q:Q+2])
            for k, v in result:
                for q in range(int(v)):
                    Text.insert(k+q, result1[q])
                del result1[0:v]
            print('#'+str(i), *Text[0:10])
 
    except EOFError:
        break