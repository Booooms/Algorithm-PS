def solution(record):
    answer = []
    dic = {}

    for sp in record:
        sp_record = sp.split()
        if len(sp_record) == 3:
            dic[sp_record[1]] = sp_record[2]

    for sp in record:
        sp_record = sp.split()
        if sp_record[0] == 'Enter':
            answer.append('{}님이 들어왔습니다.' .format(dic[sp_record[1]]))
        elif sp_record[0] == 'Leave':
            answer.append('{}님이 나갔습니다.' .format(dic[sp_record[1]]))
    return answer