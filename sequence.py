def checkSum(arr, value, index):
    #base case
    if value == 0:
        return True
    if index == 0 and value != 0:
        return False
    return (checkSum(arr, value, index - 1) or checkSum(arr, value - arr[index], index - 1))

if __name__ == "__main__":
    arr = [3, 4, 9, 10, 13]
    value = 22
    print(checkSum(arr, value, 4))