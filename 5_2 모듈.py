# from 모듈 import sub, add
# 모듈에서 sub와 add 함수를 가져오겠다는 뜻

from 모듈_1 import *
# 모듈에서 모든 함수(sub와 add 함수)를 가져오겠다는 뜻

# print(add(1,4))
# print(sub(4,2))

import 모듈_2

a = 모듈_2.Math()
print(a.solv(2)) # PI * (2**2)

# 1분 코딩
# 반지름이 5인 원의 넓이 계산

b = 모듈_2.Math()
print(b.solv(r=5))

# 다른 디렉터리에 있는 모듈 사용하기

