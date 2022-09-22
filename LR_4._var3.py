class Network_member():
    NM_list = []
    Comp_list = []

    def __init__(self, id: int, points: tuple):
        self.id = id
        self.points = points
        Network_member.NM_list.append(self)

    def __str__(self):
        return f"ID: {self.id}, points: {self.points}, compatibility: {self.compatibility}"

    @classmethod
    def generate_compatibility(cls):
        for i in cls.NM_list:
            for j in cls.NM_list[cls.NM_list.index(i) + 1:]:
                a1, b1, c1 = i.points
                a2, b2, c2 = j.points
                ap, bp, cp = abs(a1 - a2), abs(b1 - b2), abs(c1 - c2)

                if ap == 0 and (bp != 0 and cp != 0) and (bp or cp) != 0:
                    cls.Comp_list.append(("a", (i.id, j.id)))
                if bp == 0 and (ap != 0 and cp != 0) and (ap or cp) != 0:
                    cls.Comp_list.append(("b", (i.id, j.id)))
                if cp == 0 and (bp != 0 and ap != 0) and (bp or ap) != 0:
                    cls.Comp_list.append(("c", (i.id, j.id)))
                else:
                    cls.Comp_list.append((None, (i.id, j.id)))


if __name__ == '__main__':
    test_input1 = [
        [1, (1, 2, 3)],
        [2, (1, 4, 5)],
        [3, (1, 2, 4)]
    ]
    test_input2 = [
        [1, (100, 100, 100)],
        [2, (100, 100, 100)],
        [3, (100, 99, 99)],
        [4, (99, 99, 100)],
    ]
    for i in test_input2:
        Network_member(i[0], i[1])
    Network_member.generate_compatibility()
    count = 0
    for i in Network_member.Comp_list:
        print(i)
        if i[0] is not None:
            count += 1
    print(count)
