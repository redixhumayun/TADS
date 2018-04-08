def checkSum(arr, value, index):
    #base case
    if value == 0:
        return True
    if index == 0 and value != 0:
        return False
    return (checkSum(arr, value, index - 1) or checkSum(arr, value - arr[index], index - 1))

def checkSumBottomUp(arr, value):
    table = [ [True for x in range(value + 1)] for y in range(len(arr) + 1) ]
    
    #setting the 0th column to all True
    #the value is 0
    for i in range(len(arr) + 1):
        table[i][0] = True

    #setting the 0th row to all False
    #cannot subtract from value if arr is empty
    for i in range(1, value + 1):
        table[0][i] = False
    
    for i in range(1, len(arr) + 1):
        for j in range(1, value + 1):
            if j < arr[i-1]:
                table[i][j] = table[i-1][j]
            else:
                table[i][j] = table[i-1][j] or table[i-1][j - arr[i-1]]
    
    #print table here
    # for i in range(len(arr) + 1):
    #     print(table[i], sep = " ")
    #     print("\n")

    printPaths(arr, len(arr) - 1, value, [], table)

def printPaths(arr, index, value, path, table):
    print(index, value, path)
    if index == 0 and value != 0 and table[index][value]:
        path.append(arr[index])
        print(path)
        return

    if index == 0 and sum == 0:
        print(path)
        return

    #path possible by ignoring current value
    if table[index - 1][value]:
        new_path = []
        printPaths(arr, index - 1, value, new_path, table)

    #path possible by accounting for current value 
    if value >= arr[index] and table[index-1][value - arr[index]]:
        path.append(arr[index])
        printPaths(arr, index - 1, value - arr[index], path, table)

if __name__ == "__main__":
    arr = [3, 34, 4, 12, 5, 2]
    value = 9
    # print(checkSum(arr, value, 4))
    checkSumBottomUp(arr, value)