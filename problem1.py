import random
import argparse
import sys

HEAD = 1
TAIL = 2

def flipOneCoinManyTimes(rng, numberOfFlips):
    heads = 0
    for i in range(0, numberOfFlips):
        toss = rng.randrange(HEAD, TAIL+1)
        heads += 1 if (toss == HEAD) else 0
    return heads


def flipManyCoinsManyTimes(rng, numberOfFlips, numberOfCoins):
    cRand = rng.randrange(0, numberOfCoins)
    headsMin = numberOfCoins
    for i in range(0, numberOfCoins):
        heads = flipOneCoinManyTimes(rng, numberOfFlips)
        if (i == 0):
            headsOne = heads
        if (i == cRand):
            headsRand = heads
        if (heads < headsMin):
            headsMin = heads
    return (headsOne, headsRand, headsMin)


def performExperiment(rng, numberOfFlips, numberOfCoins, numberOfTimes):
    totalHeadsOne, totalHeadsRand, totalHeadsMin = 0,0,0
    for i in range(0, numberOfTimes):
        if (((i+1) % 10) == 0):
            sys.stdout.write('.')
            sys.stdout.flush()
            if (((i+1) % 1000) == 0):
                print(i+1)
                sys.stdout.flush()

        headsOne, headsRand, headsMin = flipManyCoinsManyTimes(rng, numberOfFlips, numberOfCoins)
        totalHeadsOne += headsOne
        totalHeadsRand += headsRand
        totalHeadsMin += headsMin

    totalFlipsPerCoin = float(numberOfFlips * numberOfTimes)
    vOne = float(totalHeadsOne) / totalFlipsPerCoin
    vRand = float(totalHeadsRand) / totalFlipsPerCoin
    vMin = float(totalHeadsMin) / totalFlipsPerCoin

    return (vOne, vRand, vMin)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--flips", "-f", help="number of flips", default=10, type=int)
    parser.add_argument("--coins", "-c", help="number of coins", default=1000, type=int)
    parser.add_argument("--times", "-t", help="number of times", default=100000, type=int)
    parser.add_argument("--seed",  "-s", help="seed for random number generator", default=None) # not reproducable
    args = parser.parse_args()
    rng = random.Random()
    rng.seed(args.seed)

    print('{coins} coins flipped {flips} times, repeated {times} times.'
          .format(coins=args.coins, flips=args.flips, times = args.times))

    vOne, vRand, vMin = performExperiment(rng, args.flips, args.coins, args.times)

    print('\n vOne  = {vOne}\n vRand = {vRand}\n vMin  = {vMin}'
          .format(vOne=vOne, vRand=vRand, vMin=vMin))


if __name__ == "__main__":
    main()
