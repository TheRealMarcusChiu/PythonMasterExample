import nltk
nltk.download('punkt')
from nltk.collocations import BigramCollocationFinder, BigramAssocMeasures, TrigramCollocationFinder

bi_dict = dict()
bg_measures = BigramAssocMeasures()
with open('text/text.txt', 'r') as file:
    text = file.read()
    table = str.maketrans(dict.fromkeys('0123456789'))
    textWithoutNumbers = text.translate(table)

    words = nltk.word_tokenize(textWithoutNumbers)

    bi_finder = BigramCollocationFinder.from_words(words, window_size=2)
    bigram_measures = nltk.collocations.BigramAssocMeasures()
    bi_finder.apply_freq_filter(2)
    t = bi_finder.ngram_fd.items()
    ngram = list(t)
    ngram.sort(key=lambda item: item[-1], reverse=False)
    for (k, v) in ngram:
        print(k, v)
    bi_finder.score_ngrams(bigram_measures.pmi)
    bi_collocs = bi_finder.nbest(bg_measures.likelihood_ratio, 10)
    print(bi_collocs)


    tri_finder = TrigramCollocationFinder.from_words(words)
    bi_finder.apply_freq_filter(5)
    t = tri_finder.ngram_fd.items()
    ngram = list(t)
    ngram.sort(key=lambda item: item[-1], reverse=False)
    for (k, v) in ngram:
        print(k, v)
