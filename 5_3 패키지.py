# 간단한 파이썬 프로그램이 아니라면 패키지 구조로 만드는 게 좋음

# import package.sound.echo
# package.sound.echo.echo_test()

# from package.sound import echo
# echo.echo_test()

# from package.sound.echo import echo_test
# echo_test()

# import package
# package.sound.echo.echo_test()


"""
__init__.py의 존재이유:
1. 이게 각 디렉터리에 없으면 패키지로 인식되지 않음
2. 패키지와 관련된 설정이나 초기화 코드를 포함할 수 있음
"""

from package.sound import *
echo.echo_test() # 이렇게 했는데 정의되지 않았다는 오류가 뜸.
# 이를 방지하기 위해서 import *로 할때는 __init__.py 파일에 __all__ 변수를 설정하고 import 할 수 있는 모듈을 정의해줘야함


from package.graphic.render import render_test #이렇게 해도 되지만
render_test()

