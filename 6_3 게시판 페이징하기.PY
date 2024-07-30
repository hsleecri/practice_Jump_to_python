# 게시판 페이징하기

"""
A 씨는 게시판 프로그램을 작성하고 있다.
그런데 게시물의 총 개수와 한 페이지에 보여 줄 게시물 수를 입력으로 주었을 때
총 페이지 수를 출력하는 프로그램이 필요하다고 하다.

함수 이름 = total_page_num,
입력 값: 게시물의 총 개수, 한 페이지에 보여 줄 게시물 수 -> total_post, post_per_page
중간 과정: 그냥 나누면 되는 거 아냐?
출력 값: 총 페이지 수
결과는 어떤 형태로 저장? : 그냥 정수형 
"""

# 한번 해보자
def total_page_num(total_post, post_per_page):
    """
    (Attirbutes)
    total_post: int, 게시물의 총 개수
    post_per_page: int, 한 페이지당 게시물 수

    (Result)
    total_page_num: 총 페이지 수

    (Example)
    5, 10 = 1
    15, 10 = 2
    35, 10 = 3
    30, 10 = 3
    """
    if total_post % post_per_page == 0:
        return int(total_post / post_per_page)
    else:
        return int(total_post // post_per_page +1)

print(total_page_num(31,10))

# 굳 잘했당


