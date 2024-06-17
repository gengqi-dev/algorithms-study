#
# @lc app=leetcode.cn id=231 lang=python3
# @lcpr version=30203
#
# [231] 2 的幂
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        counter = 0
        while n > 0:
            if n & 1 == 1:
                counter += 1
            n = n >> 1
        if counter == 1:
            return True
        else:
            return False


# @lc code=end


#
# @lcpr case=start
# 1\n
# @lcpr case=end

# @lcpr case=start
# 16\n
# @lcpr case=end

# @lcpr case=start
# 3\n
# @lcpr case=end

#
