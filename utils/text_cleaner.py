import re
import nltk

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer


# Download required data (first time)
nltk.download("stopwords")
nltk.download("wordnet")


lemmatizer = WordNetLemmatizer()


def clean_text(text):

    # convert to lowercase
    text = text.lower()


    # remove special characters
    text = re.sub(
        r"[^a-zA-Z ]",
        " ",
        text
    )


    # split words
    words = text.split()


    # remove stopwords
    stop_words = set(stopwords.words("english"))

    words = [
        word for word in words
        if word not in stop_words
    ]


    # lemmatization
    words = [
        lemmatizer.lemmatize(word)
        for word in words
    ]


    return " ".join(words)