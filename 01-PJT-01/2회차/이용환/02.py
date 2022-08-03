with open('data\\fruits.txt', 'r', encoding='utf-8') as f:
    text = f.read()
    names = text.split('\n')
    names2 = list(set(names))
    cnt = 0
    qi = []
    for name in names2:
        if name.endswith('berry'):
            cnt += 1
            qi.append(name)
    result = '\n'.join(s for s in qi)
    with open('02.txt', 'w', encoding='utf-8') as q:
        q.write(str(cnt))
        q.write('\n' + result)

