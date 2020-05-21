'''
https://leetcode.com/problems/boats-to-save-people/
'''

=====================================================================================================================
class Solution(object):
    def numRescueBoats(self, people, limit):
        people.sort()
        lower = 0
        highest = len(people) - 1
        boats = 0
        while(lower <= highest):
            if(people[lower] + people[highest] <= limit):
                boats = boats + 1
                lower = lower + 1
                highest = highest - 1
            elif(people[lower] + people[highest] > limit):
                highest = highest - 1
                boats = boats + 1
            else:
                boats = boats + 1
        return boats
  =====================================================================================================================     
  Time complexity: O(NlogN)
  Space complexity : O(1)
