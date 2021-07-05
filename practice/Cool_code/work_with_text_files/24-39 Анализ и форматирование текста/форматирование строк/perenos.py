def perenos(line, k):
    while len(line) > k:
        words = line.split()
        words_count = len(words)
        while len(" ".join(words[:words_count])) > k:
            words_count -= 1
        print(" ".join(words[:words_count]))
        line = " ".join(words[words_count:])
    print(" ".join(words[words_count:]))


line = 'Now that you have downloaded Postgres, get started using it'
perenos(line, 20)
