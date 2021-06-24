"""удаление пробелов с момощью
регулярных выражений"""

import re

text = "а   роза   упала  на  лапу     азора   "

optimized_text = re.sub('\s+', ' ', text)

all_words = re.findall('\w+', text)

print(optimized_text)
print(all_words)
