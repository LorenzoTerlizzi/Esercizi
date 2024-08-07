from multiprocessing import Process
import time


def sleep():

    print("Sono nella funzione")

    time.sleep(1)

    print(f"Sta uscendo dalla funzione")

if __name__ == "__main__":


    tic = time.time()

    t1 = Process(target= sleep)
    t2 = Process(target= sleep)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    toc: float = time.time()
    time_elapsed: float = toc - tic

    print(f"{time_elapsed=}")