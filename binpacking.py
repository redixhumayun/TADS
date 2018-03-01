def findNumberOfBins(weights):
    numOfBins = 1
    bin_remainder = 1
    for weight in weights:
        if(weight > bin_remainder):
            numOfBins += 1
            bin_remainder = 1 - weight
        else:
            bin_remainder -= weight
    return numOfBins

if __name__ == "__main__":
    weights = [0.25, 0.5, 0.75, 0.25, 1]
    result = findNumberOfBins(weights)
    print(result)