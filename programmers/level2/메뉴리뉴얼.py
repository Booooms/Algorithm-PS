from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    for i in course:
        arr = []
        for j in orders:
            combi = combinations(sorted(j), i)
            arr += combi
        counter = Counter(arr)

        if len(counter) != 0 and max(counter.values()) != 1:
            for k in counter:
                if counter[k] == max(counter.values()):
                    answer += [''.join(k)]
            # answer += [''.join(k) for k in counter if counter[k] == max(counter.values())]
    return sorted(answer)