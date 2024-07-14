def add(a,b):
    return a+b

def sub(a,b):
    return a-b

# print(add(1,4))
# print(sub(4,2))

# 이렇게 만들면 import 할때 여기 프린트함수까지 바로 가져와져 결과값을 출력함

# 그래서 이렇게 만들어 줘야 함

if __name__ == "__main__":
    print(add(1,4))
    print(sub(4,2))