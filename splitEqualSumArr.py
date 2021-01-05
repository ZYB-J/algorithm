import math


def countPrimes(n):
    isPrim = []
    for k in range(n):
        isPrim.append(True)
    i = 2
    print('fdfd',math.sqrt(n))
    while i < math.sqrt(n):
        if isPrim[i]:
            j = i * 2
            print('tttt', i, j)
            while j < n:
                isPrim[j] = False
                #print('fffff',j)
                j = j + i
        i = i + 1
    count = 0
    i = 2
    while i < n:
        if isPrim[i]:
            count = count + 1
        i = i + 1
    return count


if __name__ == "__main__":
    print(countPrimes(100))
