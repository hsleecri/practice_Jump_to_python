from package.sound.echo import echo_test

def render_test():
    print("render")
    echo_test()

# def render_test():
#     print("render")

from ..sound.echo import echo_test # 상대 접근 ..는 부모

def render_test():
    print("render")
    echo_test()