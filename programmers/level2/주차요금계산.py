# 프로그래머스 LV2 주차 요금 계산
import math

def changeToMinute(first, second):
    h1, m1 = map(int, first.split(':'))
    h2, m2 = map(int, second.split(':'))
    total1, total2 = h1 * 60 + m1, h2 * 60 + m2

    return total2 - total1

def solution(fees, records):
    dt, df, ut, uf = fees
    check = {}
    check_time = {}
    
    # in-out 둘다 있는 차량 주차시간 구하기
    for record in records:
        when, car, inout = record.split()
        if inout == "IN":
            check[car] = when
        else:
            if car not in check_time:
                check_time[car] = changeToMinute(check[car], when)
            else:
                check_time[car] += changeToMinute(check[car], when)
            check[car] = "0"
            
    # 23:59에 출차된 것으로 간주할 때 주차시간 구하기
    for key, value in check.items():
        if value != "0":
            if key in check_time:
                check_time[key] += changeToMinute(value, "23:59")
            else:
                check_time[key] = changeToMinute(value, "23:59")  # 테스트3번에서 check_time에 아예 아무것도 안들어가있을 수도 있음

    check_time = sorted(check_time.items())

    answer = []
    for car, total_time in check_time:
        if total_time <= dt:
            answer.append(df)
        else:
            answer.append(df + math.ceil((total_time - dt) / ut) * uf)

    return answer