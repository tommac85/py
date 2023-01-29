#files.py
import sys
#aaa = sys.getdefaultencoding()
#print(aaa)
#f = open('wasteland.txt', mode='wt', encoding = 'utf-8)')
#mode='wt'
#mode 'r' open for reading
# 'w' open for writing
# 'a' open for appending
# 2 znak oznacza slector
# 'b' = binary mode
# 't' = text mode
# wt = open for writing in text mode
##f.write('what branches grow\n')
f = open(sys.argv[1], mode='rt', encoding='utf-8')
for line in f:
    sys.stdout.write(line)
f.close()