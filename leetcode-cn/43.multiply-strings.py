#
# @lc app=leetcode.cn id=43 lang=python3
# @lcpr version=30203
#
# [43] 字符串相乘
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if len(num1) < 2 or len(num2) < 2:
            return str(int(num1) * int(num2))
        else:
            n = max(len(num1), len(num2))
            m = n // 2
            a, b = divmod(int(num1), 10**m)
            c, d = divmod(int(num2), 10**m)
            ac = int(self.multiply(str(a), str(c)))
            bd = int(self.multiply(str(b), str(d)))
            ad_bc = int(self.multiply(str(a + b), str(c + d))) - int(ac) - int(bd)
            return str(ac * 10 ** (2 * m) + ad_bc * 10**m + bd)


# @lc code=end


#
# @lcpr case=start
# "2"\n"3"\n
# @lcpr case=end

# @lcpr case=start
# "123"\n"456"\n
# @lcpr case=end

#
