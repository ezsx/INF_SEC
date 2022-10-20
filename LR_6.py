from random import randint


def generate_input(random):
    n = randint(3, 3)
    m = randint(2, 2)
    ls = [randint(0, n-1) for _ in range(n)]
    lo = [randint(0, m-1) for _ in range(m)]
    A = [[0 for _ in range(n)] for _ in range(m)]
    if random:
        return write_rights_A(A, n, m), ls, lo, n, m
    else:
        return write_correct_rights_A(A, ls, lo, n, m), ls, lo, n, m


def write_correct_rights_A(A, ls, lo, n, m):
    for i in range(n):
        for j in range(m):
            rw = [0, 0]
            if ls[i] > lo[j]:
                rw[0] = 1
            if ls[i] < lo[j]:
                rw[1] = 1
            A[j][i] = rw
    return A


def write_rights_A(A, n, m):
    for i in range(n):
        for j in range(m):
            rw = [randint(0, 1), randint(0, 1)]
            A[j][i] = rw
    return A


class Bell_LaPadula_criterion:
    def __init__(self, n, m, A, ls, lo):
        self.n = n
        self.m = m
        self.A = A
        self.ls = ls
        self.lo = lo

    def check_rights(self):
        for i in range(self.n):
            for j in range(self.m):
                if self.A[j][i][0] == 1 and self.A[j][i][1] == 1:
                    return False
        return True


def create_ls_lo(A, n, m):
    ls = [0 for _ in range(n)]
    lo = [0 for _ in range(m)]
    for i in range(n):
        for j in range(m):
            if A[j][i][0] == 1:
                ls[i] += 1
            if A[j][i][1] == 1:
                lo[j] += 1
    return ls, lo


if __name__ == '__main__':
    A, ls, lo, n, m = generate_input(False)
    B = Bell_LaPadula_criterion(n, m, A, ls, lo)
    [print(i) for i in A]
    print(ls)
    print(lo)
    print(B.check_rights())

    P = create_ls_lo(A, n, m)
    [print(i) for i in P]
