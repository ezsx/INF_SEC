alphabet = "abcdefghijklmnopqrstuvwxyz".upper()


# генерируем перестановочные строки
def permut_str(N):
    return list(set(alphabet[:N]))


# все почти перестановочные строки для перестановочной строки
def all_almost_permut_str(l_str):
    res = []
    for i in range(0, len(l_str) + 1):  # catch index
        for j in l_str:  # catch element
            ob = l_str[:i] + [j] + l_str[i:]
            if ob not in res:
                res.append(ob)

    return res  # [ bba -bba bab aba baa -baa ]


def sub_sets(N, str):
    subs_list = []
    for i in range(0, len(str) - N + 1):
        subs_list.append(str[i:N + i])
    return subs_list


if __name__ == '__main__':

    from itertools import permutations

    from random import randint, choice

    # N = randint(3, 7)
    #
    # p_r = permut_str(N)
    # # какое же питон вообще то волшебное говно
    # p_r2 = [z for z in choice([j for j in permutations(p_r)])]

    count = 0
    # test

    p_r = ['A', 'B', 'C']
    p_r2 = ['A', 'C', 'B']
    N = 3
    print(f"str_1: {p_r} , str_2: {p_r2}")

    # строим все перестановки данных двух строк
    # N = randint(len(p_r)-2, len(p_r2))
    all_subsets = sub_sets(N, p_r) + sub_sets(N, p_r2)
    print(all_subsets)
    from itertools import combinations

    all_subsets = [i for i in combinations(all_subsets, 2)]
    new_all_subsets = [i[0] + i[1] for i in all_subsets]
    print(new_all_subsets)

    print(new_all_subsets)

    for i in new_all_subsets:

        # превращаем полученную тапл перестановку в список
        lst = [j for j in i]
        print(f"{count} перестановка: {lst}")
        # создаем для потенциальной гипер перестановочной строки все подстроки длины N+1
        all_subs_N_1 = sub_sets(len(p_r) + 1, lst)
        # создаем для перестановочной строки все почти перестановочные строки
        aap = all_almost_permut_str(p_r) + all_almost_permut_str(p_r2)
        print(f"все подстроки N+1: {all_subs_N_1}")
        print(f"все почти перестановочные строки, строк str_1 и str_2: {aap}")
        check = False
        # ищем все подстроки длины N+1 гипер перестановочной строки
        # в почти перестановочных строках перестановочной строки длины N
        for i in all_subs_N_1:
            if i not in aap:
                break
            check = True

        if check:
            print(f"искомая кратчайшая гипер почти перестановочная строка: {lst}")
            break
        count += 1

# просто полнейший бред собаки, что это вообще за условие кому это вообще нужно
#
