class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        '''
        winner , loser -> winner defeated loser
        return answer[[this list has players who didn't lose any match] [this list has players who 
        lost exactly one match ]]
        each of the answer[i] should be sorted in increasing order
        each players win count and loss count
        if the player has 0 loss count then he is a winner foreva
        if the player has loss count == 1 then he's a loser
        '''
        # win_ct = 0
        # los_ct = 0
        player_stats = dict()
        players = set()
        answer = [[],[]]
        for row in matches:
            for idx,player in enumerate(row):
                if player not in players:
                    players.add(player)
                if idx == 0:
                    if player not in player_stats:
                        player_stats[player] = (1,0)
                    else:
                        curr_wins, curr_loss = player_stats.get(player)
                        player_stats[player] = (curr_wins + 1, curr_loss)
                else:
                    if player not in player_stats:
                        player_stats[player] = (0,1)
                    else:
                        curr_wins, curr_loss = player_stats.get(player)
                        player_stats[player] = (curr_wins, curr_loss + 1)
        
        players = sorted(players)
        for p in players:
            win_ct, loss_ct = player_stats.get(p)
            if win_ct or loss_ct != 0:
                if loss_ct == 0:
                    answer[0].append(p)
                elif loss_ct == 1:
                    answer[1].append(p)
        return answer
            
            
