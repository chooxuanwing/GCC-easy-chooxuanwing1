import sys
# You may change this function parameters

def findMaxProfit(numOfPredictedDay, predictedSharePrices):
    # Participants code will be here
    # print(numOfPredictedDay,predictedSharePrices)
    temp=0

    for i in range(0,len(predictedSharePrices)):
        for j in range(i,len(predictedSharePrices)):
            if (predictedSharePrices[j]-predictedSharePrices[i] > temp):
                temp=predictedSharePrices[j]-predictedSharePrices[i]
                print(temp)


    return temp


def main():
    line = input().split()
    numOfPredictedDay =  int(line[0])
    predictedSharePrices = list(map(int, line[1:]))
    print('hello')
    answer = findMaxProfit(numOfPredictedDay, predictedSharePrices)

    # Please do not remove the below line.
    print(answer)
    # Do not print anything after this line1

if __name__ == '__main__':
    main()
