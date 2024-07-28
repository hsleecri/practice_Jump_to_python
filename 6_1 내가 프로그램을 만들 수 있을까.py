# 구구단 프로그램 만들기

"""
프로그램을 만들 때는 입력과 출력을 생각하기
예시: 함수 이름 = gugu,
입력 값: 2
출력 값: 2단
결과는 어떤 형태로 저장? : 연속된 자료 형태이므로 리스트
"""

# 한번 해보자

def gugu(num):
    result = []
    for i in range(1,10):
        result.append(num *i)
    return result

print(gugu(2))