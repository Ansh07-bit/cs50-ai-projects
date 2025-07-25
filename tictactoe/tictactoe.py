"""
Tic Tac Toe Player
"""
import copy
import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    Xno = 0  # Frequency of X
    Ono = 0  # Frequency of O
    
    # Checking frequency by iterating through the board
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                continue
            elif board[i][j] == X:
                Xno += 1
            elif board[i][j] == O:
                Ono += 1
    
    # returning the value based on frequency keeping in mind that X will be playing first
    if Xno == Ono:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()  # set to store actions

    # Finding the empty space
    for i in range(3):
        for j in range(3):
            if not board[i][j]:
                actions.add((i, j))

    return actions            


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):  # checking the action is valid or not 
        raise Exception("Invalid Input")  # if not raise an Exception
    
    newBoard = copy.deepcopy(board)  # deepcopy the board 

    newBoard[action[0]][action[1]] = player(board)  # performing the action

    return newBoard


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
     
    # checking for the same element in the row or colomn 
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != None:
            return board[i][0]  # returning the winner
        if board[0][i] == board[1][i] == board[2][i] != None:
            return board[0][i]  # returning the winner
    
    # checking for the same diagonal element
    if board[0][0] == board[1][1] == board[2][2] != None:
        return board[0][0]  # returning the winner
    if board[0][2] == board[1][1] == board[2][0] != None:
        return board[0][2]  # returning the winner
    
    return None  # Result for the no player exists
    
    
def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    
    # game ending by win of someone
    if winner(board):
        return True
    
    # game ending by draw
    for i in range(3):
        for j in range(3):
            if board[i][j] is EMPTY:
                return False
    
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    winningPlayer = winner(board)  # saving the winner

    # Returning the min or max value
    if winningPlayer is None:
        return 0
    elif winningPlayer == X:
        return 1
    else:
        return -1


def min_value(board):
    """ 
    Returns min value the given board
    """

    # if it is the terminal state it returns the utility of the state
    if terminal(board):
        return utility(board)
     
    v = float('inf')  # Initializing the return value

    # finding min of next max values
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    
    return v


def max_value(board):
    """ 
    Returns max value the given board
    """

    # if it is the terminal state it returns the utility of the state
    if terminal(board):
        return utility(board)
     
    v = float('-inf')  # Initializing the return value

    # finding max of next min values
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    
    return v


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    # if it is the terminal state it returns the utility of the state
    if terminal(board):
        return None
    
    optimalAction = None  # action to be return 
    
    if player(board) == X:
        pre = v = float('-inf')  # Initializing the return value and previous value

        # finding max of next min values
        for action in actions(board):
            v = max(v, min_value(result(board, action)))
            if v > pre:
                pre = v
                optimalAction = action
        
        return optimalAction
    else:
        pre = v = float('inf')  # Initializing the return value and previous value

        # finding min of next min values
        for action in actions(board):
            v = min(v, max_value(result(board, action)))
            if v < pre:
                pre = v
                optimalAction = action
        
        return optimalAction