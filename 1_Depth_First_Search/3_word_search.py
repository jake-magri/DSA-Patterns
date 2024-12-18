"""
Problem: Word Search
Check if a word exists in a grid using DFS.
"""

def exist(board, word):
    def dfs(i, j, k):
        if k == len(word): return True
        if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or board[i][j] != word[k]:
            return False
        tmp, board[i][j] = board[i][j], "#"
        res = dfs(i+1, j, k+1) or dfs(i-1, j, k+1) or dfs(i, j+1, k+1) or dfs(i, j-1, k+1)
        board[i][j] = tmp
        return res
    
    for i in range(len(board)):
        for j in range(len(board[0])):
            if dfs(i, j, 0): return True
    return False

board = [["A","B","C","E"], ["S","F","C","S"], ["A","D","E","E"]]
word = "ABCCED"
print("Word exists:", exist(board, word))
