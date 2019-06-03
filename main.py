import socketio
import random
import mmlib
# HOST_PORT = 'http://192.168.1.127:4000'
# USER_NAME = 'Jose.Memencho'
# TOURNAMENT_ID = 142857

HOST_PORT = 'http://localhost:4000'
USER_NAME = 'Jose'
TOURNAMENT_ID = 12

# 1A - 8G
LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
movimiento = ''

socket_io = socketio.Client()

socket_io.connect(HOST_PORT)

# socket_io.connect('http://192.168.88.252:4000')


@socket_io.on('connect')
def on_connect():
    print('I\'m connected!')
    socket_io.emit('signin', {
        'user_name': USER_NAME,
        'tournament_id': TOURNAMENT_ID,
        'user_role': 'player'
        })


@socket_io.on('ok_signin')
def on_ok():
    print('Succesfully signed in')


@socket_io.on('ready')
def on_ready(data):
    gameID = data['game_id']
    playerTurnID = data['player_turn_id']
    board = data['board']
    print('Got: ', gameID)
    print('Got: ', playerTurnID)
    print('Got: ', board)

    # do a ROLL
    # letter = random.choice(LETTERS)
    # number = random.randint(0, 64)
    # movimiento = number
    
    # do a roll using IA hell yeah
    (move_coord, score) = mmlib.minmax2(board, 0, 3, playerTurnID, playerTurnID)
    # transform the coord into an int
    movimiento = mmlib.coord_to_index(move_coord)

    mmlib.mark(board, move_coord)
    print(move_coord)
    print(movimiento)
    print(board[movimiento])
    # print("sending: ", (TOURNAMENT_ID, playerTurnID, gameID, movimiento, score))
    # print("sending: ", (TOURNAMENT_ID, playerTurnID, gameID, movimiento))

    socket_io.emit('play', {
        'tournament_id': TOURNAMENT_ID,
        'player_turn_id': playerTurnID,
        'game_id': gameID,
        'movement': movimiento
        })


@socket_io.on('finish')
def on_finish(data):
    gameID = data['game_id']
    playerTurnID = data['player_turn_id']
    winnerTurnID = data['winner_turn_id']
    board = data['board']

    socket_io.emit('player_ready', {
        'tournament_id': TOURNAMENT_ID,
        'player_turn_id': playerTurnID,
        'game_id': gameID
    })

# socket_io.disconnect()
