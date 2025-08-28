class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        hmap = {}
        res = float("inf")

        for i,n in enumerate(cards):
            if n in hmap:
                res= min(res,i -hmap[n] + 1)
            hmap[n] = i
        
        return res if res != float("inf") else -1

        # hmap = defaultdict(list)
        # res = float("inf")

        # def find_min(l):
        #     res = float("inf")
        #     for i in range(1,len(l)):
        #         res = min(res,abs(l[i]-l[i-1])+1)
        #     return res

        # for i,n in enumerate(cards):
        #     hmap[n].append(i)

        # for l in hmap.values():
        #     if len(l)>1:
        #         res = min(res,find_min(l))
        
        # return res if res != float("inf") else -1