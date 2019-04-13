import codecs
import sys

with codecs.open(sys.argv[1],"r","utf-8") as f:
  #for line in f.readlines():
  for line in f:
    chars = [c for c in line if c != u' ']
    with codecs.open(sys.argv[2], "a", "utf-8") as newf:
      newf.write(u' '.join(chars))
