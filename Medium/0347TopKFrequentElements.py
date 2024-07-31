class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        n = len(nums)
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        bucket = [[] for _ in range(n + 1)]

        for num, count in freq.items():
            bucket[count].append(num)

        res = []

        for i in range(n, 0, -1):
            res.extend(bucket[i])

            if len(res) >= k:
                break

        return res[:k]

    def topKFrequent1(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        return [num for num, _ in sorted(freq.items(), key=lambda x: x[1], reverse=True)[:k]]
