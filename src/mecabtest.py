import sys
import MeCab

#tagger = MeCab.Tagger ('-F\s%f[6] -U\s%f[6] -E\\n')
tagger = MeCab.Tagger ('-Owakati')

fi = open(sys.argv[1], 'r')
fo = open(sys.argv[2], 'w')

line = fi.readline()
while line:
  result = tagger.parse(line)
  fo.write(result[1:])
  line = fi.readline()

fi.close()
fo.close()
