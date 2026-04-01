import copy

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if len(board) < 1:
            return False

        x_len = len(board)
        y_len = len(board[0])

        def search_word(x, y, making_word, visited):
            if len(making_word) != 0:
                if making_word[-1] != word[len(making_word) - 1]:
                    return False

            if len(making_word) == len(word):
                return True

            if x >= x_len or y >= y_len:
                return False
            if x < 0 or y < 0:
                return False

            if visited[x][y] == True:
                return False

            visited[x][y] = True
            print(visited)
            making_word = making_word + board[x][y]
            print(making_word)
            
            if search_word(x - 1, y, making_word, copy.deepcopy(visited)):
                return True;
            if search_word(x + 1, y, making_word, copy.deepcopy(visited)):
                return True;
            if search_word(x, y - 1, making_word, copy.deepcopy(visited)):
                return True;
            if search_word(x, y + 1, making_word, copy.deepcopy(visited)):
                return True;
            
            return False

        
        for x in range(x_len):
            for y in range(y_len):
                visited = [[False] * y_len for _ in range(x_len)]
                if search_word(x, y, "", visited) == True:
                    return True

        return False
        