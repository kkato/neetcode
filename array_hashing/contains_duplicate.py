class Solution:
  def hasDuplicate(self, nums: list[int]) -> bool:
    hashset = set()

    for n in nums:
      if n in hashset:
        return True
      hashset.add(n)
    return False

if __name__ == "__main__":
  sol = Solution()
  print(sol.hasDuplicate(nums=[1, 2, 3, 3]))
