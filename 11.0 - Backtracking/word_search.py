def exist(board: list[list[str]], word: str) -> bool:
    def dfs (i, j, word_i):
        if board[i][j] != word[word_i]:
            return False
        if word_i == len(word) - 1:
            return True
        char = board[i][j]
        board[i][j] = "*"  # mark as visited
        coors = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
        
        for r, c in coors:
            if 0 <= r < len(board) and 0 <= c < len(board[0]):
                if dfs(r, c, word_i + 1):
                    return True     
        
        board[i][j] = char  # unmark as visited
        return False
    for r in range(len(board)):
        for c in range(len(board[0])):
            if dfs(r, c, 0):
                return True
    return False
    
if __name__ == "__main__":
    board = [input().split() for _ in range(int(input("Enter number of rows: ")))]
    word = input("Enter the word to search: ")
    result = exist(board, word)
    print("true" if result else "false")