"""
一条包含字母 A-Z 的消息通过以下方式进行了编码：

'A' -> 1
'B' -> 2
...
'Z' -> 26
给定一个只包含数字的非空字符串，请计算解码方法的总数

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/decode-ways
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution:
    def numDecodings(self, s: str) -> int:
        #动态规划：时间复杂度O(n),空间复杂度O(n)
        # 类似于爬楼梯，不过存在一些异常情况，f(n) = f(n-1)+f(n-2)
        size = len(s)
        #特判
        if size == 0:
            return 0
        dp = [0]*(size+1)
        dp[0] = 1
        for i in range(1,size+1):
            t = int(s[i-1])
            if t>=1 and t<=9:
                dp[i] += dp[i-1] #最后一个数字解密成一个字母
            if i >=2:#下面这种情况至少要有两个字符
                t = int(s[i-2])*10 + int(s[i-1])
                if t>=10 and t<=26:
                    dp[i] += dp[i-2]#最后两个数字解密成一个一个字母
        return dp[-1]
        # 这里只考虑适合的情况