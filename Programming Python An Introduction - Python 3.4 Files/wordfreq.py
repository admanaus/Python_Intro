# wordfreq.py
#   A simple progam that determins word frequency in a document, demonstrating
#   the use of a Pythin dictinary.

def byFreq(pair):
    return pair[1]

def main():
    print('This program analizes word frequency in a file')
    print('and prints out a report on the most frequent words.\n')

    # Get the sequence of words from the file
    fname = input('File to analize: ')
    text = open(fname, 'r').read()
    text = text.lower()
    for ch in '!@#$%^&*()-_=+[]{}\|;:",./<>?`~':
        text = text.replace(ch, ' ')
    words = text.split()

    # constructs a dictionay of word counts
    counts = {}
    for w in words:
        counts[w] = counts.get(w,0) + 1

    # output analysis of n most frequent words
    n = eval(input('Output analisis of how many words? '))
    items = list(counts.items())
    items.sort()
    items.sort(key=byFreq, reverse=True)
    for i in range(n):
        word, count = items[i]
        print("{0:<15}{1:>5}".format(word, count))

if __name__ == '__main__': main()
    
