import sys
sys.stdin = open("input.txt",'r')

for t in range(1,int(input())+1):
    day,hour,minute = map(int,input().split())

    if day == 11 and hour < 11 and minute < 11:
        print(f"#{t} -1")
        continue
    
    start = (11 * 1440) + (11 * 60) + 11
    end = (day*1440) + (hour*60) + minute

    ans = end-start
    
    print(f"#{t} {ans}")