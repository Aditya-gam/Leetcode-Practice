class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """

        maxAltitude = 0
        currentAltitude = 0

        for i in gain:
            currentAltitude += i
            if currentAltitude > maxAltitude:
                maxAltitude = currentAltitude

        return maxAltitude
