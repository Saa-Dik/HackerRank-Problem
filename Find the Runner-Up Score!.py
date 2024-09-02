if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    array_1=set(arr)
    array_2=sorted(array_1)
    print(array_2[-2])
