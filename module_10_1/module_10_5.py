from multiprocessing import Pool
import time
def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            if not line:
                break
            all_data.append(line)

#start_time = time.time()
#filenames = [f'./file {number}.txt' for number in range(1, 5)]
#for filename in filenames:
#    read_info(filename)
#print(end_time - start_time)

if __name__ == '__main__':
    start_time = time.time()
    filenames = [f'./file {number}.txt' for number in range(1, 5)]
    pool = Pool(4)
    pool.map(read_info, filenames)
    pool.close()
    pool.join()
    end_time = time.time()
    print(end_time - start_time)
