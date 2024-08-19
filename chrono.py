import time


class Chrono():
    def __init__(self):
        self.tempsDemmarage = time.time()

    def start(self):
        self.tempsDemmarage = time.time()

    def getChrono(self):
        return round(time.time() - self.tempsDemmarage, 2)
