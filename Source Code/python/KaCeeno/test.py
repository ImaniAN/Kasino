'''
Created on 15.4.2014

@author: Paleksi
'''
import unittest
from game import Game

class Test(unittest.TestCase):


    def test_load_game(self):
        game = Game()
        try:
            value, message = game.load_game("broken.txt")
        except IOError:
            pass # should cause IOError
        if (value == True):
            self.fail("Loading an invalid file didn't fail")
            
        game = Game()   # Create a new game
        
        try:
            value, message = game.load_game("testi.txt")
        except IOError:
            self.fail("Loading a correct save file failed" + message)
        if (value == False):
            self.fail("Loading a correct save file failed" + message)
            
        self.assertEqual("Aleksi",  game.get_player_in_turn().get_name(), "Wrong player in turn")
        self.assertEqual("Aleksi", game.get_table().get_latest().get_name(), "Wrong latest player")
        self.assertEqual(4, len(game.get_player_in_turn().get_hand()), "Wrong amount of cards in hand")
        self.assertEqual(2, len(game.get_players()), "Wrong amount of players")
        self.assertEqual(True, game.get_players()[0].is_human(), "Wrong type of Player")
        self.assertEqual(False, game.get_players()[1].is_human(), "Wrong type of Player")
        self.assertEqual(True, game.get_player_in_turn().has_played(), "Wrong boolean for Played")
        self.assertEqual(True, game.get_player_in_turn().has_taken(), "Wrong boolean for Taken")
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()