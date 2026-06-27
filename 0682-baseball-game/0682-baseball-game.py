class Solution:
    def calPoints(self, operations: List[str]) -> int:
        score_stck = []
        final_score = 0
        for i in operations:
            if i == 'C':
                if score_stck:
                    score_stck.pop()
            elif i == 'D':
                if score_stck:
                    score_stck.append(score_stck[-1] * 2)
            elif i == '+':
                if len(score_stck)>=2:
                    score_stck.append(score_stck[-1] + score_stck[-2])
            else:
                score_stck.append(int(i))
        
        for score in score_stck:
            final_score += score
        return final_score

        