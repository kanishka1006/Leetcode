class Solution(object):
    def sequentialDigits(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: List[int]
        """
        digits = "123456789"

        answer = []
        for length in range(len(str(low)),len(str(high))+1):
            for start in range(10-length ):
                num = int(digits[start:start + length])
                if low <=num <=high:
                    answer.append(num)
        return answer
        