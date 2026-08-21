class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        
        for num in nums: 
            if num in dic:
                dic[num] += 1
            else:
                dic[num] = 1

        # values_list = list(dic.values())
        sorted_numbers = sorted(dic.keys(), key=dic.get, reverse=True)

        return sorted_numbers[:k]