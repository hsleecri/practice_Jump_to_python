# 탭 문자를 공백 문자 4개로 바꾸기

"""
문서 파일을 읽어서 그 문서 파일 안에 있는 탭문자를 공백문자 4개로 바꾸는 스크립트
필요한 기능: 문서 파일 읽기, 문자열 변경하기
입력받는 값: 탭을 포함한 문서 파일
출력 값: 탭이 공벅으로 수정된 문서 파일

python tabto4.py src dst
python tabto4.py a.txt b.txt
src: 탭을 포함하는 원본 파일 이름
dst: 공백 4개로 변환하고 저장할 파일 이름
"""



import sys

src = sys.argv[1] # df
dst = sys.argv[2] # df

f = open(src)
tab_content = f.read()
f.close()

space_content =  tab_content.replace("\t", " "*4)

f = open(dst, 'w')
f.write(space_content)
f.close()

# f = open(original_name,'r')
