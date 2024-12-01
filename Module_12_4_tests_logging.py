import unittest
from rt_with_exceptions import Runner
import logging


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены.')
    def test_walk(self):
        try:
            runner_1 = Runner('Петя', speed=-5)
            for _ in range(10):
                runner_1.walk()
            self.assertEqual(runner_1.distance, 50)
            logging.info('"test_walk" выполнен успешно')
        except ValueError as ve:
            logging.warning('Неверная скорость для Runner', exc_info=True)



    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены.')
    def test_run(self):
        try:
            runner_2 = Runner(1324)
            for _ in range(10):
                runner_2.run()
            self.assertEqual(runner_2.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except TypeError as te:
            logging.warning('Неверный тип данных для объекта Runner', exc_info=True)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены.')
    def test_challenge(self):
        runner_3 = Runner('Лёша')
        runner_4 = Runner('Саша')
        for _ in range(10):
            runner_3.walk()
        for _ in range(10):
            runner_4.run()
        self.assertNotEqual(runner_3.distance, runner_4.distance)


logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log',
                        encoding='utf-8', format="%(asctime)s | %(levelname)s | %(message)s")

if __name__ == '__main__':
    unittest.main()
