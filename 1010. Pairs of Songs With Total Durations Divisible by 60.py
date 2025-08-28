class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        """
        res = 2
        hmap = {
        }

        [30,20,150,100,40]
          ^
          30
          60-30 =30
        for x in time:
          remainder = x % 60
          to_find = ( 60- remainder ) % 60 
          if to_find in hmap:
            res += hmap[to_find]
          hmap[remainder] = hmap.get(remainder,0) + 1
        """
        res = 0 
        hmap = {}
        for x in time:
          remainder = x % 60
          to_find = ( 60- remainder ) % 60 
          if to_find in hmap:
            res += hmap[to_find]
          hmap[remainder] = hmap.get(remainder,0) + 1
        
        return res