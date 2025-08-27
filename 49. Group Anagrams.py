class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        hmap[sorted_word] = [word1,word2,word3]        
        """
        hmap = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for char in s:
                res = ord(char) - ord('a')
                count[res] += 1
            hmap[tuple(count)].append(s)

        return list(hmap.values())


        # hmap = defaultdict(list)
        # for s in strs:
        #     sorted_word = ''.join(sorted(s)) #Onlogn
        #     hmap[sorted_word].append(s)

        # return list(x for x in hmap.values())

