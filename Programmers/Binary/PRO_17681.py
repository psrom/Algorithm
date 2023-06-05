def solution(n, arr1, arr2):
    binary_arr1 = []
    binary_arr2 = []
    for a in arr1:
        map_element = str(bin(a)[2:])
        if len(map_element) != n:
            map_element = '0' * (n - len(map_element)) + map_element
        binary_arr1.append(map_element)
        
    for a in arr2:
        map_element = str(bin(a)[2:])
        if len(map_element) != n:
            map_element = '0' * (n - len(map_element)) + map_element
        binary_arr2.append(map_element)
    
    result_map = ['' for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            if binary_arr1[i][j] == binary_arr2[i][j] == '0':
                result_map[i] += ' '
            else:
                result_map[i] += '#'
        
    return result_map

# ===================================================================
# 함수를 이용하면 훨씬 간단하게 풀 수 있다.
def solution2(n, arr1, arr2):
    answer=[]
    for i in range(0,n):
        tem = bin(arr1[i]|arr2[i])[2:].zfill(n)
        tem = tem.replace('1','#')
        tem = tem.replace('0',' ')
        answer.append(tem)
    return answer