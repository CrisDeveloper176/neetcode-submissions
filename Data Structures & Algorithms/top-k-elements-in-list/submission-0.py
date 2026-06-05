import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map1 = {}
        result = []
        for i in range(len(nums)):
            map1[nums[i]] = map1.get(nums[i], 0) + 1
        maxheap = []
        for num, freq in map1.items():
            heapq.heappush(maxheap, (-freq, num))
        
        for i in range(k):
            freq, num = heapq.heappop(maxheap)
            result.append(num)
        return result
            

        

             