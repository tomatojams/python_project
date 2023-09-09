workers = []
total_number = int(input())
for i in range(total_number):
    workers.append(int(input()))
trees = [0 for _ in range(len(workers))]
leafs = [0 for _ in range(len(workers))]

# trees, leafs, bones 가공
worker_level = 0
high_index = 0
high_data_limit = 0
repeat_data = 0  # 1일때 사장 한명 0일때 사장 여러명
for count, data in enumerate(workers):
    if data == -1:  # 1일때 사장 한명, -1일때 사장 여러명
        trees[worker_level] += 1
        leafs[worker_level] += 1
    elif data > 0 and data <= high_data_limit:
        trees[worker_level] += 1
        leafs[worker_level] += 1
        if data != repeat_data:
            leafs[worker_level - 1] -= 1
            repeat_data = data
    elif data > high_data_limit:
        worker_level += 1
        high_data_limit = count
        trees[worker_level] += 1
        leafs[worker_level] += 1
        leafs[worker_level - 1] -= 1
        repeat_data = data

trees = [i for i in trees if i != 0]  # 공정 전체 보여줌
leaves = [i for i in leaves[: len(trees)]]  # 공정마다 말단
leaves[-1] = 0  # 마지막 공정은 반드시 해야하므로 bones에 속함
bones = [ai - bi for ai, bi in zip(trees, leaves)]  # 상사와 하사가있는 반드시 그 타이밍에 수행할 일
ma = max(bones)  # 리스트 컴프리헨션내에서 함수사용하지말것 시간지연
bones_to_filled = [(ma - i) for i in bones]  # bones 의 여유공간

leaves_temp = []
bones_unfilled = []
bank = 0
for i, j in zip(leaves, bones_to_filled):
    bank += i - j  # leaf의 여유분
    if bank < 0:  # j가 여유분 초과 값일때
        bones_unfilled.append(j - i)  # 못채운수만큼 기록
        leaves_temp.append(0)  # leaf 소모
        bank = 0  # 여유분 소모
    else:  # j가 여유분 이하
        leaves_temp.append(i - j)  # 남은거 기록
        bones_unfilled.append(0)

for reindex, j in enumerate(
    reversed(leaves_temp)
):  # 데이타 변경하면서 반대순서로 중요, 슬라이싱하면 데이타 변경이 안됨
    index = len(leaves_temp) - reindex - 1
    if j < 0:
        leaves_temp[index - 1] = leaves_temp[index - 1] + j
        leaves_temp[index] = 0
leaves = [i for i in leaves_temp]
# leaves  1차 가공끝

# bones를 얼마나 채웠고 따라서  bones 변경
bones_filled = [a - b for a, b in zip(bones_to_filled, bones_unfilled)]
bones_trans = [i + z for i, z in zip(bones, bones_filled)]
leaf = 0

# 모든값 계산하기
for reindex3, data in enumerate(leaves[::-1]):
    index = len(leaves) - reindex3 - 1
    if data != 0 and leaves[index] > leaves[index + 1]:
        for fo_index2, min in enumerate(leaves[index + 1 :]):
            index2 = fo_index2 + index + 1
            # endpoints = index2
            if index2 == len(leaves) - 1:
                endpoints = index2
                break
            elif min >= sum(leaves[index:index2]) / len(leaves[index:index2]):
                endpoints = index2 - 1
                break
        local_sum = sum(leaves[index : endpoints + 1])
        local_wide = len(leaves[index : endpoints + 1])

        a = [local_sum // local_wide for i in range(local_wide)]
        b = local_sum % local_wide
        for i in range(1, b + 1):
            a[-i] = a[-i] + 1
        for i in range(0, local_wide):
            leaves[index + i] = a[i]
bones_trans = [i + j for i, j in zip(bones_trans, leaves)]
print(len(bones))
print(len(workers) - (max(bones_trans)))
