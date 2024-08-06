


"""
필요한 기능: 파이썬 파일만 찾아서 출력하기 (*.py)
입력값: 검색 시작할 디렉터리
출력값: 파이썬 파일명
"""

# python sub_dir_search.py

import os

def search(dirname):
    try:
        filenames = os.listdir(dirname)
        for filename in filenames:
            full_filename = os.path.join(dirname, filename)
            if os.path.isdir(full_filename):
                search(full_filename)
            else:
                ext = os.path.splitext(full_filename)[-1]
                if ext == '.py':
                    print(full_filename)
    except PermissionError:
        pass

search("C:")

import os

for (path, dir, files) in os.walk("C:/"):
    for filename in files:
        ext = os.path.splitext(filename)[-1]
        if ext == '.py':
            print("%s/%s"% (path, filename))