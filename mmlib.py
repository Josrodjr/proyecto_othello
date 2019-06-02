import math
import copy
import numpy
# Othello white moves with low evaluation scores
# Othello black moves with high evaluations scores

# player turn either 2 1 or 0
PLAYER_TURN = 2

BOARD = [0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 2, 1, 0, 0, 0,
         0, 0, 0, 1, 2, 0, 0, 0,
         0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 0, 0, 0, 0]

BOARD_SCORE = [8, -2, 3, 3, 3, 3, -2, 8,
               -2, 1, 2, 2, 2, 2, 1, -2,
               3, 2, 1, 1, 1, 1, 2, 3,
               3, 2, 1, 1, 1, 1, 2, 3,
               3, 2, 1, 1, 1, 1, 2, 3,
               3, 2, 1, 1, 1, 1, 2, 3,
               -2, 1, 2, 2, 2, 2, 1, -2,
               8, -2, 3, 3, 3, 3, -2, 8]

SENDING = (12, 2, 5287908743203175, 7)


# generate an INT evaluation of board
# return (sum(score * board) + sum(board))
def explore(board_layout):
    score = numpy.array(BOARD_SCORE)
    board = numpy.array(board_layout)
    temp_score = score * board
    num_score = numpy.sum(temp_score) + numpy.sum(board)
    print(num_score)
    return 0


def tomatrix(board_layout):
    one = board_layout[0:8]
    two = board_layout[8:16]
    three = board_layout[16:24]
    four = board_layout[24:32]
    five = board_layout[32:40]
    six = board_layout[40:48]
    seven = board_layout[48:56]
    eight = board_layout[56:64]
    mat = numpy.asmatrix((one, two, three, four, five, six, seven, eight))
    return mat


def onboard(x, y):
    # Returns True if the coordinates are located on the board.
    return x >= 0 and x <= 7 and y >= 0 and y <=7


def validspots(board_layout, turn):
    if turn == 1:
        otherturn = 2
    if turn == 2:
        otherturn = 1
    possible_moves = []
    board_mat = tomatrix(board_layout)
    for x in range(8):
        for y in range(8):
            if board_mat[x, y] == otherturn:
                if onboard(x, y+1):
                    if board_mat[x, y+1] == 0:
                        possible_moves.append([x, y+1])
                if onboard(x+1, y):
                    if board_mat[x+1, y] == 0:
                        possible_moves.append([x+1, y])
                if onboard(x+1, y+1):
                    if board_mat[x+1, y+1] == 0:
                        possible_moves.append([x+1, y+1])
                if onboard(x, y-1):
                    if board_mat[x, y-1] == 0:
                        possible_moves.append([x, y-1])
                if onboard(x-1, y):
                    if board_mat[x-1, y] == 0:
                        possible_moves.append([x-1, y])
                if onboard(x-1, y-1):
                    if board_mat[x-1, y-1] == 0:
                        possible_moves.append([x-1, y-1])
                if onboard(x-1, y+1):
                    if board_mat[x-1, y+1] == 0:
                        possible_moves.append([x-1, y+1])
                if onboard(x+1, y-1):
                    if board_mat[x+1, y-1] == 0:
                        possible_moves.append([x+1, y-1])
    return possible_moves


def mark(board_layout, moves):
    board_mat = tomatrix(board_layout)
    for x, y in moves:
        board_mat[x, y] = 69
    print(board_mat)
    return 0


# yikes = validspots(BOARD, 1)
# mark(BOARD, yikes)

# generate a new BOARD with the move
def make_move(board_layout, move, turn):
    x, y = move
    if turn == 1:
        otherturn = 2
    if turn == 2:
        otherturn = 1
    board_mat = tomatrix(board_layout)
    # first horsemen
    if onboard(x, y):
        board_mat[x, y] = turn
    # eight horsemen
    if onboard(x, y+1):
        if board_mat[x, y+1] == otherturn:
            board_mat[x, y+1] = turn
    if onboard(x+1, y):
        if board_mat[x+1, y] == otherturn:
            board_mat[x+1, y] = turn
    if onboard(x+1, y+1):
        if board_mat[x+1, y+1] == otherturn:
            board_mat[x+1, y+1] = turn
    if onboard(x, y-1):
        if board_mat[x, y-1] == otherturn:
            board_mat[x, y-1] = turn
    if onboard(x-1, y):
        if board_mat[x-1, y] == otherturn:
            board_mat[x-1, y] = turn
    if onboard(x-1, y-1):
        if board_mat[x-1, y-1] == otherturn:
            board_mat[x-1, y-1] = turn
    if onboard(x-1, y+1):
        if board_mat[x-1, y+1] == otherturn:
            board_mat[x-1, y+1] = turn
    if onboard(x+1, y-1):
        if board_mat[x+1, y-1] == otherturn:
            board_mat[x+1, y-1] = turn
    # flatten the board
    # flat = board_mat.flatten()
    flat = numpy.column_stack(board_mat).flatten().tolist()
    return flat[0]

# print(tomatrix(make_move(BOARD, [3, 5], 2)))


# generate the best move and the best score for the depth searched
# default depth searched should start at 0
def minmax(board_layout, depth_searched, max_depth_searched, turn):
    chosen_move = 0
    move_board_score = 0
    # algorithm logic 
    # explore then call minmax on each possible move

    if depth_searched == max_depth_searched:
        chosen_move = explore(board_layout)
    else:
        # generate a list of moves that alter the boardstate
        moves_list = validspots(board_layout, turn)
        # no valid moves
        if len(moves_list) == 0:
            chosen_move = explore(board_layout)
        else:
            for move in moves_list:
                best_score = math.inf
                temporal_board = copy.deepcopy(board_layout)
                altered_board = make_move(temporal_board, move, turn)
                new_depth = depth_searched + 1
                # change the turn
                if turn == 1:
                    turn = 2
                else:
                    turn = 1
                # check the minmax of the altered board but moving the depth searched
                (rec_move, rec_board_score) = minmax(altered_board, new_depth, max_depth_searched, turn)
                # change the chosen moves and the chosen scores
                if rec_board_score < best_score:
                    chosen_move = rec_move
                    move_board_score = rec_board_score
                                 
    return (chosen_move, move_board_score)