import unittest

from Module_12.module_12_1.runner import Runner


IS_FROZEN = False


@unittest.skipIf(IS_FROZEN, "Тесты в этом кейсе заморожены")
class RunnerTests(unittest.TestCase):
    def test_walk(self):
        runner_1 = Runner("test_runner_1")
        for i in range(10):
            runner_1.walk()
        self.assertEqual(runner_1.distance, 50)

    def test_run(self):
        runner_2 = Runner("test_runner_2")
        for i in range(10):
            runner_2.run()
        self.assertEqual(runner_2.distance, 100)

    def test_challenge(self):
        runner_3 = Runner("test_runner_3")
        runner_4 = Runner("test_runner_4")

        for i in range(10):
            runner_3.walk()
            runner_4.run()

        self.assertNotEqual(runner_3.distance, runner_4.distance)

if __name__ == '__main__':
    unittest.main()