import re

def solution(new_id):
    #1
    id = new_id.lower()
    #2
    id = re.sub('[^a-z\d\-_.]', '', id)
    # if id.isalpha() or id.isdigit() or id in ['-', '_', '.']:
    #         answer += id
    #3
    while '..' in id:
        id = id.replace("..", ".")
    #4    
    id = id.strip('.')
    #5
    if id == '':
        id = 'a'
    #6
    if len(id) > 15:
        id = id[:15]
        id = id.strip('.')
    #7
    while len(id) < 3:
        id += id[-1:]
    return id

# other solution
# import re

# def solution(new_id):
#     st = new_id
#     st = st.lower()
#     st = re.sub('[^a-z0-9\-_.]', '', st)
#     st = re.sub('\.+', '.', st)
#     st = re.sub('^[.]|[.]$', '', st)
#     st = 'a' if len(st) == 0 else st[:15]
#     st = re.sub('^[.]|[.]$', '', st)
#     st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3-len(st))])
#     return st
