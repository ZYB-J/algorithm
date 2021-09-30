class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxstart = 0
        maxend = 0
        length = len(s)
        if length<2:
            return s
        for r in range(2,length+1):
            for l in range(0,length):
                sub = s[l:r]
                start = 0
                end = r-l

                subLen  = end
                if subLen<0:
                    break
                #print(subLen)
                while end>start:
                    if sub[start] == sub[end-1]:
                        start = start+1
                        end = end -1
                    else:
                        break
                if end <= start:
                    print(subLen)
                    if subLen > (maxend - maxstart):
                        maxstart = l
                        maxend = r
        print(maxstart,maxend)
        return s[maxstart:maxend]
if __name__ == '__main__':
    s = "ababadabab"
    so = Solution()
    result = so.longestPalindrome(s)
    print(result)
