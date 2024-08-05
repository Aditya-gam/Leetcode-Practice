class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """

        nums1.sort()
        nums2.sort()
        res = [[], []]
        i = 0
        j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                res[1].append(nums1[i])
                i += 1
            elif nums1[i] > nums2[j]:
                res[2].append(nums2[j])
                j += 1
            else:
                i += 1
                j += 1

        while i < len(nums1):
            res[1].append(nums1[i])
            i += 1

        while j < len(nums2):
            res[2].append(nums2[j])
            j += 1

        return res

    def findDifference1(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        # Alternative solution using set

        nums1 = set(nums1)
        nums2 = set(nums2)

        return list(nums1 - nums2) + list(nums2 - nums1)
