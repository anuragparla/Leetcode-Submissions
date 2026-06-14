class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        losses = dict()

        for winner, loser in matches:
            if winner not in losses:
                losses[winner] = 0
            losses[loser] = losses.get(loser,0) + 1

        zero_losses = []
        one_loss = []

        for player, loss_count in losses.items():
            if loss_count == 0:
                zero_losses.append(player)
            elif loss_count == 1:
                one_loss.append(player)
        
        return [sorted(zero_losses), sorted(one_loss)]
