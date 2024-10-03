import unittest
import logging

from Module_12.module_12_4.rt_with_exceptions import Runner


logging.basicConfig(
    level=logging.INFO,
    filename="runner_tests.log",
    filemode="w",
    encoding="utf-8",
    format="%(asctime)s | %(levelname)s | %(message)s"
)
logger = logging.getLogger(__name__)


class RunnerTests(unittest.TestCase):

    def test_walk(self):
        try:
            runner_1 = Runner("Vasya", -1)
            for i in range(10):
                runner_1.walk()
            self.assertEqual(runner_1.distance, 50)
            logger.info("test_walk выполнен успешно")
        except TypeError:
            logger.warning(f"Неверный тип данных для объекта Runner", exc_info=True)
        except ValueError:
            logger.warning(f"Неверная скорость для Runner", exc_info=True)

    def test_run(self):
        try:
            runner_2 = Runner(-1)
            for i in range(10):
                runner_2.run()
            self.assertEqual(runner_2.distance, 100)
            logger.info("test_run выполнен успешно")
        except TypeError:
            logger.warning(f"Неверный тип данных для объекта Runner", exc_info=True)
        except ValueError:
            logger.warning(f"Неверная скорость для Runner", exc_info=True)

    def test_challenge(self):
        try:
            runner_3 = Runner("test_runner_3")
            runner_4 = Runner("test_runner_4")

            for i in range(10):
                runner_3.walk()
                runner_4.run()

            self.assertNotEqual(runner_3.distance, runner_4.distance)
            logger.info("test_challenge выполнен успешно")

        except TypeError:
            logger.warning(f"Неверный тип данных для объекта Runner", exc_info=True)
        except ValueError:
            logger.warning(f"Неверная скорость для Runner", exc_info=True)


if __name__ == '__main__':
    unittest.main(verbosity=2)
