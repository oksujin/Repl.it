# 리스트 컴프리헨션 : 리스트 내부에 코드를 작성하는 방법
# 1. 0부터 19까지 수 중, 홀수만 포함하기
a = [i for i in range(20) if i % 2 == 1]
print (a)

# 2. 1부터 9까지의 수의 제곱 값을 포함하는 리스트
b = [i*i for i in range (1, 9)]
print(b)

# 3. N*M 크기의 2차원 리스트 초기화하기
N = 3
M = 4
array = [[0] * M for _ in range(N)]
print(array)