s = input()
result = []
value = 0

for i in s:
    # 알파벳인경우
    if i.isalpha():
        result.append(i)
    else:
        value += int(i)

result.sort()

if value != 0:
    result.append(str(value))

print(''.join(result))