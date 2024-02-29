class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        answer = -inf
        left = 0
        total_pts = sum(cardPoints)
        n = len(cardPoints)
        curr_sum =0
        if n == k:
            return total_pts
        for right in range(len(cardPoints)):
            curr_sum += cardPoints[right]
            if right-left+1 >= n-k:
                answer = max(answer,total_pts-curr_sum)
                curr_sum -= cardPoints[left]
                left+=1


        return answer
