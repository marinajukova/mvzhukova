import re
with open ('corpus.txt', 'r', encoding = 'utf-8') as f:
    adject = f.read()
    arr = re.findall(r'<w lemma=".*?" type="(l.f.*?)">.*?</w>',adject)   
    d = {}
    for i in arr:
        print(i)
        d[i] = adject.count(i)
with open ('adj.txt', 'w', encoding = 'utf-8') as f:
    for key in d:
        b =  str(key) + ' ' + str(d[key]) + '\n'
        f.write(b)
