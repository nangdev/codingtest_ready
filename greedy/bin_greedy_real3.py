N = int(input())
for i in range(N):
    S = input()
    arr = list(map(int,S))
    result = 0
    if arr.count(0) > arr.count(1):
        lis = S.split('0')
        lis2 = ' '.join(lis).split()
        result = len(lis2)
    else:
        lis = S.split('1')
        lis2 = ' '.join().split()
        result = len(lis2)
    
    print(result)
