from collections import Counter
from nltk.util import ngrams


def get_bag_of_words(lemmatized_file):
    """
    Применять к файлам без фраз: ...lemma_minus_stopwords.txt
    :param lemmatized_file
    :return: bag_of_words_out (список кортежей)
    """

    file = open(lemmatized_file, encoding="utf8")
    lemmatized_all = []

    for line in file.readlines():
        post = line.split()
        for token in post:
            if token not in ('который', 'это', 'свой', 'весь', 'самый', 'также', 'наш', 'мочь', 'несколько', 'то_число', 'во_время', 'первый', 'второй', 'третий'):
                lemmatized_all.append(token)

    bag_of_words = Counter(sorted(lemmatized_all))
    lst = []
    for word, count in sorted(bag_of_words.items(), key=lambda x: x[1], reverse=True):
        item_temp = str(word), int(count)
        lst.append(item_temp)

    nums = list(range(1, len(lst) + 1))
    itog = list(zip(nums, lst))
    bag_of_words_out = []
    for i in itog:
        new = (i[0], *i[1])
        bag_of_words_out.append(new)

    return bag_of_words_out


def bag_of_words_to_file(lemmatized_phrased_file):
    """
    По отдельности эту функцию лучше вызывать для файлов ...lemma_phrases_no_sw.txt,
    так как в них частотные биграммы объединены во фразы.
    Записывает результат в файл bag_of_words
    :param lemmatized_phrased_file
    """

    with open('Files/bag_of_words.txt', "w", encoding="utf8") as output_file:
        to_file = get_bag_of_words(lemmatized_phrased_file)

        for i in to_file:
            output_file.write(str(i))
            output_file.write('\n')


bag_of_words_to_file('Files/ria_after_lemma_phrases_no_sw.txt')


def trigrams_fo_file(lemmatized_file):
    """
    Записывает результат в файл 3-grams, использовать для файлов ...lemma_minus_stopwords.txt
    :param lemmatized_file
    """
    file = open(lemmatized_file, encoding="utf8")
    lemmatized_all = []
    for line in file.readlines():
        post = line.split()
        for token in post:
            lemmatized_all.append(token)

    trigrams = ngrams(lemmatized_all, 3)
    trigrams_frequency = Counter(trigrams)

    with open('Files/3-grams.txt', "w", encoding="utf8") as output_file:
        trigrams_list = trigrams_frequency.most_common(1000)
        for i in trigrams_list:
            if i[1] > 1:
                output_file.write(f'{i[0][0]} {i[0][1]} {i[0][2]}: {i[1]}')
                output_file.write('\n')


trigrams_fo_file('Files/ria_after_lemma_minus_stopwords.txt')


def get_bigrams(lemmatized_file):
    """
    Передавать аргументом функции имя файла ...lemma_minus_stopwords.txt
    :param lemmatized_file
    """
    file = open(lemmatized_file, encoding="utf8")
    lemmatized_all = []
    for line in file.readlines():
        post = line.split()
        for token in post:
            lemmatized_all.append(token)

    bigrams = ngrams(lemmatized_all, 2)
    bigrams_frequency = Counter(bigrams)

    bigrams_list = []
    for bigram, count in sorted(bigrams_frequency.items(), key=lambda x: x[1], reverse=True):
        item = '_'.join(bigram), int(count)
        bigrams_list.append(item)

    nums = list(range(1, len(bigrams_list) + 1))
    itog = list(zip(nums, bigrams_list))
    bigrams_out = []
    for i in itog:
        new = (i[0], *i[1])
        bigrams_out.append(new)

    return bigrams_out


def bigrams_to_file(lemmatized_file):
    """
    Функция записывает в файл список кортежей (позиция, биграмма, абс.частота).
    """
    with open('Files/bigrams.txt', "w", encoding="utf8") as output_file:
        to_file = get_bigrams(lemmatized_file)
        for i in to_file:
            output_file.write(str(i))
            output_file.write('\n')


bigrams_to_file('Files/ria_after_lemma_minus_stopwords.txt')


def get_unigram_difference_0(file_1, file_2):
    """
    Записывает в файл difference_unigrams_0.txt униграммы, присутствующие в файле 1 и отсутствующие в файле 2
    """
    bow_1 = get_bag_of_words(file_1)
    bow_2 = get_bag_of_words(file_2)
    dict_1 = {}
    for i in bow_1:
        dict_1[i[1]] = i[0], i[2]
    dict_2 = {}
    for i in bow_2:
        dict_2[i[1]] = i[0], i[2]

    list_difference = []
    with open('Files/difference_unigrams_0.txt', "w", encoding="utf8") as output_file:
        for key, value in dict_1.items():
            if key not in dict_2.keys() and value[1] >= 2:
                item = [key, value[0], value[1]]
                list_difference.append(item)
                output_file.write(str(item))
                output_file.write('\n')

    return list_difference


get_unigram_difference_0('Files/ria_after_lemma_minus_stopwords.txt', 'Files/ria_before_lemma_minus_stopwords.txt')


def get_bigram_difference_0(file_1, file_2):
    """
    Записывает в файл difference_bigrams_0.txt биграммы, присутствующие в файле 1 и отсутствующие в файле 2
    """
    bi_1 = get_bigrams(file_1)
    bi_2 = get_bigrams(file_2)
    dict_1 = {}
    for i in bi_1:
        dict_1[i[1]] = i[0], i[2]
    dict_2 = {}
    for i in bi_2:
        dict_2[i[1]] = i[0], i[2]

    list_difference = []
    with open('Files/difference_bigrams_0.txt', "w", encoding="utf8") as output_file:
        for key, value in dict_1.items():
            if key not in dict_2.keys() and value[1] >= 2:
                item = [key, value[0], value[1]]
                list_difference.append(item)
                output_file.write(str(item))
                output_file.write('\n')

    return list_difference


get_bigram_difference_0('Files/ria_after_lemma_minus_stopwords.txt', 'Files/ria_before_lemma_minus_stopwords.txt')


def get_difference_uni(file_1, file_2, distance=500, position=500):
    """
    Выводит униграммы с наибольшей разницей в частотности между корпусом 1 и корпусом 2 (по убыванию разности).
    Формат вывода: кортеж (униграмма, позиция частотности в корпусе 1, позиция частотности в корпусе 2)
    """
    bow_1 = get_bag_of_words(file_1)
    dict_1 = {}
    for i in bow_1:
        dict_1[i[1]] = i[0], i[2]
    bow_2 = get_bag_of_words(file_2)
    dict_2 = {}
    for i in bow_2:
        dict_2[i[1]] = i[0], i[2]

    list_difference = []
    for word, value in dict_1.items():
        if word in dict_2.keys():
            if abs(dict_2[word][0] - dict_1[word][0]) >= distance:
                if dict_1[word][0] <= position or dict_2[word][0] <= position:
                    res = [word, dict_1[word][0], dict_2[word][0]]
                    list_difference.append(res)
    list_difference.sort(key=lambda item: abs(item[1] - item[2]), reverse=True)

    with open('Files/difference_unigrams.txt', "w", encoding="utf8") as output_file:
        for i in list_difference:
            output_file.write(str(i))
            output_file.write('\n')

    return list_difference


get_difference_uni('Files/ria_after_lemma_minus_stopwords.txt', 'Files/ria_before_lemma_minus_stopwords.txt')


def get_difference_bi(file_1, file_2, distance=500, position=250):
    """
    То же, что get_difference_uni, но для биграмм
    """
    bi_1 = get_bigrams(file_1)
    dict_1 = {}
    for i in bi_1:
        dict_1[i[1]] = i[0], i[2]
    bi_2 = get_bigrams(file_2)
    dict_2 = {}
    for i in bi_2:
        dict_2[i[1]] = i[0], i[2]

    list_difference = []
    for word, value in dict_1.items():
        if word in dict_2.keys():
            if abs(dict_2[word][0] - dict_1[word][0]) >= distance and (dict_1[word][0] <= position or dict_2[word][0] <= position):
                res = [word, dict_1[word][0], dict_2[word][0]]
                list_difference.append(res)
    list_difference.sort(key=lambda item: abs(item[1] - item[2]), reverse=True)

    with open('Files/difference_bigrams.txt', "w", encoding="utf8") as output_file:
        for i in list_difference:
            output_file.write(str(i))
            output_file.write('\n')

    return list_difference


get_difference_bi('Files/ria_after_lemma_minus_stopwords.txt', 'Files/ria_before_lemma_minus_stopwords.txt')

def lemma_portrait(lemma, file_context):
    print('----------------')
    print(f'лемма: {lemma}')
    bow_mdz_after = get_bag_of_words('Files/mdz_after_lemma_minus_stopwords.txt')
    for i in bow_mdz_after:
        if i[1] == str(lemma):
            print(f'корпус: mdz_after, позиция {i[0]}, tokens per million: {round((i[2] * 1000000 / 2778768), 2)}')

    bow_ria_after = get_bag_of_words('Files/ria_after_lemma_minus_stopwords.txt')
    for i in bow_ria_after:
        if i[1] == str(lemma):
            print(f'корпус: ria_after, позиция {i[0]}, tokens per million: {round((i[2] * 1000000 / 1590131), 2)}')

    bow_mdz_before = get_bag_of_words('Files/mdz_before_lemma_minus_stopwords.txt')
    for i in bow_mdz_before:
        if i[1] == str(lemma):
            print(f'корпус: mdz_before, позиция {i[0]}, tokens per million: {round((i[2] * 1000000 / 973104), 2)}')

    bow_ria_before = get_bag_of_words('Files/ria_before_lemma_minus_stopwords.txt')
    for i in bow_ria_before:
        if i[1] == str(lemma):
            print(f'корпус: ria_before, позиция {i[0]}, tokens per million: {round((i[2] * 1000000 / 2013471), 2)}')

    print('\ncontext corpus: ria_after')
    file = open(file_context, encoding="utf8")
    for line in file.readlines():
        if lemma in line:
            print(line, end='')

lemma_portrait('феминизм', 'Files/ria_after_lemma.txt')


def bigram_portrait(bigram, file_context):
    print('----------------')
    print(f'биграмма: {bigram}')

    bigr_mdz_after = get_bigrams('Files/mdz_after_lemma.txt')
    for i in bigr_mdz_after:
        if i[1] == str(bigram):
            print(f'корпус: mdz_after, позиция: {i[0]}, tokens per million: {round((i[2] * 1000000 / 2778768), 2)}')

    bigr_ria_after = get_bigrams('Files/ria_after_lemma.txt')
    for i in bigr_ria_after:
        if i[1] == str(bigram):
            print(f'корпус: ria_after, позиция: {i[0]}, tokens per million: {round((i[2] * 1000000 / 1590131), 2)}')

    bigr_mdz_before = get_bigrams('Files/mdz_before_lemma.txt')
    for i in bigr_mdz_before:
        if i[1] == str(bigram):
            print(f'корпус: mdz_before, позиция: {i[0]}, tokens per million: {round((i[2] * 1000000 / 973104), 2)}')

    bigr_ria_before = get_bigrams('Files/ria_before_lemma.txt')
    for i in bigr_ria_before:
        if i[1] == str(bigram):
            print(f'корпус: ria_before, позиция: {i[0]}, tokens per million: {round((i[2] * 1000000 / 2013471), 2)}')

    print('\ncontext corpus: ria_after')
    file = open(file_context, encoding="utf8")
    for line in file.readlines():
        if bigram.replace('_', ' ') in line:
            print(line, end='')


bigram_portrait('честный_выборы', 'Files/ria_after_lemma_minus_stopwords.txt')
