class Worker:
    w_dict = dict()

    def __init__(self, id):
        self.id = id
        self.knowns = []
        self.called = False
        self.cnt_of_rel = 0
        self.was_counted = False
        Worker.w_dict[id] = self

    def __str__(self):
        return str(self.id) + " " + str(self.called) + " " + str(self.cnt_of_rel)

    def count_of_relation(self):
        if self.was_counted:
            return self.cnt_of_rel
        self.was_counted = True
        sum = 1
        for w in self.knowns:
            sum += w.count_of_relation()
        self.cnt_of_rel = sum
        return sum

    def make_call(self):
        self.called = True
        if len(self.knowns) == 0:
            return None
        m = max(self.knowns, key=lambda x: x.cnt_of_rel if not x.called else -1)
        if not m.called:
            m.called = True
            return m
        else:
            return None

    @classmethod
    def get(cls, id):
        w = cls.w_dict.get(id)
        if w is None:
            w = Worker(id)
            cls.w_dict[id] = w
        return w

    @classmethod
    def is_all_called(cls):
        for w in cls.w_dict.values():
            if not w.called:
                return False
        return True


def gen_input():
    from random import randint
    from random import choice
    # возможны кейсы с несвязанными графами нужно доработать
    n = [i for i in range(1, randint(5, 10) + 1)]  # [1,2,3,4,5,6,7,8,9]
    arr = []
    n.remove(1)
    arr.append([1] + list(set([choice(n) for _ in n])))  # [1,2,3,4,5,6,7,8,9]
    for i in n:
        s = n
        s.remove(i)
        arr.append([i] + list(set([choice(s) for _ in n])))
    return arr


def test_input():
    arr = [[1, 2, 5, 6, 7, 8],
           [2, 8, 6, 7],
           [3, 4],
           [4, 8, 5, 6, 7],
           [5],
           [6, 8, 3, 5],
           [7],
           [8, 3]]
    arr2 = [
        [1, 2, 3, 4],
        [2],
        [3, 5],
        [4, 6],
        [5, 7, 8, 9],
        [6, 8, 9],
        [7],
        [8],
        [9]
    ]
    return arr


def init_workers(arr):
    for i in arr:
        w = Worker.get(i[0])
        for j in i[1:]:
            w.knowns.append(Worker.get(j))


def show_workers():
    workers = list(Worker.w_dict.values())
    workers.sort(key=lambda x: x.count_of_relation(), reverse=True)
    for w in workers:
        print(w)


def run_all():
    # инициализируем количество тактов
    takt = 0
    # в список прозвонивших добавляем первого
    called = [Worker.get(1)]
    # инициализируем список связей под каждым узлом
    Worker.get(1).count_of_relation()
    # цикл пока всех не обзвонили
    while (not Worker.is_all_called()):
        takt += 1
        # список кому прозвоним в этот такт
        called_now = []
        # проходим по всем кому прозвонили к этому такту
        for w in called:
            # из списка тех что прозвонили иницируем звонок
            w_call = w.make_call()
            if w_call is not None:
                # тот кому дозвонились попадает в список прозвонивших
                called_now.append(w_call)
                # каждый звонок печатаем кто кому и номер такта
                print("call from {} to {}, takt - {}".format(w.id, w_call.id, takt))
        # увеличиваем количество тактов

        called += called_now
    # печатаем общее количество тактов
    print("total takt - {}".format(takt))


if __name__ == '__main__':
    # arr = gen_input()
    arr = test_input()
    init_workers(arr)
    run_all()
    show_workers()
