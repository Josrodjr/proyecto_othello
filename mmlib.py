import math
import copy
# Othello white moves with low evaluation scores
# Othello black moves with high evaluations scores


# generate an INT evaluation of board
def explore(board_layout):
    return 0


# generate a LIST of possible moves
def moves(board_layout):
    possible_moves = []
    return possible_moves


# generate a new BOARD with the move
def make_move(board_layout, move):
    return 0


# generate the best move and the best score for the depth searched
# default depth searched should start at 0
def minmax(board_layout, depth_searched, max_depth_searched):
    chosen_move = 0
    move_board_score = 0
    # algorithm logic 
    # explore then call minmax on each possible move

    if depth_searched == max_depth_searched:
        chosen_move = explore(board_layout)
    else:
        # generate a list of moves that alter the boardstate
        moves_list = moves(board_layout)
        # no valid moves
        if len(moves_list) == 0:
            chosen_move = explore(board_layout)
        else:
            for move in moves_list:
                best_score = math.inf
                temporal_board = copy.deepcopy(board_layout)
                altered_board = make_move(temporal_board, move)
                new_depth = depth_searched + 1
                # check the minmax of the altered board but moving the depth searched
                (rec_move, rec_board_score) = minmax(altered_board, new_depth, max_depth_searched)
                # change the chosen moves and the chosen scores
                if rec_board_score < best_score:
                    chosen_move = rec_move
                    move_board_score = rec_board_score
                                 
    return (chosen_move, move_board_score)