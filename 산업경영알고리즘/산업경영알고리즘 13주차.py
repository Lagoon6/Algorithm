from abc import abstractproperty


def knapsak(maxWeight, rowCount, weight, money, item):
    print('##메모리제이션 배열##')
    array = [[ 0 for _ in range(maxWeight+1)] for _ in range(rowCount +1)]
    item_array = [[''for _ in range(maxWeight +1)] for _ in range(rowCount +1 )]
    
    for row in range(1,rowCount+1):
        print(row, '개-->', end ='')
        for col in range(1, maxWeight+1):
            if weight[row]> col:
                array[row][col] = array[row-1][col]
                item_array[row][col] = item_array[row-1][col]
            else:
                value1 = money[row] + array[row-1][col-weight[row]]
                item_value1 = item[row] + "" + item_array[row-1][col-weight[row]]
                value2 = array[row-1][col]
                item_value2 = item_array[row-1][col]
                if value1 > value2:
                    array[row][col] = value1
                    item_array[row][col] = item_value1
                
                else:
                    array[row][col] = value2
                    item_array[row][col] = item_value2
        
            print('%6d'%array[row][col], end = '')
            print(': %6s'%item_array[row][col],end='')
    
        print()
    return array[rowCount][maxWeight]

maxWeight = 7
rowCount = 4
weight = [0, 6, 4, 3, 5]
money = [0, 13, 8, 6, 12]  
item = [" ", "금괴", "수정", "루비", "진주"]   

knapsak(maxWeight, rowCount, weight, money, item)