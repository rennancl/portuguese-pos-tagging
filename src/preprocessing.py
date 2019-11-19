def processFile(filename):
    lines = [line.rstrip('\n') for line in open(filename)]
    train_sentences = []
    train_tags = []
    for line in lines:
        train_sentences.append([token.split("_")[0] for token in line.split(" ")])
        train_tags.append([token.split("_")[1] for token in line.split(" ")])

    return train_sentences, train_tags

def getVocabAndClasses(train_sentences, train_tags):    
    vocab = set([word.lower() for s in train_sentences for word in s ])
    tags = set([tag for tags in train_tags for tag in tags])
    return vocab, tags

def wordsToInt():
    train_sentences, train_tags = processFile("../dataset/macmorpho-train.txt")
    test_sentences, test_tags = processFile("../dataset/macmorpho-test.txt")

    vocab, tags = getVocabAndClasses(train_sentences, train_tags )

    word2index = {w: i + 2 for i, w in enumerate(list(vocab))}
    word2index['PAD'] = 0  # padding
    word2index['OOV'] = 1  # out of vocab

    tag2index = {t: i + 1 for i, t in enumerate(list(tags))}
    tag2index['PAD'] = 0  #  padding

    train_sentences = [[word2index[elem.lower()] for elem in s] for s in train_sentences]
    train_tags = [[tag2index[elem] for elem in s] for s in train_tags]
    test_sentences = [[word2index[elem.lower()] if elem.lower() in word2index else 1 for elem in s] for s in test_sentences]
    test_tags = [[tag2index[elem] for elem in s] for s in test_tags]

wordsToInt()