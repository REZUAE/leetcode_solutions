from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        """
        hmap[sorted_word] = [word1,word2,word3]        
        """
        hmap = defaultdict(list)
        for s in strs:
            sorted_word = ''.join(sorted(s))  # O(n log n)
            hmap[sorted_word].append(s)

        return list(hmap.values())


print(ord("z") - ord("a") )

# # ---------------- Test Cases ----------------
# if __name__ == "__main__":
#     sol = Solution()

#     # Each test case is a tuple: (input, expected_output)
#     test_cases = [
#         (["eat","tea","tan","ate","nat","bat"], [["eat","tea","ate"],["tan","nat"],["bat"]]),
#         ([""], [[""]]),
#         (["a"], [["a"]])
#     ]

#     for i, (input_data, expected) in enumerate(test_cases):
#         output = sol.groupAnagrams(input_data)
#         # Since the order of groups and words in each group may vary, we need to normalize for comparison
#         output_sorted = [sorted(group) for group in output]
#         expected_sorted = [sorted(group) for group in expected]

#         if sorted(output_sorted) == sorted(expected_sorted):
#             print(f"Test case {i+1}: ✅ Passed")
#         else:
#             print(f"Test case {i+1}: ❌ Failed")
#             print(f"Input: {input_data}")
#             print(f"Output: {output}")
#             print(f"Expected: {expected}")
