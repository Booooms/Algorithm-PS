import itertools as it
def is_prime(n):
    if n in [0,1]:
        return False
    
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def solution(numbers):
    answer = []
    nums = list(numbers)
    tmp = []
    
    for i in range(1, len(nums)+1):
        tmp += (list(it.permutations(nums, i)))
    hap = [int(''.join(t)) for t in tmp]

    for j in hap:
        if is_prime(j):
            answer.append(j)

    return len(set(answer))