import re
def file_open():
    with open ('corpus.txt', 'r', encoding='utf-8') as corpus:
        words=corpus.readlines()
    return words
def f1(lines):
    lines_num=int()
    for line in lines:
        lines_num+=1
    with open ('lines_number.txt', 'a', encoding='utf-8') as firstdoc:
        firstdoc.write(str(lines_num))
    return 'The answer is in the document.'


def go():
    return f1(file_open())

go()

with open ('corpus.txt', 'r', encoding = 'utf-8') as f:
    morph = f.read()
    arr = re.findall(r'(<w lemma=".*?" type="(.*?)">.*?</w>)', morph)
    d = {}
    for i in arr:
        d[i[1]] = morph.count(i[1])
with open ('dict.txt', 'w', encoding = 'utf-8') as f:
    for key in d:
        a = str(key) + ' ' + '\n'
        f.write(a)
        
