class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrame_dict ={}

        for w in strs:
            sort_word = ''.join(sorted(w))

            anagrame_dict.setdefault(sort_word,[]).append(w)
        
        return list(anagrame_dict.values())