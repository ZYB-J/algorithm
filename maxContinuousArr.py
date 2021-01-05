from typing import List


def getMaxArr(arr):
    leng = len(arr)
    maxValue = 0
    preValue = 0
    x = 0;
    y = 0;
    for k in range(leng):
        preValue = 0
        for i in range(k, leng):
            preValue = arr[i] + preValue
            if (maxValue < preValue):
                x = k
                y = i
                maxValue = preValue
        print(maxValue)
    print(x, y)


def romanToInt(s):
    a = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    ans = 0
    for i in range(len(s)):
        if i < len(s) - 1 and a[s[i]] < a[s[i + 1]]:
            ans -= a[s[i]]
        else:
            ans += a[s[i]]
        print(ans)
    print(ans)


def twoSum(nums: List[int], target: int) -> List[int]:
    hashmap = {}
    for index, num in enumerate(nums):
        if num >= target:
            continue
        a = target - num
        print(a)
        if a in hashmap:
            return [hashmap[a], index]
        hashmap[num] = index
    return None


def lengthOfLongestSubstring( s: str) -> int:
    ast={}
    max =0
    for index, num in enumerate(s):
        if num in ast:
            i = ast[num]
            if index-i+1>max:
                ast[num]=index
            else:
                max = max+1
    return max
if __name__ == '__main__':
    arr = [1, -2, 3, -4, 2, 1, -2, 9]
    # getMaxArr(arr)
    # romanToInt("VIVIX")
    #print(twoSum(arr, 5))
    print(max)
