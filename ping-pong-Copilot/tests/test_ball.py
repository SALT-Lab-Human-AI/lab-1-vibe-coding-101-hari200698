import unittest
from src.ball import Ball
from src.constants import SCREEN_WIDTH, SCREEN_HEIGHT

class TestBall(unittest.TestCase):

    def setUp(self):
        self.ball = Ball()

    def test_initial_position(self):
        self.assertEqual(self.ball.x, SCREEN_WIDTH // 2)
        self.assertEqual(self.ball.y, SCREEN_HEIGHT // 2)

    def test_move(self):
        initial_x = self.ball.x
        initial_y = self.ball.y
        self.ball.move()
        self.assertNotEqual(self.ball.x, initial_x)
        self.assertNotEqual(self.ball.y, initial_y)

    def test_bounce(self):
        initial_direction = self.ball.direction
        self.ball.bounce()
        self.assertNotEqual(self.ball.direction, initial_direction)

    def test_reset(self):
        self.ball.move()
        self.ball.reset()
        self.assertEqual(self.ball.x, SCREEN_WIDTH // 2)
        self.assertEqual(self.ball.y, SCREEN_HEIGHT // 2)

if __name__ == '__main__':
    unittest.main()