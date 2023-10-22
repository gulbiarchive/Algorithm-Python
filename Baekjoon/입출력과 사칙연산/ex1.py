# h: 세로 길이, w: 가로 길이
h, w = map(int, input().split())
# a,b=input().split()
# h=int(a)
# w=int(b)

m=[] # 빈 리스트 생성, 격자판 표현할 변수
# h(세로)길이만큼 반복
for i in range(1, h+1) :
    # 리스트 m에 빈 리스트 추가
    # 각 행을 나타냄
    m.append([]) 
    # w(가로) 길이만큼 반복
    for j in range(1, w+1) :
        # 각 행에 0을 추가하여 2차원 리스트의
        # 각 원소 0으로 초기화
        m[i].append(0)

# 막대의 개수 입력
n=int(input())

# 막대의 개수만큼 반복
for i in range(n) :
    # l: 각 막대의 길이
    # d: 방향
    # x, y: 시작 위치
    l,d,x,y = input().split()
    # 막대 길이만큼 반복
    for j in range(int(l)) :
        # 방향이 가로(0)인 경우
        if int(d)==0 :
            # 격자판의 해당 위치를 1로 설정하여
            # 막대가 놓인 위치를 표시
            m[int(x)][int(y)+j]=1
        # 방향이 세로(1)인 경우
        else :
            # 격자판의 해당 위치를 1로 설정하여
            # 막대가 놓인 위치 표시
            m[int(x)+j][int(y)]=1

# 격자판 출력 반복문
for i in range(1, h+1) :
    # 각 행에 대해 열에 대한 반복문
    for j in range(1, w+1) :
        # 격자판의 해당 위치 값을 출력하고,
        # 출력 후 줄 바꿈이 일어나지 않도록
        # end 키워드 사용
        print(m[i][j], end=' ')
    print() # 각 행 출력한 후 줄 바꿈 
    
    
    