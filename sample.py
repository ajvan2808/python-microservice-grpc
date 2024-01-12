# def solution(p, q):
#     N = len(p)
#     distinst_char = set()
#
#     for i in range(N):
#         if p[i] == q[i]:
#             distinst_char.add(p[i])
#         distinst_char.add(p[i])
#         distinst_char.add(q[i])
#     return len(distinst_char)
#
# solution("abc", "bcd")
#

# def solution(A):
#     count_map = {}
#     for element in A:
#         if element in count_map:
#             count_map[element] += 1
#         else:
#             count_map[element] = 1
#
#     # Find the first element with a count of 1.
#     for i, element in enumerate(A):
#         if count_map[element] == 1:
#             return element
#
#     # No unique numbers found.
#     return -1


def solution(A):
    occurs_map = {items: A.count(items) for items in A}
    new_lst = []
    moves = 0
    for i, occurences in occurs_map.items():
        if i > 5:
            moves += occurences
        else:
            occurences_lst = [i] * i
            new_lst.extend(occurences_lst)

    for y in occurs_map.keys():
        if y <= 5:
            count = new_lst.count(y)
            original_count = occurs_map.get(y, 0)
            moves += abs(original_count - count)

    return moves


print(solution([1, 1, 1, 1, 3, 3, 4, 4, 4, 4]))

