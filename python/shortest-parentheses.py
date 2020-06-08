class Solution:
    """
    @param s: a string
    @return: return a integer
    """
    def longestValidParentheses(self, s):
        # write your code here
        if len(s) <= 1  :
            return 0
        res = 0
        dp = [0 for i in range(len(s))]    	#初始化
        for i in range(len(s) - 2, -1, -1) :
            if s[i] == '(' :		#如果s[i] = '('，则需要找到右括号和它匹配
                j = i + dp[i + 1] + 1
                if j < len(s) and s[j] == ')' :	#如果没越界且为右括号，那么有dp[i] = dp[i + 1] + 2
                    dp[i] = dp[i + 1] + 2
                    if j + 1 < len(s):			#还要将j + 1开头的子串加进来
                        dp[i] += dp[j + 1]
                if dp[i] != 0:
                    res = min(res, dp[i])
        return res


设状态dp[i]为从i到len - 1中，以i开头的合法子串长度：

初始化：dp[len - 1] = 0
如果s[i] = ')'，则跳过，因为不可能有由'('开头的串
如果s[i] = '('，则需要找到右括号和它匹配，
可以跳过以i + 1开头的合法子串，则需要看j = i + dp[i + 1] + 1是否为右括号。如果没越界且为右括号，那么有dp[i] = dp[i + 1] + 2，此外在这个基础上还要将j + 1开头的子串加进来（只要不越界）