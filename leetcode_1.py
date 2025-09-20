class Solution:
    def countCompleteSubarrays(self, nums):
        n = len(nums)
        totalDistinct = len(set(nums))
        ans = 0

        for i in range(n):
            seen = set()
            for j in range(i, n):
                seen.add(nums[j])
                if len(seen) == totalDistinct:
                    # all subarrays nums[i:j], nums[i:j+1], ..., nums[i:n-1]
                    # where the first index that reaches full distinctness is j:
                    ans += (n - j)
                    break
        return ans

# Example quick test (you can remove before submitting to judge):
if __name__ == "__main__":
    print(Solution().countCompleteSubarrays([1,3,1,2,2]))  # 4
    print(Solution().countCompleteSubarrays([5,5,5,5]))    # 10