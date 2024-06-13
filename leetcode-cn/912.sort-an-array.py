#
# @lc app=leetcode.cn id=912 lang=python3
# @lcpr version=30203
#
# [912] 排序数组
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        else:
            n = len(nums)
            m = n // 2
            highArray = self.sortArray(nums[:m])
            lowArray = self.sortArray(nums[m:])
            res = []
            i, j = 0, 0
            while i < len(highArray) and j < len(lowArray):
                if highArray[i] < lowArray[j]:
                    res.append(highArray[i])
                    i += 1
                else:
                    res.append(lowArray[j])
                    j += 1
            if i == len(highArray):
                res.extend(lowArray[j:])
            else:
                res.extend(highArray[i:])
            return res


# @lc code=end


#
# @lcpr case=start
# [5,2,3,1]\n
# @lcpr case=end

# @lcpr case=start
# [5,1,1,2,0,0]\n
# @lcpr case=end

#
