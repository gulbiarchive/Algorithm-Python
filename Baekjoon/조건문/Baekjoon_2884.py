H, M = map(int, input().split())

# 분을 45분 기준으로 나누기
if M < 45:
    if H > 0:
        H -= 1
        M = 60 - (45 - M)
    else:
        H = 23
        M = 60 - (45 - M)
else:
    M -= 45

print(H, M)