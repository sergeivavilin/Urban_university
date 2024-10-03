import unittest

from Module_12.module_12_1.tests_12_1 import RunnerTests
from Module_12.module_12_2.tests_12_2 import TournamentTests


tournamentTS = unittest.TestSuite()
tournamentTS.addTests(unittest.makeSuite(RunnerTests))  # Устаревший метод
tournamentTS.addTests(unittest.TestLoader().loadTestsFromTestCase(TournamentTests))  #

test_runner = unittest.TextTestRunner(verbosity=2)
test_runner.run(tournamentTS)