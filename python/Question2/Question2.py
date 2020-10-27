# import sys
# You may change this function parameters
def findMaxProfit(numOfPredictedTimes, predictedSharePrices):
    # Participants code will be here
    temp=0

    for i in range(0,numOfPredictedTimes-1):
        if (predictedSharePrices[i+1]-predictedSharePrices[i] > 0):
            temp+=predictedSharePrices[i+1]-predictedSharePrices[i]
            print(temp)


    return temp

def main():
    # line = input().split()
    numOfPredictedTimes = int(line[0])
    predictedSharePrices = list(map(int, line[1:]))

    answer = findMaxProfit(numOfPredictedTimes, predictedSharePrices)
    # Do not remove below line
    print(answer)
    # Do not print anything after this line

if __name__ == '__main__':
    main()