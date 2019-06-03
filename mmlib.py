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


def coord_to_index(position):
    (x, y) = position
    result = (x * 8) + y
    return result


# generate an INT evaluation of board
# return (sum(score * board) + sum(board))
def explore(board_layout, turn):
    # remove from the equation the values from the other turn
    if turn == 2:
        otherturn = 1
    if turn == 1:
        otherturn = 2
    score = numpy.array(BOARD_SCORE)
    board = numpy.array(board_layout)
    # remove the values of the other turn
    board[board == otherturn] = 0
    # now in case that we got turn 2 turn the 2-s into 1-s
    board[board == 2] = 1
    # print(board)
    temp_score = score * board
    num_score = numpy.sum(temp_score) + numpy.sum(board)
    return num_score


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
                        # move in the opposite direction searching for a turn
                        incidence = 0
                        yval = y
                        while yval >= 0:
                            if board_mat[x, yval] == turn:
                                incidence += 1
                            yval -= 1
                        # if any incidences of our turn on that direction
                        if incidence > 0:
                            possible_moves.append([x, y+1])
                if onboard(x+1, y):
                    if board_mat[x+1, y] == 0:
                        # move in the opposite direction searching for a turn
                        incidence = 0
                        xval = x
                        while xval >= 0:
                            if board_mat[xval, y] == turn:
                                incidence += 1
                            xval -= 1
                        # if any incidences of our turn on that direction
                        if incidence > 0:
                            possible_moves.append([x+1, y])
                if onboard(x+1, y+1):
                    if board_mat[x+1, y+1] == 0:
                        # move in the opposite direction searching for a turn
                        incidence = 0
                        xval = x
                        yval = y
                        while xval >= 0 and yval >= 0:
                            if board_mat[xval, yval] == turn:
                                incidence += 1
                            xval -= 1
                            yval -= 1
                        # if any incidences of our turn on that direction
                        if incidence > 0:
                            possible_moves.append([x+1, y+1])
                if onboard(x, y-1):
                    if board_mat[x, y-1] == 0:
                        # move in the opposite direction searching for a turn
                        incidence = 0
                        yval = y
                        while yval <= 7:
                            if board_mat[x, yval] == turn:
                                incidence += 1
                            yval += 1
                        # if any incidences of our turn on that direction
                        if incidence > 0:
                            possible_moves.append([x, y-1])
                if onboard(x-1, y):
                    if board_mat[x-1, y] == 0:
                        # move in the opposite direction searching for a turn
                        incidence = 0
                        xval = x
                        while xval <= 7:
                            if board_mat[xval, y] == turn:
                                incidence += 1
                            xval += 1
                        # if any incidences of our turn on that direction
                        if incidence > 0:
                            possible_moves.append([x-1, y])
                if onboard(x-1, y-1):
                    if board_mat[x-1, y-1] == 0:
                        # move in the opposite direction searching for a turn
                        incidence = 0
                        xval = x
                        yval = y
                        while xval <= 7 and yval <= 7:
                            if board_mat[xval, yval] == turn:
                                incidence += 1
                            xval += 1
                            yval += 1
                        # if any incidences of our turn on that direction
                        if incidence > 0:
                            possible_moves.append([x-1, y-1])
                if onboard(x-1, y+1):
                    if board_mat[x-1, y+1] == 0:
                        # move in the opposite direction searching for a turn
                        incidence = 0
                        xval = x
                        yval = y
                        while xval <= 7 and yval >= 0:
                            if board_mat[xval, yval] == turn:
                                incidence += 1
                            xval += 1
                            yval -= 1
                        # if any incidences of our turn on that direction
                        if incidence > 0:
                            possible_moves.append([x-1, y+1])
                if onboard(x+1, y-1):
                    if board_mat[x+1, y-1] == 0:
                        # move in the opposite direction searching for a turn
                        incidence = 0
                        xval = x
                        yval = y
                        while xval >= 0 and yval <= 7:
                            if board_mat[xval, yval] == turn:
                                incidence += 1
                            xval -= 1
                            yval += 1
                        # if any incidences of our turn on that direction
                        if incidence > 0:
                            possible_moves.append([x+1, y-1])
    return possible_moves


def mark(board_layout, moves):
    board_mat = tomatrix(board_layout)
    print(board_mat)
    x, y = moves
    board_mat[x, y] = 42
    print(board_mat)
    return board_mat


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
def minmax(board_layout, depth_searched, max_depth_searched, turn, absoluteturn):
    chosen_move = 0
    move_board_score = 0
    # algorithm logic 
    # explore then call minmax on each possible move

    if depth_searched == max_depth_searched:
        chosen_move = explore(board_layout, turn)
    else:
        # generate a list of moves that alter the boardstate
        moves_list = validspots(board_layout, turn)
        # no valid moves
        if len(moves_list) == 0:
            chosen_move = explore(board_layout, turn)
        else:
            for move in moves_list:
                best_score = math.inf
                temporal_board = copy.deepcopy(board_layout)
                # print(('temp', tomatrix(temporal_board)))
                altered_board = make_move(temporal_board, move, turn)
                # print(('alter', tomatrix(altered_board)))
                # value of the altered board
                # rec_board_score = explore(altered_board)
                # print(rec_board_score)
                new_depth = depth_searched + 1
                # change the turn
                if turn == 1:
                    turn = 2
                if turn == 2:
                    turn = 1
                # check the minmax of the altered board but moving the depth searched
                # print(( new_depth, max_depth_searched, turn))
                (rec_move, rec_board_score) = minmax(altered_board, new_depth, max_depth_searched, turn, absoluteturn)
                # change the chosen moves and the chosen scores
                if rec_board_score < best_score and absoluteturn == turn:
                    chosen_move = rec_move
                    move_board_score = rec_board_score
    return (chosen_move, move_board_score)


def minmax_lower(board_layout, depth_searched, max_searched, turn, absolute_turn):
    the_move = 0
    the_score = 0
    best_min = math.inf
    # save the votes that this move got based on the lowest score
    average_move = 0
    moves_list = validspots(board_layout, turn)
    # scores = []
    for move in moves_list:
        temp_board = copy.deepcopy(board_layout)
        altered_board = make_move(temp_board, move, turn)
        # score the new board
        score = explore(altered_board, turn)
        # scores.append(score)
        if score < best_min:
            the_move = move
            the_score = score
    # after we got the scores of the minimizer we do average move
    # average_move = sum(scores)/len(scores)
    # UP TO HERE WE GOT MAX VALUE AND VALID INPUT
    return (the_move, the_score)


def minmax2(board_layout, depth_searched, max_searched, turn, absolute_turn):
    # for the first iteration get the best move score wise
    moves_list = validspots(board_layout, turn)
    the_score = 0
    the_move = 0
    # minimizer param
    best_min = math.inf

    if depth_searched != max_searched:
        if turn == absolute_turn:
            # DO MAXIMIZER
            # for each move in this level
            for move in moves_list:
                temp_board = copy.deepcopy(board_layout)
                altered_board = make_move(temp_board, move, turn)
                # score the new board
                score = explore(altered_board, turn)
                
                # send the new board to the minimizer so we see what options enemy has
                if turn == 1:
                    otherturn = 2
                if turn == 2:
                    otherturn = 1
                the_min_move, the_min_score = minmax2(altered_board, depth_searched+1, max_searched, otherturn, absolute_turn)

                # if it is the best score we got so far we save the move and the score
                if score > the_score and the_min_score < best_min:
                    the_score = score
                    the_move = move
        else:
            # DO MINIMIZER
            local_high = 0
            the_min_move = 0
            the_min_score = 0
            for move in moves_list:
                temp_board = copy.deepcopy(board_layout)
                altered_board = make_move(temp_board, move, turn)
                # score the new board
                score = explore(altered_board, turn)
                
                # throw the recurrency if works
                if turn == 1:
                    otherturn = 2
                if turn == 2:
                    otherturn = 1
                
                the_max_move, the_max_score = minmax2(altered_board, depth_searched+1, max_searched, otherturn, absolute_turn)

                if score < best_min and the_max_score > local_high:
                    the_min_move = move
                    the_min_score = score
                return (the_min_move, the_min_score)
        
    # UP TO HERE WE GOT MAX VALUE AND VALID INPUT
    return (the_move, the_score)


# print(minmax2(BOARD, 0, 3, 2, 2))

# print(minmax(BOARD, 0, 2, 1, 1))
# chosen_move, score = minmax(BOARD, 0, 2, 1, 1)
# BOARD[chosen_move] = 70
# print(tomatrix(BOARD))