class Solution:
    found_exit = False

    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        row_len = len(maze)
        col_len = len(maze[0])
        self.find_path(start[0], start[1], destination[0], destination[1], maze, row_len, col_len)
        found = self.found_exit
        self.found_exit = False
        return found

    def find_path(self, curr_row, curr_col, dest_row, dest_col, maze, row_len, col_len):

        # stop condition #1
        # reached edge of maze
        if curr_row < 0 or curr_row >= row_len or curr_col < 0 or curr_col >= col_len or maze[curr_row][
            curr_col] == "#":
            print("reached edge of maze")
            return

        # stop condition #2
        # found the exit
        if curr_row is dest_row and curr_col is dest_col:
            print("found the exit")
            self.found_exit = True
            return

        # mark current as visited
        # tmp = maze[curr_row][curr_col]
        maze[curr_row][curr_col] = '#'

        # traverse till there is a wall
        a = b = c = d = curr_row
        e = f = g = h = curr_col

        # up
        while a - 1 >= 0 and a - 1 < row_len and e >= 0 and e < col_len and maze[a - 1][e] is not 1:
            a -= 1
        if maze[a][e] != '#':
            self.find_path(a, e, dest_row, dest_col, maze, row_len, col_len)

        # west
        while b >= 0 and b < row_len and f - 1 >= 0 and f - 1 < col_len and maze[b][f - 1] is not 1:
            f -= 1
        if maze[b][f] != '#':
            self.find_path(b, f, dest_row, dest_col, maze, row_len, col_len)

        # south
        while c + 1 >= 0 and c + 1 < row_len and g >= 0 and g < col_len and maze[c + 1][g] is not 1:
            c += 1

        if maze[c][g] != '#':
            self.find_path(c, g, dest_row, dest_col, maze, row_len, col_len)

        # east
        while d >= 0 and d < row_len and h + 1 >= 0 and h + 1 < col_len and maze[d][h + 1] is not 1:
            h += 1

        if maze[d][h] != '#':
            self.find_path(d, h, dest_row, dest_col, maze, row_len, col_len)
