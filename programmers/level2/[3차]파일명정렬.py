def solution(files):
    answer = []
    for f in files:
        head, number, tail = '', '', ''

        number_check = False
        for i in range(len(f)):
            if f[i].isdigit(): 
                number += f[i]
                number_check = True
            elif not number_check: 
                head += f[i]
            else:             
                tail = f[i:]
                break
        answer.append((head, number, tail))  

    answer.sort(key=lambda x: (x[0].upper(), int(x[1]))) 

    return [''.join(t) for t in answer]

# other solution_1
# import re

# def solution(files):
#     a = sorted(files, key=lambda file : int(re.findall('\d{1,5}', file)[0]))
#     b = sorted(a, key=lambda file : re.split('\d{1,5}', file.lower())[0])
#     return b

# other solution_2
# import re

# def solution(files):

#     def key_function(fn):
#         head,number,tail = re.match(r'([a-z-. ]+)(\d{,5})(.*)',fn).groups()
#         return [head,int(number)]

#     return sorted(files, key = lambda x: key_function(x.lower()))