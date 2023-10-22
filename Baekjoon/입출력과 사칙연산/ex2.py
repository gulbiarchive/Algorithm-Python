# 사용자로부터 리스트의 크기 n 입력받기
n=int(input())

# num: 리스트에 들어갈 숫자를 나타내는 변수
# 문제에서 리스트는 1부터 시작하므로
# 1로 초기화
num=1

# 리스트의 행을 나타냄
for y in range(n):
    # 리스트의 열을 나타냄
    for x in range(n):
        # num을 end 키워드로
        # 공백 포함하여 한줄로 출력
        print(num, end=' ')
        # 그 다음 숫자를 위해 num 변수 1 증가
        num+=1
    # 다음 행 줄 바꿈
    print()
    
    
    