from sortedcontainers import SortedDict

class SoccerRanking:
    def __init__(self, players):
        self.players = players
        self.player_to_score = {player: i + 1 for i, player in enumerate(players)}  # 1-based ranks
        self.ranking_tree = SortedDict()
        
        # Initially populate the tree with player names and their relative scores
        for i, player in enumerate(players):
            self.ranking_tree[self.player_to_score[player]] = player

    
    def update_rank(self, player_x, player_y, operation):
        score_x = self.player_to_score[player_x]
        score_y = self.player_to_score[player_y]
        
        if operation == "<":
            # Find the successor of player_y (i.e., the next rank above player_y)
            # Successor is the player who has the smallest score strictly greater than score_y
            successor_score = next(iter(self.ranking_tree.irange(score_y + 1, None)), None)
            print(successor_score)
            if successor_score is None:
                # If there's no successor, place player_x at the end
                new_score_x = (score_y + score_y + 1) / 2

            else:
                # New score for player_x is the average of player_y's score and the successor's score
                new_score_x = (score_y + successor_score) / 2
            
            # Remove player_x from the tree and update its score
            del self.ranking_tree[score_x]
            self.ranking_tree[new_score_x] = player_x
            self.player_to_score[player_x] = new_score_x

        elif operation == ">":
            # Find the predecessor of player_y (i.e., the next rank below player_y)
            # Predecessor is the player who has the largest score strictly less than score_y
            predecessor_score = next(iter(self.ranking_tree.irange(None, score_y - 1)), None)
            print(predecessor_score)
            if predecessor_score is None:
                # If there's no predecessor, place player_x at the beginning
                new_score_x = (score_y + 0) / 2
            else:
                # New score for player_x is the average of player_y's score and the predecessor's score
                new_score_x = (score_y + predecessor_score) / 2
            
            # Remove player_x from the tree and update its score
            del self.ranking_tree[score_x]
            self.ranking_tree[new_score_x] = player_x
            self.player_to_score[player_x] = new_score_x

    def print_ranking(self):
        i = 1
        for score in self.ranking_tree:
            print(f"{i} {self.ranking_tree[score]}")
            i += 1
            
def main():
    n, k = map(int, input().split()) 
    players = [input().strip() for _ in range(n)]

    ranking_system = SoccerRanking(players)
    
    for _ in range(k):
        operation = input().strip()
        player_x, op, player_y = operation.split()
        print(operation)
        ranking_system.update_rank(player_x, player_y, op)

    ranking_system.print_ranking()

if __name__ == "__main__":
    main()
