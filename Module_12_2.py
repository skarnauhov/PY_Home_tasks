import unittest

from rt_with_exceptions import Runner, Tournament

# тесты не учитывают проверку бегунов с одинаковой скоростью,
# в этом случае первым будет тот, кто первый в списке


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner_1 = Runner('Усейн', 10)
        self.runner_2 = Runner('Андрей', 12)
        self.runner_3 = Runner('Ник', 3)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены.')
    def test_1_tournament(self):
        t1 = Tournament(90, self.runner_1, self.runner_3)
        self.all_results['test_1'] = t1.start()
        self.assertTrue(self.all_results['test_1'][len(self.all_results['test_1'])] == 'Ник')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены.')
    def test_2_tournament(self):
        t2 = Tournament(90, self.runner_2, self.runner_3)
        self.all_results['test_2'] = t2.start()
        self.assertTrue(self.all_results['test_2'][len(self.all_results['test_2'])] == 'Ник')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены.')
    def test_3_tournament(self):
        t3 = Tournament(90, self.runner_1, self.runner_2, self.runner_3)
        self.all_results['test_3'] = t3.start()
        self.assertTrue(self.all_results['test_3'][len(self.all_results['test_3'])] == 'Ник')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены.')
    def test_4_tournament(self):
        """
        данный тест сравнивает список бегунов полученный в результате работы метода start класса Tournament
        и список бегунов полученный в результате сортировки бегунов по атрибуту: скорость бегуна
        """
        t4 = Tournament(90, self.runner_3, self.runner_2, self.runner_1)
        self.all_results['test_4'] = t4.start()
        list_1 = list(self.all_results['test_4'].values())
        list_1_1 = []
        for i in range(len(list_1)):
            list_1_1.append(list_1[i].name)
        list_2 = list(dict(sorted(({self.runner_1.name: self.runner_1.speed,
                             self.runner_2.name: self.runner_2.speed,
                            self.runner_3.name: self.runner_3.speed}).items(), key=lambda item: item[1], reverse=True)).keys())
        self.assertTrue(list_1_1 == list_2)

    @classmethod
    def tearDownClass(cls):
        for key, value in cls.all_results.items():
            print(f'{key}: {value}')


if __name__ == '__main__':
    unittest.main()