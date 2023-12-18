## 자료형
# 정수형, 실수형, 복소수형, 문자열, 리스트, 튜플, 사전


## 지수 표현 방식
# e나 E 다음에 오는 수는 10의 지수부
# return 실수형
# 1e9 => 10 ** 9
n = 1e9
print(n)

a = 10 ** 9
print(n)


# 실수값은 10진수 체계에서 정확하지 않다 ex) 10 / 3 = 0.33333....
# 이진수로 계산하는 컴퓨터는 더욱 미세한 오차 존재
# 아래처럼 0.89999이기 때문에 False가 나온다.
b = 0.3 + 0.6
print(b)
print(True) if b == 0.9 else print(False)


# 따라서 round() 함수 사용 권장
# round(실수, 반올림하여 나오는 소수점 자리)
print(round(b, 4))
print(True) if round(b, 4) else print(False)


## 리스트 자료형
# 리스트 컴프리헨션
# 리스트 초기화 방식
# 2차원 리스트 n * n 초기화 방식
n = 5
m = 3
arr = [[0] * m for _ in range(n)]
arr[0][1] = 2
print(arr)

# 아래처럼 선언 시, 얕은 복사(주소값참조, 모두 같은 객체로 인식됨)
arr2 = [[0]*m] * n
arr2[0][1] = 3
print(arr2)

# 관련 메서드
arr3 = []
arr3.append("삽입할 값1") # O(1)
arr3.sort() # O(NlogN)
arr3.sort(reverse=True) # O(NlogN)
arr3.reverse() # O(N)
arr3.insert(1, "삽입할 값2") # O(N)
arr3.count("특정값") # O(N)
# arr3.remove("특정값") # O(N)


# 문자열 자료형
# 인덱싱, 슬라이싱 가능
a = "ABCDEF"
print(a[2:4])

# 특정 인덱스 값 변경 불가능(Immutable)
# a[0] = 'a'
# print(a)
# TypeError: 'str' object does not support item assignment


# 튜플 자료형
# () 소괄호 이용
# 리스트보다 공간 효율적(더 적은 메모리 사용)
a = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
print(a)
print(a[1:4])

# 한 번 선언된 값 변경 불가능(Immutable)
# a[1] = 1
# print(a)
# TypeError: 'tuple' object does not support item assignment

# 리스트보다 튜플 사용하는 경우
# 1. 서로 다른 성질의 데이터를 묶어서 관리할 때
#    최단 경로 알고리즘 -> (비용, 노드번호)의 형태로 자주 사용
# 2. 데이터의 나열을 해싱의 키 값으로 사용해야 할 때
#    튜플은 리스트와 달리 Immutable하기에 키 값으로 사용 가능
# 3. 리스트보다 메모리 효율적으로 사용해야할 때























