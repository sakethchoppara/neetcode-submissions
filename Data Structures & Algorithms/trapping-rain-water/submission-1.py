class Solution:
    def trap(self, height: List[int]) -> int:
        h = height
        n = len(h)
        if n == 0:
            return 0
        left_max = [0]*n
        right_max = [0]*n
        left_max[0] = h[0]
        for i in range(1, n):
            left_max[i] = max(left_max[i-1], h[i])
        right_max[n-1] = h[n-1]
        for i in range(n-2, -1, -1):
            right_max[i] = max(right_max[i+1], h[i])
        return sum(min(left_max[i], right_max[i]) - h[i] for i in range(n))

