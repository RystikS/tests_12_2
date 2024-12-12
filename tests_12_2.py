import unittest
from runner_and_tournament import *


class TournamentTest(unittest.TestCase):

    all_results = {}
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner_1 = Runner("Усэйн", 10)
        self.runner_2 = Runner("Андрей", 9)
        self.runner_3 = Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        pass


    def test_tour_1(self):
        tournament = Tournament(90, self.runner_1, self.runner_3)
        results = tournament.start()
        for runner_position in results.keys():
            winner_name = results[runner_position].name
            self.all_results[runner_position] = winner_name
        print(self.all_results)
        self.assertTrue(self.all_results[max(results.keys())] == "Ник")

    def test_tour_2(self):
        tournament = Tournament(90, self.runner_2, self.runner_3)
        results = tournament.start()
        for runner_position in results.keys():
            winner_name = results[runner_position].name
            self.all_results[runner_position] = winner_name
        print(self.all_results)
        self.assertTrue(self.all_results[max(results.keys())] == "Ник")

    def test_tour_3(self):
        tournament = Tournament(90, self.runner_1, self.runner_2, self.runner_3)
        results = tournament.start()
        for runner_position in results.keys():
            winner_name = results[runner_position].name
            self.all_results[runner_position] = winner_name
        print(self.all_results)
        self.assertTrue(self.all_results[max(results.keys())] == "Ник")


if __name__ == '__main__':
    unittest.main()
