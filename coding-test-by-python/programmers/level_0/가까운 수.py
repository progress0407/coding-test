# fail
# def solution(array, n):
#     array.sort()
#     size = len(array)
#     small = array[0]
#     big = array[size - 1]
#     for x in array:
#         if n >= x:
#             small = x
#         if n <= x:
#             big = x
#     if abs(n - small) < abs(n - big):
#         return small
#     else:
#         return big

# fail
# def solution(array, n):
#     eg) distance : original_value
#     distance_dict = {abs(n - x): x for x in array}
#     distances = distance_dict.keys()
#     min_distance = min(distances)
#     min_val = distance_dict[min_distance]
#     if [distances].count(min_distance) == 1:
#         return min_val
#     else:
# 타깃 val: 27
# 거리 같은 25와 29라고 가정
#       return min_val - min_distance


def solution(array, n):
    displacement_to_distances = {n - x: abs(n - x) for x in array}
    distances = list(displacement_to_distances.values())
    min_distance = min(distances)

    if distances.count(min_distance) == 1:
        return get_distance(array, min_distance, n)
    else:
        return n - min_distance


def get_distance(array, min_distance, n):
    if array.count(n + min_distance) == 1:
        return n + min_distance
    else:
        return n - min_distance


# solution_result = solution([3, 10, 28], 20)  # expected 28
# solution_result = solution([10, 11, 12], 13) # expected 12
# solution_result = solution([3, 10, 10], 20) # 같은 수 여러 개 expected 10
# solution_result = solution([3, 25, 29], 27)  # 거리가 같은 수 여러 개 expected 25
# solution_result = solution([-5, -5, 3], -4)  # 거리가 같은 수 여러 개 expected 25
solution_result = solution([-5, -3, 3], -4)  # 거리가 같은 수 여러 개 expected 25
print(solution_result)
