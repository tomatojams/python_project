

def exam1(data,name,number):
    data.append((name,number))
    for step in range(len(data)):
        max_idx = step
        for i in range(step+1, len(data)):
            if data[i][1]> data[max_idx][1]:
                max_idx = i
        (data[step], data[max_idx]) = (data[max_idx], data[step])
    return data

def exam2(array):
    k=0
    for step in range(len(array)):
        min_idx = step

        for i in range(step+1, len(array)):
            if array[i] < array[min_idx]:
                min_idx = i
        if step != min_idx:
            (array[step], array[min_idx]) =(array[min_idx], array[step])
            k +=1
    return k

def exam3(mass):
    weight = [0, 6, 4, 3, 5]
    money =  [0, 13, 8, 6, 12]

    array = [[0 for _ in range(mass+1)]for _ in range(5)]
    for row in range(1, 5):
        for col in range(1, mass+1):
            if weight[row]> col:
                array[row][col] = array[row-1][col]
            else:
                value1 = money[row] + array[row-1][col-weight[row]]
                value2 = array[row-1][col]
                array[row][col] = max(value1, value2)
    return array[4][mass]

def exam4(n,k):
    number = [ str(i) for i in range(1,n+1)]
    current = k-1

    for i in range(n-1):
        if len(number) == 1:
            return number[0]

        number[current]= '0'
        for j in range(k):
            current = (current+1)%n
            while( number[current] =='0'):
                current = (current+1)%n

    for i in range(n):
        if number[i] !='0':
            return int(number[i])

def exam5(array,x):
    low = 0
    high = len(array)-1
    k = 0
    while low <= high:
        mid = low +(high-low+1)//2
        k +=1
        if array[mid] == x:
            return k
        elif array[mid] < x:
            low = mid+1
        elif array[mid]>x:
            high = mid -1
    return -1

def exam6(str1, str2):
#초기화
    dash = [[0 for _ in range(len(str1))] for _ in range(len(str2))]
    for i in range(len(str1)):
        dash[0][i] = i
    for j in range(len(str2)):
        dash[j][0] = j
#행렬계산
    for j in range(1, len(str2)):
        for i in range(1, len(str1)):
            maintain_replace = dash[j-1][i-1] + (0 if(str1[i-1] == str2[j-1]) else 1) #대각선 전의 값을참조
            insert = dash[j-1][i] +1 # 바로 위의 값을 참조해서 +1, 삽입이라서 현재 칼럼에 위치
            delete = dash[j][i-1] +1 # 왼쪽 값을 참조해서 +1, 삭제라서 다음칼럼 위치
            dash[j][i] =min(maintain_replace, insert, delete) # 네가지 변경점중 가장 최소의 값을 적어줌

    return dash[-1][-1] # 마지막값이 최소변경값