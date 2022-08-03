with open('data\\fruits.txt', 'r', encoding='utf-8') as f:
    text = f.read()
    names = text.split()
    tcid = {}
    for q in names:
        if q not in tcid:
            tcid[q] = 1
        else:
            tcid[q] += 1
    #for a, b in tcid.items():
    with open('03.txt', 'w', encoding='utf-8') as qq:
        for a, b in tcid.items():
            qq.write(a), qq.write(' '), qq.write(f'{b}\n')
            
