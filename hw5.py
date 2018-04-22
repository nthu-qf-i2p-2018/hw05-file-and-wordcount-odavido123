
# coding: utf-8

# In[ ]:


import csv, json, pickle, string

def main(filename):
    txtfile = open(filename)
    lines = txtfile.readlines()
    all_words = []

    for line in lines:
        words = line.split()

        for word in words:
            word = word.strip(string.punctuation)

            if word!=' ':
                all_words.append(word)

    from collections import Counter
    counter = Counter(all_words)

    with open("wordcount.csv", "w") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['word', 'count'])
        
        for i in list(all_words):
            writer.writerow([all_words[i], all_words.count(all_words[i])])

    with open("wordcount.json", "w") as json_file:
        json.dump(counter, json_file)

    pickle.dump(counter, open("wordcount.pkl", 'wb'))


if __name__ == '__main__':
    main("i_have_a_dream.txt")

