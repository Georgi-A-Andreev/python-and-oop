class Worker:

    def __init__(self, name, salary, energy):
        self.name = name
        self.salary = salary
        self.energy = energy
        self.money = 0

    def work(self):
        if self.energy <= 0:
            raise Exception('Not enough energy.')

        self.money += self.salary
        self.energy -= 1

    def rest(self):
        self.energy += 1

    def get_info(self):
        return f'{self.name} has saved {self.money} money.'


import unittest


class WorkerTests(unittest.TestCase):

    def test_initialization(self):
        worker = Worker('Gosho', 100, 10)
        self.assertEqual(worker.name, 'Gosho')
        self.assertEqual(worker.salary, 100)
        self.assertEqual(worker.energy, 10)
        self.assertEqual(worker.money, 0)

    def test_energy_is_incremented(self):
        worker = Worker('Gosho', 100, 10)
        worker.rest()
        self.assertEqual(worker.energy, 11)

    def test_if_error_if_negative_energy(self):
        worker = Worker('Gosho', 100, -10)
        with self.assertRaises(Exception) as context:
            worker.work()
        self.assertEqual(str(context.exception), 'Not enough energy.')

    def test_salary_increase_after_work(self):
        worker = Worker('Gosho', 100, 10)
        worker.work()
        self.assertEqual(worker.money, 100)

    def test_worker_energy_decrease_after_work(self):
        worker = Worker('Gosho', 100, 10)
        worker.work()
        self.assertEqual(worker.energy, 9)

    def test_get_info(self):
        worker = Worker('Gosho', 100, 10)
        self.assertEqual(worker.get_info(), 'Gosho has saved 0 money.')


if __name__ == '__main__':
    unittest.main()
