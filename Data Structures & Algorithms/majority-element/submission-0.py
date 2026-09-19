class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candi = 0
        count = 0
        n = len(nums)
        
        for num in nums:
            if (count == 0):        # initialize at start
                candi = num
                count = 1
            elif (num == candi):    # inc count if match
                count += 1
            elif (num != candi):    # dec count if no match
                count -= 1
                if (count == 0):    # if count goes to 0, switch candi, the last man standing is the output
                    candi = num
                    count = 1 
  
        return candi
        