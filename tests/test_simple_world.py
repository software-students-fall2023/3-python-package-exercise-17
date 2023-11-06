import pytest

from simple_wordle import *

# A function to test the SimpleWordle.guess( ) function
def test_guess ( ):
    with open ( "word_list.txt", "r" ) as file:
        word_list = file.read ( ).splitlines ( )
    game = SimpleWordle ( word_list )

    # Default invalid word message
    invalid_msg = "Invalid word length."

    # Testing as many test cases, feel free to add more if you think of them
    assert game.guess ( "STARK" ) == "🟩🟩🟩🟩🟩"
    assert game.guess ( "stark" ) == "🟩🟩🟩🟩🟩"
    assert game.guess ( "sToCK" ) == "🟩🟩⬛⬛🟩"
    assert game.guess ( "sock" ) == invalid_msg
    assert game.guess ( "starks" ) == invalid_msg
    assert game.guess ( "krats" ) == "🟨🟨🟩🟨🟨"
    assert game.guess ( " " ) == invalid_msg
    assert game.guess ( "\0" ) == invalid_msg

    file.close( )

# Takes the shortcut to make sure the attempts are limited
def test_play_fail_shortcut ( ):
    with open ( "word_list.txt", "r" ) as file:
        word_list = file.read ( ).splitlines ( )
    game = SimpleWordle ( word_list )

    game.attempts = 9999999999999999999999
    assert game.play ( ) == 0

    file.close ( )

# Guesses 6 times incorrectly
def test_play_fail_long ( monkeypatch ):
    with open ( "word_list.txt", "r" ) as file:
        word_list = file.read ( ).splitlines ( )
    game = SimpleWordle ( word_list )

    monkeypatch.setattr ( "builtins.input", lambda _: "stars" )
    assert game.play ( ) == 0
    file.close ( )

# This test ensures the game starts successfully
def test_start_game ( monkeypatch ):

    monkeypatch.setattr ( "builtins.input", lambda _: "stars" )
    assert start_game ( ) == 0

def test_add_word ( ):
    with open ( "word_list.txt", "a" ) as file:
        assert add_word ('hello') == 0
    file.close ()

def test_remove_word ( ):
    with open ( "word_list.txt", "r" ) as file:
        word_list = file.read ( ).splitlines ( )
        if len(word_list)==0:
            # This test ensures the remove function does nothing when word_list empty
            assert remove_word ("hello") == 1
        else:
            # This test ensures the remove function removes successfully when word_list contains the word
            assert remove_word (word_list[0]) == 0
            # This test ensures the remove function does noting  when word_list does not contain the word
            assert remove_word ("ajdfklajdfklajl") == 1
# Makes sure it properly prints the contents
def test_show_word_list ( capsys ):

    show_word_list ( "show_word_list.txt" )
    cap = capsys.readouterr ( )
    all_out = cap.out.split ( "\n" )
    assert all_out [ 0 ] == "stark"
    assert all_out [ 1 ] == "stock"
