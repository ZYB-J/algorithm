"""
寻找最长回文子串
"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxstart = 0
        maxend = 0
        max_len = 0
        length = len(s)
        if length<2:
            return s
        dp = [[False] * length for _ in range(length)]
        for i in range(0,length):
            dp[i][i] = True

        #串的长度
        for l in range(2,length+1):
            for i in range(length):
                j = l+i-1 #串的右边界
                if j>=length:
                    break
                if s[i] != s[j]:
                    dp[i][j] = False
                else:
                    if j-i<3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i+1][j-1]
                if dp[i][j] and j-i+1>max_len:
                    max_len = j-i+1
                    maxstart = i
        return s[maxstart:maxstart+max_len]
if __name__ == '__main__':
    s = "ababadabab"
    so = Solution()
    result = so.longestPalindrome(s)
    print(result)

