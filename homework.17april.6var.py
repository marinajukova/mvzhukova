import os
num = 0
for roots, dirs, files in os.walk('.'):
    exp = []
    for f in files:
        name = f[::-1].split('.')[0]
        if name not in exp:
            exp.append(name)
        else:
            num += 1
            break
print(num)
