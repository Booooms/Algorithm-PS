def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda numbers : numbers*3, reverse=True)
    return str(int(''.join(numbers)))