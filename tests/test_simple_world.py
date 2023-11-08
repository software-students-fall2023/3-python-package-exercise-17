import pytest
import os

from simple_wordle import *

# A set of functions to test SimpleWordle.guess ( ) functionality

def test_guess_correct_lowercase ( ):
    with open ( "word_list.txt", "r" ) as file:
        word_list = file.read ( ).splitlines ( )
    game = SimpleWordle ( word_list )

    assert game.guess ( "stark" ) == "🟩🟩🟩🟩🟩"

    file.close ( )

def test_guess_correct_uppercase ( ):
    with open ( "word_list.txt", "r" ) as file:
        word_list = file.read ( ).splitlines ( )
    game = SimpleWordle ( word_list )

    assert game.guess ( "STARK" ) == "🟩🟩🟩🟩🟩"

    file.close ( )

def test_guess_incorrect_grey_unifcase ( ):
    with open ( "word_list.txt", "r" ) as file:
        word_list = file.read ( ).splitlines ( )
    game = SimpleWordle ( word_list )

    assert game.guess ( "stock" ) == "🟩🟩⬛⬛🟩"

    file.close ( )    

def test_guess_incorrect_grey_difcase ( ):
    with open ( "word_list.txt", "r" ) as file:
        word_list = file.read ( ).splitlines ( )
    game = SimpleWordle ( word_list )

    assert game.guess ( "sToCk" ) == "🟩🟩⬛⬛🟩"

    file.close ( )

def test_guess_yellow_ouput ( ):
    with open ( "word_list.txt", "r" ) as file:
        word_list = file.read ( ).splitlines ( )
    game = SimpleWordle ( word_list )

    assert game.guess ( "krats" ) == "🟨🟨🟩🟨🟨"

    file.close ( )

def test_guess_yellow_grey_output ( ):
    with open ( "word_list.txt", "r" ) as file:
        word_list = file.read ( ).splitlines ( )
    game = SimpleWordle ( word_list )

    assert game.guess ( "krots" ) == "🟨🟨⬛🟨🟨"

    file.close ( )

def test_guess_all_color_output ( ):
    with open ( "word_list.txt", "r" ) as file:
        word_list = file.read ( ).splitlines ( )
    game = SimpleWordle ( word_list )

    assert game.guess ( "srotk" ) == "🟩🟨⬛🟨🟩"

    file.close ( )

def test_guess_too_small_input ( ):
    with open ( "word_list.txt", "r" ) as file:
        word_list = file.read ( ).splitlines ( )
    game = SimpleWordle ( word_list )

    assert game.guess ( "sock" ) == "Invalid word length."

    file.close ( )

def test_guess_too_big_input ( ):
    with open ( "word_list.txt", "r" ) as file:
        word_list = file.read ( ).splitlines ( )
    game = SimpleWordle ( word_list )

    assert game.guess ( "starks" ) == "Invalid word length."

    file.close ( )

def test_guess_empty_input ( ):
    with open ( "word_list.txt", "r" ) as file:
        word_list = file.read ( ).splitlines ( )
    game = SimpleWordle ( word_list )

    assert game.guess ( " " ) == "Invalid word length."

    file.close ( )

def test_guess_null_input ( ):
    with open ( "word_list.txt", "r" ) as file:
        word_list = file.read ( ).splitlines ( )
    game = SimpleWordle ( word_list )

    assert game.guess ( "\0" ) == "Invalid word length."

    file.close ( )



# A set of tests to test the SimpleWordle.play ( ) function

def test_play_fail_attempts_shortcut ( ):
    with open ( "word_list.txt", "r" ) as file:
        word_list = file.read ( ).splitlines ( )
    game = SimpleWordle ( word_list )

    game.attempts = 9999999999999999999999
    assert game.play ( ) == 0

    file.close ( )

def test_play_fail_long_input ( monkeypatch ):
    with open ( "word_list.txt", "r" ) as file:
        word_list = file.read ( ).splitlines ( )
    game = SimpleWordle ( word_list )

    monkeypatch.setattr ( "builtins.input", lambda _: "stars" )
    assert game.play ( ) == 0
    file.close ( )

def test_play_success_input ( monkeypatch ):
    with open ( "word_list.txt", "r" ) as file:
        word_list = file.read ( ).splitlines ( )
    game = SimpleWordle ( word_list )

    monkeypatch.setattr ( "builtins.input", lambda _: "stark" )
    assert game.play ( ) == 1
    file.close ( )

# A set of tests to test the start_game ( ) function

def test_start_game_fail ( monkeypatch, capsys ):

    monkeypatch.setattr ( "builtins.input", lambda _: "stars" )
    start_game ( )
    cap = capsys.readouterr ( )
    all_out = cap.out.split ( "\n" )

    for x in range ( 5 ):
        assert all_out [ x ] == "🟩🟩🟩🟩🟨"

    assert all_out [ 6 ] == "Sorry, you didn't guess the word. The correct word was STARK."

def test_start_game_success( monkeypatch, capsys ):

    monkeypatch.setattr ( "builtins.input", lambda _: "stark" )
    start_game ( )
    cap = capsys.readouterr ( )
    all_out = cap.out.split ( "\n" )

    assert all_out [ 0 ] == "🟩🟩🟩🟩🟩"
    assert all_out [ 1 ] == "Congratulations! You've guessed the word in 1 attempts."

def test_start_game_sim_real_win ( monkeypatch, capsys ):

    inputs = iter ( [ "ready", "stars", "starm", "stark"])
    monkeypatch.setattr ( "builtins.input", lambda _: next ( inputs ) )

    start_game ( )
    cap = capsys.readouterr ( )
    all_out = cap.out.split ( "\n" )
    
    assert all_out [ 0 ] == "🟨⬛🟩⬛⬛"
    assert all_out [ 1 ] == "🟩🟩🟩🟩🟨"
    assert all_out [ 2 ] == "🟩🟩🟩🟩⬛"
    assert all_out [ 3 ] == "🟩🟩🟩🟩🟩"
    assert all_out [ 4 ] == "Congratulations! You've guessed the word in 4 attempts."

def test_start_game_sim_real_loss ( monkeypatch, capsys ):

    inputs = iter ( [ "ready", "stars", "starm", "stara", "asdf", "lm", "12345", "hello" ])
    monkeypatch.setattr ( "builtins.input", lambda _: next ( inputs ) )

    start_game ( )
    cap = capsys.readouterr ( )
    all_out = cap.out.split ( "\n" )
    
    assert all_out [ 0 ] == "🟨⬛🟩⬛⬛"
    assert all_out [ 1 ] == "🟩🟩🟩🟩🟨"
    assert all_out [ 2 ] == "🟩🟩🟩🟩⬛"
    assert all_out [ 3 ] == "🟩🟩🟩🟩🟨"
    assert all_out [ 4 ] == "Invalid word length."
    assert all_out [ 5 ] == "Invalid word length."
    assert all_out [ 6 ] == "⬛⬛⬛⬛⬛"
    assert all_out [ 7 ] == "⬛⬛⬛⬛⬛"
    assert all_out [ 8 ] == "Sorry, you didn't guess the word. The correct word was STARK."


# # A set of tests to test the add_word ( ) function

def test_add_word_one ( ):

    add_word ( "hello", "add_word_list.txt" )

    with open( "add_word_list.txt", "r" ) as file:
        words = file.read ( ).splitlines ( )

    assert words [ 0 ] == "HELLO" 

    file.close ( )
    os.remove ( "add_word_list.txt" )

def test_add_word_multiple ( ):

    add_word ( "hello", "add_word_list.txt" )
    add_word ( "WORLD", "add_word_list.txt" )

    with open( "add_word_list.txt", "r" ) as file:
        words = file.read ( ).splitlines ( )

    assert words [ 0 ] == "HELLO"
    assert words [ 1 ] == "WORLD"

    file.close ( )
    os.remove ( "add_word_list.txt" )

def test_add_word_print ( capsys ):

    add_word ( "hello", "add_word_list.txt" )
    add_word ( "WORLD", "add_word_list.txt" )

    cap = capsys.readouterr ( )
    all_out = cap.out.split ( "\n" )
    assert all_out [ 0 ] == "Added HELLO to the word list."
    assert all_out [ 1 ] == "Added WORLD to the word list."

    os.remove ( "add_word_list.txt" )   


# # A set of tests to test the add_word ( ) function

def test_remove_word_not_found ( capsys ):

    remove_word ( "hello", "remove_word_list.txt" )

    cap = capsys.readouterr ( )
    assert cap.out == "HELLO was not found in the word list.\n"

def test_remove_word_found ( capsys ):

    remove_word ( "world", "remove_word_list.txt" )
    cap = capsys.readouterr ( )
    assert cap.out == "Removed WORLD from the word list.\n"

    with open ( "remove_word_list.txt", "w" ) as file:
        file.write ( "WORLD" )
    
    file.close ( )

def test_remove_word_file_check ( ):

    remove_word ( "WORLD", "remove_word_list.txt" )

    assert os.stat("remove_word_list.txt").st_size == 0

    with open ( "remove_word_list.txt", "w" ) as file:
        file.write ( "WORLD" )
    file.close ( )



# A set of tests to test show_word_list ( ) function

def test_show_word_list_2 ( capsys ):

    show_word_list ( "show_word_list_2.txt" )
    cap = capsys.readouterr ( )
    all_out = cap.out.split ( "\n" )
    assert all_out [ 0 ] == "stark"
    assert all_out [ 1 ] == "stock"

def test_show_word_list_0 ( capsys ):

    show_word_list ( "show_word_list_0.txt" )
    cap = capsys.readouterr ( )
    assert cap.out == ""

def test_show_word_list_wrong_length ( capsys ):

    show_word_list ( "show_word_list_wrong.txt" )
    cap = capsys.readouterr ( )
    assert cap.out == "LoremIpsum\n"
