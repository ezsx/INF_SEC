# генерируем перестановочные строки
def permut_str(N):
    return list(set(alphabet[:N]))


# все почти перестановочные строки для перестановочной строки
def all_almost_permut_str(l_str):
    res = []
    for i in range(0, len(l_str) + 1):  # catch index
        for j in l_str:                 # catch element
            ob = l_str[:i] + [j] + l_str[i:]
            if ob not in res:           # генерим с излишком но не включаем повторы
                res.append(ob)
    return res  # ab --> [ bba -bba bab aba baa -baa ]

#все подстроки длины N заданной строки
def sub_sets(N, str):
    subs_list = []
    for i in range(0, len(str) - N + 1):
        subs_list.append(str[i:N + i])
    return subs_list

#генерируем случайные входные данные строки
def random_input():
    from itertools import permutations
    from random import randint, choice
    N = randint(3, 7)
    p_r = permut_str(N)
    # какое же питон вообще то волшебное говно
    p_r2 = [z for z in choice([j for j in permutations(p_r)])]
    return p_r, p_r2, N


def main_alg(p_r, p_r2, N):
    # инициализируем счетчик шага
    count = 0

    # инициализируем список для хранения всех возможных гипер перестановочных строк
    all_possible_hyper_str = [p_r+p_r2]+[p_r2+p_r]+all_almost_permut_str(p_r+p_r2)+all_almost_permut_str(p_r2+p_r)
    print(all_possible_hyper_str)

    all_res = []

    for i in all_possible_hyper_str:
        # создаем для потенциальной гипер перестановочной строки все подстроки длины N+1
        all_subs_N_1 = sub_sets(N + 1, i)
        # создаем для перестановочной строки все почти перестановочные строки
        aap = all_almost_permut_str(p_r) + all_almost_permut_str(p_r2)

        print(f"{count} перестановка: {i}")
        print(f"все подстроки N+1: {all_subs_N_1}")
        print(f"все почти перестановочные строки, строк str_1 и str_2: {aap}")

        check = False
        # ищем все подстроки длины N+1 гипер перестановочной строки
        # в почти перестановочных строках перестановочной строки длины N
        for j in all_subs_N_1:
            if j not in aap:
                break
            check = True

        if check:
            print("check true")
            all_res.append(i)
        else:
            print("check false")
        count += 1
    print(all_res)
    print(f"искомая кратчайшая гипер почти перестановочная строка: {min(all_res, key=len)}")



if __name__ == '__main__':

    import time
    start_time = time.time()
    alphabet = "abcdefghijklmnopqrstuvwxyz".upper()
    p_r = ['A', 'B', 'C']
    p_r2 = ['A', 'C', 'B']
    N = 3
    # p_r, p_r2, N = random_input()
    main_alg(p_r, p_r2, N)
    print("--- %s seconds ---" % (time.time() - start_time))
    print(all_almost_permut_str(p_r), len(all_almost_permut_str(p_r)))

# просто полнейший бред собаки, что это вообще за условие кому это вообще нужно
