class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}

        for s in strs:
            count_list = [0] * 26
            for c in s:
                count_list[ord(c) - ord('a')] += 1
            
            fingerprint = tuple(count_list)
            if fingerprint not in dic:
                dic[fingerprint] = []
            dic[fingerprint].append(s)

        return list(dic.values())

