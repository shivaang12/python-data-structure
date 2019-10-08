import math

def construct_sparse_table(arr):
    n = len(arr)
    sparse_table = [[-1 for i in range(n)] 
                     for j in range(int(math.log(n, 2))+1)]
    for j in range(int(math.log(n, 2))+1):
        for i in range(n):
            min_index = i
            if(i+(2**j)-1 < n):
                for x in range(i, i+(2**j)-1):
                    if(given_array[x] < given_array[min_index]):
                        min_index = x
                sparse_table[j][i] = min_index
    return sparse_table

def query(arr, sparse_table, query_range):
    length_of_array = len(arr)
    min_elements = []
    while length_of_array > 0:
        k = int(math.log(len(arr), 2))
        min_elements.append(arr[sparse_table[k][query_range[0]]])
        length_of_array = length_of_array - (2**k)
    return min(min_elements)

if __name__ == '__main__':
    given_array = [4, 6, 1, 5, 7, 3]

    sparse_table = construct_sparse_table(given_array)
    query_list = [[3, 5], [0, 5], [0, 3]]

    for x in query_list:
        print(query(given_array, sparse_table, x))
    
        
