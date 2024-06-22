# read = open('list.txt', 'r', encoding='utf-8')
# counts = dict()
# for line in read:
#     words = line.split()
# for word in words:
#     counts[word] = counts.get(word, 0) + 1
# print(counts)
#
# read.close()
name = input('Enter file:')
handle = open(name, encoding='utf-8')

counts = dict()
for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

bigcount = None
bigword = None
for word, count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print(bigword, bigcount)