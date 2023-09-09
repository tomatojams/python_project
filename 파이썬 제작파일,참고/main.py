workers = []
total_number = int(input())
for _ in range(total_number):
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
leafs = [i for i in leaves[: len(trees)]]  # 공정마다 말단
leaves[-1] = 0  # 마지막 공정은 반드시 해야하므로 bones에 속함
bones = [ai - bi for ai, bi in zip(trees, leaves)]  # 상사와 하사가있는 반드시 그 타이밍에 수행할 일
ma = max(bones)  # 리스트 컴프리헨션내에서 함수사용하지말것 시간지연
bones_to_filled = [(ma - i) for i in bones]  # bones 의 여유공간

leaves_temp = []
bones_unfilled = []
bank = 0
j: object
for i, j in zip(leaves, bones_to_filled):
    bank += i - j  # leaf의 여유분
    if bank < 0:  # j가 여유분 초과 값일때
        bones_unfilled.append(j - i)  # 못채운수만큼 기록
        leaves_temp.append(0)  # leaf 소모
        bank = 0  # 여유분 소모
    else:  # j가 여유분 이하
        leaves_temp.append(i - j)  # 남은거 기록
        bones_unfilled.append(0)


for reindex, j in enumerate(reversed(leaves_temp)):
    index = len(leaves_temp) - reindex - 1
    if j < 0:
        leaves_temp[index - 1] = leaves_temp[index - 1] + j
        leaves_temp[index] = 0
leaves = [i for i in leaves_temp]
bones_filled = [a - b for a, b in zip(bones_to_filled, bones_unfilled)]
bones_trans = [i + z for i, z in zip(bones, bones_filled)]

leaf = 0
if sum(leaves) != 0:
    leaves_priority = [sum(leaves[i:]) / (len(leaves) - i) for i in range(len(leaves))]
    a = max(leaves_priority)
    if a % 1 == 0:
        leaf = int(a // 1)
    else:
        leaf = int(a // 1 + 1)
print(len(bones))
print(len(workers) - (max(bones_trans) + leaf))
