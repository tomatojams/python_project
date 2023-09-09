
workers = []
total_number = int(input())
for i in range(total_number):
    workers.append(int(input()))
print(workers)
#workers = [-1, 1, 1, 1, 1, 1, 2, 4, 5, 7, 7, 7, 8, 8, 11, 15, 15] #17명 6,13 정답7
#workers = [-1, 1, 1, 2, 2, 3, 3]
#workers = [-1, 1, 1, 1, 1, 2, 4, 4, 7, 7, 7, 8, 8, 11, 14, 14] #16명 6, 13 정답
trees = [0 for _ in range(len(workers))]
leaves = [0 for _ in range(len(workers))]

worker_level = 0
high_index = 0
high_data_limit =1
repeat_data = 0
# trees, leaves, bones 가공
for count,data in enumerate(workers):
    if data == 1:
        trees[worker_level] +=1
        leaves[worker_level] +=1
    elif data >0 and data <= high_data_limit:
        trees[worker_level] += 1
        leaves[worker_level] += 1
        if data != repeat_data:
            leaves[worker_level- 1] -=1
            repeat_data = data
    elif data > high_data_limit:
        worker_level +=1
        high_data_limit = count
        trees[worker_level] +=1
        leaves[worker_level] +=1
        leaves[worker_level-1] -=1
        repeat_data = data

trees = [i for i in trees if i != 0]
leaves = [i for i in leaves[:len(trees)]]
leaves[-1] =0
bones = [ ai - bi for ai, bi in zip(trees,leaves)]
bones_property = [(max(bones) - i) for i in bones] # bones 의 여유공간
offset_bones_property = bones_property.copy()

print("trees:",trees)
print("leaf first :",leaves)
print("bones:",bones)
print("bones_property :",bones_property)

# leaves  가공 1번째 bones 속성값을 바탕으로 변경
# leaves의 총값이 0가 될때까지 하고 멈추고 bones_property가 일부 살아남는 경우가 있는지
# 검토해볼것
leaves_temp = []
bones_property_temp =[]
bank = 0
for i, j in zip(leaves,bones_property):
    bank += (i-j)
    if bank <0:
        bones_property_temp.append(j)
        leaves_temp.append(0)
        bank = 0
    else:
        leaves_temp.append(i-j)
        bones_property_temp.append(0)

for reindex, j in enumerate(reversed(leaves_temp)): #데이타 변경하면서 반대순서로 중요, 슬라이싱하면 데이타 변경이 안됨
    index = len(leaves_temp)-reindex -1
    if j < 0:
        leaves_temp[index-1] = leaves_temp[index-1] + j
        leaves_temp[index] = 0
leaves =[i for i in leaves_temp]
# leaves  1차 가공끝

offset_bones_property = [a - b for a, b in zip(offset_bones_property, bones_property)]
print("leaf second  :",leaves)
#print("bones_property :",bones_property)
#print("offset:",offset_bones_property)

#실험값 - 지워야 함
#leaves = [100, 1, 3, 3, 4]
#leaves =[2,11, 0, 0, 0, 0, 0, 1, 11, 0]
# [2, 11, 0, 0, 0, 0, 0, 1, 5, 5]
# [1,  1, 2, 2, 2, 2, 2, 2, 5, 5]
# 평탄화 자체가 아니라 평탄화해서 마지막값의 max값을 찾는다 한번만 계산
# 따라서 값은 5


#우선순위에서 하나의 계산포인트 구함
leaves_priority = [ sum(leaves[i:])/(len(leaves)-i) for i in range(len(leaves))]
#print("leaves_priority",leaves_priority)
cal_max = leaves_priority.index(max(leaves_priority))
#print("index of max calculation",cal_max)
local_sum = sum(leaves[cal_max:])
local_wide = len(leaves[cal_max:])

a = local_sum// local_wide
b = local_sum%local_wide
if b == 0:
    leaf = a
else:
    leaf = a+1
print(leaves)
print("a:",a)
print("leaf:",leaf)

offset_bones_property =[i+j for i, j in zip(offset_bones_property, bones_property)]
trees_trans = [i+z for i, z in zip(bones,offset_bones_property)]
print(len(bones)+1)
print(len(workers)-(max(trees_trans)+leaf))
