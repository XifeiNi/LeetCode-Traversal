def memoize(f):
    cache = {}
    def memoizedFunction(*args):
        if args not in cache:
            cache[args] = f(*args)
        return cache[args]
    memoizedFunction.cache = cache
    return memoizedFunction

class Item:
    def __init__(self):
        self.numCoins = 0
        self.numPaths = 0
    def __str__(self):
        return "{}, {}".format(self.numCoins, self.numPaths)
     
def numWaysToChange(coins, targetValue):
    coins.sort()
    N = len(coins)
    cache = [[Item() for i in range(targetValue+1)]] * (N+1)
    
    totalPaths = 0
    for i in range(1, N+1):
        coinValue = coins[i-1]
        for subValue in range(1, targetValue+1):
            diff = subValue - coinValue
            if diff < 0 or (diff != 0 and cache[i][diff].numCoins == 0):
                
                # look at the cell above for a coin configuration for this value
                cache[i][subValue].numCoins = cache[i-1][subValue].numCoins
                if subValue == targetValue:
                    cache[i][subValue].numPaths = 0
                else:
                    cache[i][subValue].numPaths = cache[i-1][subValue].numPaths
            else:
                numCoins = cache[i][diff].numCoins + 1
                if cache[i-1][subValue].numCoins != 0:
                    numCoins = min(numCoins, cache[i-1][subValue].numCoins)
                cache[i][subValue].numCoins = numCoins
                
                if subValue == targetValue:
                    # just look at numPaths from diff, not above since we don't go that path
                    # (it's been seen previous iteration)
                    if diff == 0:
                        cache[i][subValue].numPaths = 1
                    else:
                        cache[i][subValue].numPaths = cache[i][diff].numPaths
                    
                elif cache[i][diff].numCoins == 0:
                    # start a new path with this coin
                    cache[i][subValue].numPaths = 1 + cache[i-1][subValue].numPaths
                else:
                    cache[i][subValue].numPaths = (cache[i][diff].numPaths + 
                                                   cache[i-1][subValue].numPaths)
            #print("cell:", i, ",", subValue, "numCoins:", cache[i][subValue].numCoins)
            #print("cell:", i, ",", subValue, "numPaths:", cache[i][subValue].numPaths)
        # sum up the numPaths for each row
        totalPaths += cache[i][targetValue].numPaths
    return totalPaths 
    
    
data=input().split()
targetValue = int(data[0])
coins=[]
for i in range(1, len(data)):
    coins.append(int(data[i]))
print(numWaysToChange(coins, targetValue))