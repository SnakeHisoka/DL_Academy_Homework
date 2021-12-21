# Задание-1:
# Реализовать решение следующей задачи: 
# «Есть два писателя, которые по очереди в течении определенного времени (у каждого разное) 
# пишут в одну книгу. Данная книга очень популярна, у неё есть как минимум 3 фаната (читателя), 
# которые ждут не дождутся, чтобы прочитать новые записи из неё. Каждый читатель и писатель – 
# отдельный поток. Одновременно книгу может читать несколько читателей, но писать единовременно 
# может только один писатель.»


import threading
import random
import time

book = ''
mutex = threading.Lock()


def writing(timer, name):
    global book      
    mutex.acquire()
    for i in range(timer*2):        
        symbol = chr(random.randint(65,90)).lower()
        print(f'{name} пишет: {symbol}')
        book += symbol
        time.sleep(0.5)
    print(f'Книга содержит следующий текст:{book}')
    mutex.release()   


def reading(name, timer):
    while True:
        time.sleep(timer)
        print(f'{name} читает: {book}')


if __name__ == "__main__":
    def iter_writing(iter): 
        for i in range(iter):
            time_of_writing_writer1 = 1
            time_of_writing_writer2 = 2

            flow_writer1 = threading.Thread(target=writing, args=(time_of_writing_writer1,
                                                                 'Писатель_1'))   
            flow_writer2 = threading.Thread(target=writing, args=(time_of_writing_writer2, 
                                                                'Писатель_2'))
            reader1 = threading.Thread(target = reading, args = ('Читатель1', 3))
            reader2 = threading.Thread(target = reading, args = ('Читатель2', 5))
            reader3 = threading.Thread(target = reading, args = ('Читатель3', 2))

            reader1.daemon = True
            reader2.daemon = True
            reader3.daemon = True
        
            flow_writer1.start()
            flow_writer2.start()
            reader1.start()
            reader2.start()
            reader3.start()
            
            flow_writer1.join()
            flow_writer2.join()
            reader1.join(0)
            reader2.join(0)
            reader2.join(0)


    iteration_wr = 2
    iter_writing(iteration_wr)


#-------------------------------------------------------------------------------------
# Задание-2:
# «Пять безмолвных философов сидят вокруг круглого стола, перед каждым философом стоит 
# тарелка спагетти. Вилки лежат на столе между каждой парой ближайших философов. 
# Каждый философ может либо есть, либо размышлять. Прием пищи не ограничен количеством 
# оставшихся спагетти — подразумевается бесконечный запас. Тем не менее, философ может 
# есть только тогда, когда держит две вилки — взятую справа и слева (альтернативная 
# формулировка проблемы подразумевает миски с рисом и палочки для еды вместо тарелок 
# со спагетти и вилок). Каждый философ может взять ближайшую вилку (если она доступна) 
# или положить — если он уже держит её. Взятие каждой вилки и возвращение её на стол 
# являются раздельными действиями, которые должны выполняться одно за другим. Вопрос 
# задачи заключается в том, чтобы разработать модель поведения (параллельный алгоритм), 
# при котором ни один из философов не будет голодать, то есть будет вечно чередовать 
# приём пищи и размышления.»


import threading
import time


class acquire(object):
    def __init__(self, *locks):
        self.locks = sorted(locks, key=lambda x: id(x))

    def __enter__(self):
        for lock in self.locks:
            lock.acquire()

    def __exit__(self, ty, val, tb):
        for lock in reversed(self.locks):
            lock.release()
        return False


def phil(left, right):
    while True:
        with acquire(left,right):      
            time.sleep(0.5)  
            print(f'Философ {threading.currentThread()} ест.')


N_FORKS = 5
forks = [threading.Lock() for n in range(N_FORKS)]


phils = [threading.Thread(
    target=phil,
    args=(forks[n], forks[(n + 1) % N_FORKS])
) for n in range(N_FORKS)]


for p in phils:
    p.start()