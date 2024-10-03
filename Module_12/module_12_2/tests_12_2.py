import unittest

from Module_12.module_12_2.runner_2 import Tournament, Runner


IS_FROZEN = True

@unittest.skipIf(IS_FROZEN, "Тесты в этом кейсе заморожены")
class TournamentTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner_1 = Runner("Уссейн", 10)
        self.runner_2 = Runner("Андрей", 9)
        self.runner_3 = Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        for _, result in cls.all_results.items():
            print(result)

    def testTournamentFastestSlowest(self):
        self.tournament = Tournament(
            90,
            self.runner_1, self.runner_3
        )

        self.all_results["testTournamentFastestSlowest"] = (self.tournament.start())

        self.assertTrue(self.all_results["testTournamentFastestSlowest"][2] == self.runner_3)


    def testTournamentMiddleSlowest(self):
        self.tournament = Tournament(
            90,
            self.runner_2, self.runner_3
        )

        self.all_results["testTournamentMiddleSlowest"] = (self.tournament.start())

        self.assertTrue(self.all_results["testTournamentMiddleSlowest"][2] == self.runner_3)

    def testTournamentThreeRunners(self):
        self.tournament = Tournament(
            90,
            self.runner_1, self.runner_2, self.runner_3
        )

        self.all_results["testTournamentThreeRunners"] = (self.tournament.start())

        self.assertTrue(self.all_results["testTournamentThreeRunners"][3] == self.runner_3)

    def testTournamentThreeRunnersRandom(self):
        self.tournament = Tournament(
            90,
            self.runner_3, self.runner_1, self.runner_2
        )

        self.all_results["testTournamentThreeRunnersRandom"] = (self.tournament.start())

        self.assertTrue(self.all_results["testTournamentThreeRunnersRandom"][3] == self.runner_3)


if __name__ == '__main__':
    unittest.main()