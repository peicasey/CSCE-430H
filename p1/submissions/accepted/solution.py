from dataclasses import dataclass

@dataclass
class PlayerScore:
    score: float
    player: str
    
    def __lt__(self, other):
        return self.score < other.score
    
    def __gt__(self, other):
        return self.score > other.score

class Node:
    def __init__(self, data, color="red"):
        self.data = data  # playerScore object
        self.color = color
        self.left = None
        self.right = None
        self.parent = None

class RedBlackTree:
    def __init__(self):
        self.TNULL = Node(None)
        self.TNULL.color = "black"
        self.root = self.TNULL

    def insert(self, key):
        node = Node(key)
        node.parent = None
        node.left = self.TNULL
        node.right = self.TNULL
        node.color = "red"

        y = None
        x = self.root

        while x != self.TNULL:
            y = x
            if node.data < x.data:
                x = x.left
            else:
                x = x.right

        node.parent = y
        if y is None:
            self.root = node
        elif node.data < y.data:
            y.left = node
        else:
            y.right = node

        if node.parent is None:
            node.color = "black"
            return

        if node.parent.parent is None:
            return

        self.fix_insert(node)

    def fix_insert(self, k):
        while k.parent.color == "red":
            if k.parent == k.parent.parent.right:
                u = k.parent.parent.left
                if u.color == "red":
                    u.color = "black"
                    k.parent.color = "black"
                    k.parent.parent.color = "red"
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        k = k.parent
                        self.right_rotate(k)
                    k.parent.color = "black"
                    k.parent.parent.color = "red"
                    self.left_rotate(k.parent.parent)
            else:
                u = k.parent.parent.right
                if u.color == "red":
                    u.color = "black"
                    k.parent.color = "black"
                    k.parent.parent.color = "red"
                    k = k.parent.parent
                else:
                    if k == k.parent.right:
                        k = k.parent
                        self.left_rotate(k)
                    k.parent.color = "black"
                    k.parent.parent.color = "red"
                    self.right_rotate(k.parent.parent)
            if k == self.root:
                break
        self.root.color = "black"

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.TNULL:
            y.left.parent = x

        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.TNULL:
            y.right.parent = x

        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def delete(self, node):
        z = node
        y = z
        y_original_color = y.color
        
        if z.left == self.TNULL:
            x = z.right
            self._transplant(z, z.right)
        elif z.right == self.TNULL:
            x = z.left
            self._transplant(z, z.left)
        else:
            y = self._minimum(z.right)
            y_original_color = y.color
            x = y.right
            
            if y.parent == z:
                x.parent = y
            else:
                self._transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
                
            self._transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color
            
        if y_original_color == "black":
            self._fix_delete(x)

    def _transplant(self, u, v):
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def _minimum(self, node):
        while node.left != self.TNULL:
            node = node.left
        return node

    def _fix_delete(self, x):
        while x != self.root and x.color == "black":
            if x == x.parent.left:
                w = x.parent.right
                if w.color == "red":
                    w.color = "black"
                    x.parent.color = "red"
                    self.left_rotate(x.parent)
                    w = x.parent.right
                if w.left.color == "black" and w.right.color == "black":
                    w.color = "red"
                    x = x.parent
                else:
                    if w.right.color == "black":
                        w.left.color = "black"
                        w.color = "red"
                        self.right_rotate(w)
                        w = x.parent.right
                    w.color = x.parent.color
                    x.parent.color = "black"
                    w.right.color = "black"
                    self.left_rotate(x.parent)
                    x = self.root
            else:
                w = x.parent.left
                if w.color == "red":
                    w.color = "black"
                    x.parent.color = "red"
                    self.right_rotate(x.parent)
                    w = x.parent.left
                if w.right.color == "black" and w.left.color == "black":
                    w.color = "red"
                    x = x.parent
                else:
                    if w.left.color == "black":
                        w.right.color = "black"
                        w.color = "red"
                        self.left_rotate(w)
                        w = x.parent.left
                    w.color = x.parent.color
                    x.parent.color = "black"
                    w.left.color = "black"
                    self.right_rotate(x.parent)
                    x = self.root
        x.color = "black"

    def find_node(self, score):
        current = self.root
        while current != self.TNULL:
            if abs(current.data.score - score) < 1e-10:  # use small epsilon for float comparison
                return current
            elif score < current.data.score:
                current = current.left
            else:
                current = current.right
        return None

    def get_successor(self, score):
        current = self.root
        successor = None
        
        while current != self.TNULL:
            if current.data.score > score:
                successor = current
                current = current.left
            else:
                current = current.right
                
        return successor.data if successor else None

    def get_predecessor(self, score):
        current = self.root
        predecessor = None
        
        while current != self.TNULL:
            if current.data.score < score:
                predecessor = current
                current = current.right
            else:
                current = current.left
                
        return predecessor.data if predecessor else None

    def in_order_list(self):
        result = []
        def _in_order(node):
            if node != self.TNULL:
                _in_order(node.left)
                result.append(node.data)
                _in_order(node.right)
        _in_order(self.root)
        return result

class SoccerRanking:
    def __init__(self, players):
        self.players = players
        self.player_to_score = {player: i + 1 for i, player in enumerate(players)}
        self.ranking_tree = RedBlackTree()
        
        for i, player in enumerate(players):
            score = i + 1
            self.ranking_tree.insert(PlayerScore(score, player))
    
    def update_rank(self, player_x, player_y, operation):
        score_x = self.player_to_score[player_x]
        score_y = self.player_to_score[player_y]
        
        # calculate the new relative score between player Y and either its 
        # successor or predecessor 
        if operation == "<":
            successor = self.ranking_tree.get_successor(score_y)
            if successor is None: 
                # player X is being moved to the bottom of the list
                # ie. between score y and score y plus 1
                new_score_x = (score_y + score_y + 1) / 2
            else:
                new_score_x = (score_y + successor.score) / 2
        else: 
            predecessor = self.ranking_tree.get_predecessor(score_y)
            if predecessor is None: 
                # player X is being moved to the top of the list
                # ie. between score 0 and score y
                new_score_x = score_y / 2
            else:
                new_score_x = (score_y + predecessor.score) / 2
        
        node_to_delete = self.ranking_tree.find_node(score_x)
        if node_to_delete:
            self.ranking_tree.delete(node_to_delete)
        
        self.ranking_tree.insert(PlayerScore(new_score_x, player_x))
        self.player_to_score[player_x] = new_score_x

    def print_ranking(self):
        ranked_players = self.ranking_tree.in_order_list()
        for i, player_score in enumerate(ranked_players, 1):
            print(f"{i} {player_score.player}")

def main():
    n, k = map(int, input().split())
    players = [input().strip() for _ in range(n)]
    
    ranking_system = SoccerRanking(players)
    
    for _ in range(k):
        operation = input().strip()
        player_x, op, player_y = operation.split()
        ranking_system.update_rank(player_x, player_y, op)
    
    ranking_system.print_ranking()

if __name__ == "__main__":
    main()
