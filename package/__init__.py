from .graphic.render import render_test

VERSION = 3.5

def print_version_info():
    print(f"The version of this game is {VERSION}")

# __init__.py 에서는 패키지 수준에서 변수와 함수를 정의할 수 있음

# 여기에 패키지 초기화 코드를 작성함
print("Initializing game ...")