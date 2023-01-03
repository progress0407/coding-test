print(list(range(5)))
print([range(5)])


# 문자열 찾기 함수
print(f"count, 있는 경우: {'1233'.count('3')}")  # 양의 정수
print(f"count, 없는 경우: {'1233'.count('4')}")  # 0

print(f"find, 있는 경우: {'1233'.find('3')}")  # 2
print(f"find, 있는 경우: {'1233'.find('4')}")  # -1

print(f"index, 있는 경우: {'1233'.index('3')}")  # 2
print(f"index, 있는 경우: {'1233'.index('4')}")  # 예외발생, ValueError, substring not found
