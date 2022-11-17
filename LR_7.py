from random import randint


def generate_input():
    n = randint(3, 3)
    m = randint(2, 2)
    ls = [randint(0, n - 1) for _ in range(n)]
    lo = [randint(0, m - 1) for _ in range(m)]
    A = [[0 for _ in range(n)] for _ in range(m)]

    return write_rights_A(A, ls, lo), ls, lo, n, m


def write_rights_A(A, n, m):
    rwox = []
    for i in range(n):
        for j in range(m):
            rwox = [randint(0, 1), randint(0, 1), randint(0, 1), randint(0, 1)]
            A[j][i] = rwox
    return A


class The_Harrison_Ruzzo_Ullman:

    def __init__(self, n, m, A, ls, lo):
        self.n = n
        self.m = m
        self.A = A
        self.ls = ls
        self.lo = lo

    def create_o(self):
        pass

    def create_s(self):
        pass

    def destroy_o(self):
        pass

    def destroy_s(self):
        pass

    def enter_p_in_A(self):
        pass

    def delete_p_from_A(self):
        pass

    def make_move(self):
        pass


if __name__ == '__main__':
    A, ls, lo, n, m = generate_input()
    print(A)
    print(ls)
    print(lo)
    print(n)
    print(m)
