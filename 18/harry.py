import os
import urllib.request
import re

# data provided
tmp = os.getenv("TMP", "/tmp")
stopwords_file = os.path.join(tmp, "stopwords")
harry_text = os.path.join(tmp, "harry")
urllib.request.urlretrieve(
    "https://bites-data.s3.us-east-2.amazonaws.com/stopwords.txt", stopwords_file
)
urllib.request.urlretrieve(
    "https://bites-data.s3.us-east-2.amazonaws.com/harry.txt", harry_text
)


def get_harry_most_common_word():
    text = open(harry_text, encoding="utf-8").read()
    stopwords = open(stopwords_file).read().split("\n")
    words = re.split(" |\n", text)
    words = [word.lower() for word in words]
    words = [re.sub("[^a-z]", "", word) for word in words]
    text_no_stop = [word for word in words if word not in stopwords]
    freq_word = max(set(text_no_stop), key=text_no_stop.count)
    return (freq_word, words.count(freq_word))
