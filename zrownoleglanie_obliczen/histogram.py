import random
import multiprocessing
import sys

def calculate_histogram_worker(part_data,data_range):
    part_histogram = [0]*(data_range + 1)
    for i in part_data:
        part_histogram[i] += 1
    return part_histogram

def calculate_histogram(data, data_range):
    cores = 4
    pool = multiprocessing.Pool(cores)
    workers = []
    part_len = int(len(data)/cores)
    for core in range(cores):
        part_data = data[core*part_len : ((core + 1)*part_len)]
        workers.append(pool.apply_async(calculate_histogram_worker,
                                        (part_data, data_range, )))

    histograms = []
    for worker in workers:
        while(1):
            try:
                histograms.append(worker.get(1))
                break
            except multiprocessing.context.TimeoutError:
                pass
            except KeyboardInterrupt: 
                print("terminating program")
                pool.terminate()
                pool.close()
                pool.join()
                raise KeyboardInterrupt
    pool.close()
    pool.join()

    histogram_final = [0]*(data_range + 1)
    for histogram in histograms:
        for i in range(len(histogram)):
            histogram_final[i] += histogram[i]
    return histogram_final

if __name__ == '__main__':
    random.seed()
    data_range = 10
    data = []

    for i in range(0,100):
        data.append(int(random.random()*data_range))

    histogram = calculate_histogram(data, data_range)
    print(histogram)
