import pytest
from project import checkValidMove, checkWin, checkDraw, checkWinWin

def test_checkValidMove():
    board = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
    assert checkValidMove(board, 1) == True
    board = [[' ','O','X'],[' ',' ',' '],[' ',' ',' ']]
    assert checkValidMove(board, 2) == False
    board = [[' ','O','X'],[' ','O',' '],[' ',' ',' ']]
    assert checkValidMove(board, 5) == False
    board = [['X','X','X'],['O',' ','O'],['O','X','X']]
    assert checkValidMove(board, 5) == True

def test_checkWin():
    board = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
    assert checkWin(board) == False
    board = [[' ','O','X'],['X',' ','X'],[' ','O',' ']]
    assert checkWin(board) == False
    board = [['X','X','X'],['O',' ','O'],['O','X','X']]
    assert checkWin(board) == True
    board = [['X','X',' '],['O','O','O'],['O','X','X']]
    assert checkWin(board) == True
    board = [['X',' ','X'],['O',' ','O'],['X','X','X']]
    assert checkWin(board) == True
    board = [['X',' ','X'],['X',' ','O'],['X','O','X']]
    assert checkWin(board) == True
    board = [['O','X','X'],['O','X','O'],[' ','X',' ']]
    assert checkWin(board) == True
    board = [[' ',' ','X'],['O',' ','X'],['O',' ','X']]
    assert checkWin(board) == True
    board = [['X',' ',' '],['O','X','O'],['O',' ','X']]
    assert checkWin(board) == True
    board = [[' ',' ','X'],['O','X','O'],['X',' ',' ']]
    assert checkWin(board) == True

def test_checkDraw():
    board = [[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']],[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']],[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']],[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']],[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']],[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']],[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']],[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']],[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]]
    assert checkDraw(board) == False
    board = [[['X','X','X'],['X',' ','X'],['X','X','X']],[['X','X','X'],['X','X','X'],['X','X','X']],[['X','X','X'],['X','X','X'],['X','X','X']],[['X','X','X'],['X','X','X'],['X','X','X']],[['X','X','X'],['X','X','X'],['X','X','X']],[['X','X','X'],['X','X','X'],['X','X','X']],[['X','X','X'],['X','X','X'],['X','X','X']],[['X','X','X'],['X','X','X'],['X','X','X']],[['X','X','X'],['X','X','X'],['X','X','X']]]
    assert checkDraw(board) == False
    board = [[['X','O','X'],['X',' ','X'],['X','O','X']],[[' ','O','X'],[' ',' ',' '],[' ','X','X']],[['X',' ','X'],['X',' ',' '],[' ',' ','X']],[[' ',' ','X'],['X','X','X'],['X','X',' ']],[['X','X','X'],['X','X','X'],['X','X','X']],[['X','X',' '],['X','X','X'],['X','X','X']],[['X','X','X'],['X','X','X'],['X','X','X']],[['X','X','X'],['X','X','X'],['X','X','X']],[['X','X','X'],['X','X','X'],['X','X','X']]]
    assert checkDraw(board) == False
    board = [[['X','X','X'],['X','O','X'],['X','X','X']],[['X','X','X'],['X','X','X'],['X','X','X']],[['X','X','X'],['X','X','X'],['X','X','X']],[['X','X','X'],['X','X','X'],['X','X','X']],[['X','X','X'],['X','X','X'],['X','X','X']],[['X','X','X'],['X','X','X'],['X','X','X']],[['X','X','X'],['X','X','X'],['X','X','X']],[['X','X','X'],['X','X','X'],['X','X','X']],[['X','X','X'],['X','X','X'],['X','X','X']]]
    assert checkDraw(board) == True

def test_checkWinWin():
    assert checkWinWin([1,2,3,4]) == True
    assert checkWinWin([4,5,6,7]) == True
    assert checkWinWin([7,8,9,]) == True
    assert checkWinWin([1,4,7,3]) == True
    assert checkWinWin([2,5,8,]) == True
    assert checkWinWin([3,6,9,]) == True
    assert checkWinWin([1,5,9,8]) == True
    assert checkWinWin([3,5,7]) == True
    assert checkWinWin([1,3,5]) == False
    assert checkWinWin([7,4,9]) == False
    assert checkWinWin([7,4]) == False
    assert checkWinWin([]) == False
    assert checkWinWin([7,2,9]) == False
