def validspot(board_layout, turn, x, y):
    # get the other player
    if turn == 1:
        otherturn = 2
    if turn == 2:
        otherturn = 1
    # transform the board into matrix
    board_mat = tomatrix(board_layout)
    # save time by checking if tile is taken
    if board_mat[x, y] != 0:
        return False
    # number of flipped tiles
    tiles_flipped = 0
    for xdir, ydir in [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]:
        x += xdir
        y += ydir
        if onboard(x, y):
            if board_mat[x, y] == otherturn:
                # there are tiles we can flip next to this tile
                x -= xdir
                y -= ydir
                # return True
                tiles_flipped += 1
    
    if tiles_flipped > 0:
        return True
    else:
        return False


# generate a LIST of possible moves
def moves(board_layout, turn):
    possible_moves = []
    count = 0
    for x in range(8):
        for y in range(8):
            count += 1
            if validspot(board_layout, turn, x, y):
                possible_moves.append([x, y])
    print(count)
    return possible_moves