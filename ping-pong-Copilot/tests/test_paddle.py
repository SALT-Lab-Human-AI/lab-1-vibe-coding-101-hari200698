import unittest
from src.paddle import Paddle
from src.ball import Ball

class TestPaddle(unittest.TestCase):

    def setUp(self):
        self.paddle = Paddle()
        self.ball = Ball()

    def test_move_up(self):
        initial_position = self.paddle.y
        self.paddle.move_up()
        self.assertLess(self.paddle.y, initial_position)

    def test_move_down(self):
        initial_position = self.paddle.y
        self.paddle.move_down()
        self.assertGreater(self.paddle.y, initial_position)

    def test_collision_with_ball(self):
        self.paddle.y = 100  # Set paddle position
        self.ball.y = 100    # Set ball position to collide
        self.ball.x = self.paddle.x  # Align ball with paddle
        self.assertTrue(self.paddle.check_collision(self.ball))

if __name__ == '__main__':
    unittest.main()