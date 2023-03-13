class Solution:
    @classmethod
    def twoSum(cls, nums: list[int], target: int) -> list[int]:
        value = None
        for index_num, num in enumerate(nums):
            residual = target - num
            nums[index_num] = None
            if residual in nums:
                index_residual = nums.index(residual)
                value = list((index_num, index_residual))
                break
        print(value)
        return value

    @classmethod
    def twoSum_2(cls, nums: list[int], target: int) -> list[list[int]]:
        value = []
        for index_num, num in enumerate(nums):
            if num == target:
                value.append([index_num])
                continue
            residual = target - num
            nums[index_num] = None
            if residual in nums:
                index_residual = nums.index(residual)
                value.append(list((index_num, index_residual)))
        print(value)
        return value

    @classmethod
    def twoSum_3(cls, nums: list[int], target: int) -> list[int]:
        for i in range(0, len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    print([i, j])
                    return [i, j]


def _main():
    Solution.twoSum(nums=[1,2,3,4,5,6,7], target=6)
    Solution.twoSum(nums=[0, 1, 2, 3, 4, 5, 6, 7], target=6)
    Solution.twoSum(nums=[3, 2, 3, 4, 5, 6, 7], target=6)
    Solution.twoSum(nums=[3, 3], target=6)
    Solution.twoSum_2(nums=[1, 2, 3, 4, 5, 6, 7], target=6)
    Solution.twoSum_2(nums=[0, 1, 2, 3, 4, 5, 6, 7], target=6)
    Solution.twoSum_3(nums=[1, 2, 3, 4, 5, 6, 7], target=6)
    Solution.twoSum_3(nums=[0, 1, 2, 3, 4, 5, 6, 7], target=6)


if __name__ == '__main__':
    _main()
