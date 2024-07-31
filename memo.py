# 간단한 메모장 만들기

"""
원하는 메모를 파일에 저장하고 추가 및 조회가 가능한 간단한 메모장 만들기

"""

import sys

option = sys.argv[1] # 프로그램 실행 옵션 #입력된 값을 읽어 들일 수 있는 라이브러리, sys.argv[0]은 파이썬 프로그램 이름 이므로 필요없음

if option == '-a':
    memo = sys.argv[2] # 메모 내용
    f = open('memo.txt', 'a') #'a'는 추가
    f.write(memo)
    f.write('\n')
    f.close()

if option == '-v':
    f = open('memo.txt')
    memo = f.read()
    f.close()
    print(memo)


