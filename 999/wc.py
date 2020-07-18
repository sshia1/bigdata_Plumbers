with open('stop.txt') as f:
    STOP_WORDS = frozenset(l.strip() for l in f if not l.isspace())

def mapper(_, v, writer):
    for word in v.split():
        if word in STOP_WORDS:
            writer.count("STOP_WORDS", 1)
      else:
          writer.emit(word, 1)

def reducer(word, icounts, writer):
    writer.emit(word, sum(map(int, icounts)))
