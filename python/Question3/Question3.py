import sys

def find_min_days(prices, profit):
    # Participants code will be here

    out= "" 
    count1=0
    for i in profit:
        temp=[]
        count=0
        minus=sys.maxsize
        days = sys.maxsize 

        if (count1>0):
            out=out+","
        count1+=1
        for x in range(0,len(prices)):
            for y in range(x,len(prices)):
                # print(prices[y], '-', prices[x])
                count+=1
                if (prices[y]-prices[x]==i and y-x < days ):
                    
                    days=y-x
                    print(days)
                    temp.append(str(x+1)+" "+str(y+1))


                # elif (count == len(prices)):
                #     temp.append(str(-1))
                #     continue
        print(temp)       
        out = out + temp[-1]  
        # print(out)
        # out=out+str(temp[-1][0]) +" " + str(temp[-1][1])
       
    return out

n, d = map(int, input().split())
prices = list(map(int, input().split()))
profit = list()
d=2
# profit=[5,2]
# prices = [3,6,9,8,2,4]
# profit = [3,2]
# prices = [3,1,2,1,4,5]
for i in range(d):
    profit.append(int(input().strip()))
answer = find_min_days(prices,profit)
# Do not remove below line
print(answer)
# Do not print anything after this line