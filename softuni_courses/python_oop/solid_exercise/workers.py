from abc import ABC, abstractmethod


class Work(ABC):
    @abstractmethod
    def work(self):
        pass


class Worker(Work):
    def work(self):
        print("I'm working!!")


class SuperWorker(Work):
    def work(self):
        print("I work very hard!!!")


class Manager:
    def __init__(self):
        self.worker = None

    def set_worker(self, work):
        assert isinstance(work, Work), f'`worker` must be of type {work}'

        self.worker = work

    def manage(self):
        if self.worker is not None:
            self.worker.work()


worker = Worker()
manager = Manager()
manager.set_worker(worker)
manager.manage()

super_worker = SuperWorker()
try:
    manager.set_worker(super_worker)
    manager.manage()
except AssertionError:
    print("manager fails to support super_worker....")
