class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s,t = s.lower(),t.lower()

        temp_dict = {}

        if len(s) != len(t):
            return False
        
        for i in s:
            temp_dict[i] = temp_dict.get(i,0) +1
        for j in t:
            temp_dict[j] = temp_dict.get(j,0) -1
        
        return not any(temp_dict.values())