import re

def deserialize(s):
    li = []
    if re.match('^\d*$',s) != None:
        return int(s)
    temp = ''
    newLi = False
    cnt = 0
    for ch in s[1:-1]:
        if ch == '[':
            newLi = True
            temp += ch
            cnt += 1
        elif ch == ']':
            temp += ch
            cnt -= 1
            if cnt == 0:
                newLi = False
        elif ch.isnumeric():
            temp += ch
        elif ch == ',' and newLi:
            temp += ch
        elif ch == ',':
            li.append(deserialize(temp))
            temp = ''
        else:
            temp+=ch	
    if len(temp) > 0:
        li.append(deserialize(temp))
    return li

print(deserialize('[123,[456,[789]]]'))
print(deserialize('[[456,[789]],123]'))