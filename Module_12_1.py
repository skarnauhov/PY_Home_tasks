import unittest
from rt_with_exceptions import Runner


class RunnerTest(unittest.TestCase):

    def test_walk(self):
        runner_1 = Runner('Петя')
        for _ in range(10):
            runner_1.walk()
        self.assertEqual(runner_1.distance, 50)

    def test_run(self):
        runner_2 = Runner('Петя')
        for _ in range(10):
            runner_2.run()
        self.assertEqual(runner_2.distance, 100)

    def test_challenge(self):
        runner_3 = Runner('Лёша')
        runner_4 = Runner('Саша')
        for _ in range(10):
            runner_3.walk()
        for _ in range(10):
            runner_4.run()
        self.assertNotEqual(runner_3.distance, runner_4.distance)


if __name__ == '__main__':
    unittest.main()
