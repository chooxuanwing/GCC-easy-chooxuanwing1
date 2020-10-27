import sys
# You may change this function parameters
def findMaxProfit(numOfPredictedDay, predictedSharePrices):
    # Participants code will be here
    print(numOfPredictedDay,predictedSharePrices)


    return 0


def main():
    line = input().split()
    numOfPredictedDay = 14 ##int(line[0])
    predictedSharePrices = [5,1,6,3,2,5,6,1,3,6,2,5,5,10] ##list(map(int, line[1:]))

    answer = findMaxProfit(numOfPredictedDay, predictedSharePrices)

    # Please do not remove the below line.
    print(answer)
    # Do not print anything after this line1

if __name__ == '__main__':
    main()
