with open('data\\fruits.txt', 'r', encoding='utf-8') as f:
    cnt = 0
    for i in f:
        cnt += 1
    with open('01.txt', 'w', encoding='utf-8') as q:
        q.write(str(cnt))