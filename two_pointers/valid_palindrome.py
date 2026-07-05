class Solution:
  def isPlindrome(self, s:str) -> bool:
    newStr = ""
    for c in s:
      if c.isalnum():
        newStr += c.lower()

    return newStr == newStr[::-1]

if __name__ == '__main__':
  sol = Solution()
  print(sol.isPlindrome("Was it a car or a cat I saw?"))
