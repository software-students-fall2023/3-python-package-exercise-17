import pytest

from simple_wordle import SimpleWordle

def test_guess ( ):
    with open ( "word_list.txt", "r" ) as file:
        word_list = file.read ( ).splitlines ( )
    game = SimpleWordle ( word_list )
    assert game.guess ( "STARK" ) == "🟩🟩🟩🟩🟩"
    assert game.guess ( "stark" ) == "🟩🟩🟩🟩🟩"
    assert game.guess ( "sToCK" ) == "🟩🟩⬛⬛🟩"
    assert game.guess ( "sock" ) == "Invalid word length."

def test_play ( ):
    pass

def test_start_game ( ):
    pass

def test_add_word ( ):
    pass

def test_remove_word ( ):
    pass

def show_word_list ( ):
    pass