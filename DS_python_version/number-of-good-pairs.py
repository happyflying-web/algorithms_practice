# https://leetcode-cn.com/problems/number-of-good-pairs/

class Solution:
    # def numIdenticalPairs(self, nums: List[int]) -> int:
    def numIdenticalPairs(self, nums) -> int:
        temp_1 = []
        result = 0
        for i in range(0, 101):
            temp_1.append(0)
        for i in nums:
            temp_1[i] = temp_1[i] + 1
        for i in temp_1:
            if i > 1:
                x = i
                fun = x * (x - 1) / 2  # 统计学方法
                result = result + fun

        return int(result)


if __name__ == '__main__':
    sln = Solution()
    # l = [1, 1, 3, 4, 4, 2, ]
    l = [1, 2, 1, 1, 1, 3, 3]
    re = sln.numIdenticalPairs(l)
    print(re)
