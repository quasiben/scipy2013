from disco.job import Job
from disco.core import result_iterator

class WordCount(Job):
    
    partitions = 3
    input = ['http://discoproject.org/media/text/chekhov.txt']
    
    @staticmethod
    def map(line, params):
        import string
        for word in line.split():
            strippedWord = word.translate(string.maketrans("",""), string.punctuation)
            yield strippedWord, 1

    @staticmethod
    def reduce(iter, params):
        from disco.util import kvgroup
        for word, counts in kvgroup(sorted(iter)):
            yield word, sum(counts)

if __name__ == "__main__":
    from disco_words import WordCount
    
    wordcount = WordCount().run()
    
    for (word, counts) in result_iterator(wordcount.wait(show=True)):
        print word, counts 
    