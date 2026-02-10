class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
      //sort the numbers in the list to put them in ascending order
        nums.sort()
      //initializing the loop variable
        i=0
        while(i<len(nums)):
          //the first number in the list is swapped with the second number in the list and the process continues till the loop ends which gives us the resulting solution
            nums[i], nums[i+1]= nums[i+1], nums[i]
          // the iteration is set to 2 instead of 1 so that the number of iterations will be half of the given length
            i+=2
          // return the resulting nums array
        return nums
