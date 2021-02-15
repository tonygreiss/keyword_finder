import re
import pandas as pd

subject = input("enter subject here:")

with open('description.txt', 'r') as file:
    text = file.read().replace('\n', '')

text_lower = text.lower()

bar_char = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

final_text = re.sub('[{}]'.format(bar_char), '', text_lower)

word_list = final_text.split()

## If I want to exclude specific words
'''
bad_words = ["to", "a", "and", "the", "as", "on", "that", "with", "for", "are", "of", "or", "an", "their", "in", "our", "we", "is", "you", "-", "us", "from"]

final_word_list = [word for word in word_list if word not in bad_words]
'''

final_word_list = [word for word in word_list]

d = {}

for word in final_word_list:
	d[word] = final_word_list.count(word)


for w in sorted(d, key=d.get, reverse=True):
    print(w, d[w])

df = pd.DataFrame(list(d.items()), columns=['word', 'count'])

df.to_csv("word_count_"+subject+".csv")