alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

test_text = "птолдывайуцлкои"

N = len(alphabet)

D = 2  # randint(0, N)  # коэфицент умножения для кодирования

C = 5  # randint(0, N)  # коэфицент прибавления для кодирования


# функция кодирования
def encode(x):
    # [0] - число со сдвигом, [1] - количество переполнений
    p1 = overflow(x * D)[0]
    p2 = overflow(p1 + C)[0]
    c1 = overflow(x * D)[1]
    c2 = overflow(p2)[1]
    return p2, c1, c2


# функция переполнения с учетом количества переполнений
def overflow(x):
    count = 0
    if x > N:
        while x > N:
            x -= N
            count += 1
        return x, count
    return x, count


# функция декодирования
def decode(x, c1, c2):
    if c1 == 0 and c2 == 0:
        return overflow_2(overflow_2(x - C)[0] // D)[0]
    for i in range(c1):
        x += N
    for i in range(c2):
        x += N
    x -= C
    x //= D
    return x


# функция переполнения в обратную сторону с учетом количества переполнений
# замечу overflow и owerflow_2 разделены для удобства
def overflow_2(x):
    count = 0
    if x < 1:
        while x < 1:
            x += N
            count += 1
        return x, count
    return x, count


class Thai_cipher:
    def __init__(self, alphabet, D, C, text):
        self.text = text
        self.alphabet_dict = self.make_dict(alphabet)
        self.alphabet = alphabet
        self.D = D
        self.C = C

    def text_number(self, text):
        text = [self.alphabet_dict[i] for i in text]
        return text

    def encode_light(self, text):
        text = [encode(self.alphabet_dict[i])[0] for i in text]
        return text

    def decode_light(self, text):
        text = [decode(i, 0, 0) for i in text]
        return text

    def encode_text(self, text):
        text = [[encode(self.alphabet_dict[i])[0], encode(self.alphabet_dict[i])[1], encode(self.alphabet_dict[i])[2]]
                for i in text]
        return text

    def decode_text(self, text):
        text = [decode(i[0], i[1], i[2]) for i in text]
        return text

    def check_coding(self, text, text2):
        if text == text2:
            return print("Кодирование прошло успешно")
        else:
            return print("Кодирование прошло НЕ успешно")

    def make_dict(self, text):
        d = {}
        for i in range(len(text)):
            d.update({text[i]: (i + 1)})
        return d

    def set_alphabet(self, alphabet):
        self.alphabet = alphabet
        self.alphabet_dict = self.make_dict(self.alphabet)

    def set_D(self, D):
        self.D = D

    def set_C(self, C):
        self.C = C


if __name__ == '__main__':
    # для удобства в качестве иероглифов используются буквы русского алфавита
    # в таком случае надо помнить что для успешного кодирования букв в тексте
    # должно быть меньше чем букв в алфавите и все они должны быть уникальны

    # может быть подключу в дальнейшем реквестом стягивание китайских иероглифов с сайта
    # их там много и они уникальны, но алгоритм уже реализован
    # да я в курсе что поля D и C в классе не нужны


    # создаем объект класса
    chiper = Thai_cipher(alphabet, D, C, test_text)
    # исходный текст
    print("test_text = ", chiper.text)
    # переводим текст в ключи алфавита
    print("test_text_number = ", chiper.text_number(chiper.text))
    # кодируем текст
    print("test_text_encode = ", chiper.encode_text(chiper.text))
    # декодируем текст
    print("test_text_decode = ", chiper.decode_text(chiper.encode_text(chiper.text)))
    # проверяем кодирование
    chiper.check_coding(chiper.text_number(chiper.text), chiper.decode_text(chiper.encode_text(chiper.text)))
    # проверяем кодирование в легком режиме (изначально предложенным в задании)
    print("test_text_encode_light = ", chiper.encode_light(chiper.text))
    print("test_text_decode_light = ", chiper.decode_light(chiper.encode_light(chiper.text)))
    chiper.check_coding(chiper.text_number(chiper.text), chiper.decode_light(chiper.encode_light(chiper.text)))
