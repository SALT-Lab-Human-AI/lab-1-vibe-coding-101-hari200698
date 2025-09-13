import unittest
from src.game import Game

class TestGame(unittest.TestCase):

    def setUp(self):
        self.game = Game()

    def test_initial_score(self):
        self.assertEqual(self.game.score_player1, 0)
        self.assertEqual(self.game.score_player2, 0)

    def test_start_game(self):
        self.game.start_game()
        self.assertIsNotNone(self.game.ball)
        self.assertTrue(self.game.is_running)

    def test_update_score_player1(self):
        self.game.update_score(1)
        self.assertEqual(self.game.score_player1, 1)

    def test_update_score_player2(self):
        self.game.update_score(2)
        self.assertEqual(self.game.score_player2, 1)

    def test_ball_collision_with_paddle(self):
        initial_position = self.game.ball.position
        self.game.ball.position = (self.game.paddle1.position[0], self.game.paddle1.position[1])
        self.game.ball.bounce()
        self.assertNotEqual(initial_position, self.game.ball.position)

if __name__ == '__main__':
    unittest.main()