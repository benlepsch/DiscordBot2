f = open('ns.txt').read().split('.')

# need to clear out all of the \ns hidden mid line

with open('sentences.txt', 'w+') as nf:
    for i in range(len(f)):
        nf.write(' '.join(f[i].split('\n')) + '\n')
