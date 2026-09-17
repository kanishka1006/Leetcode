class Solution:
    def minSumOfLengths(self, arr, target):
        n = len(arr)
        INF = n + 1

        best = [INF] * n

        left = 0
        total = 0
        answer = INF

        for right in range(n):
            total += arr[right]

            while total > target:
                total -= arr[left]
                left += 1

            if total == target:
                length = right - left + 1

                # Check for a previous non-overlapping subarray
                if left > 0 and best[left - 1] != INF:
                    answer = min(answer, length + best[left - 1])

                best[right] = length

            # Carry forward the best subarray found so far
            if right > 0:
                best[right] = min(best[right], best[right - 1])

        if answer == INF:
            return -1

        return answer