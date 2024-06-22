import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

def extract_keywords(text):
    words = word_tokenize(text.lower())
    stop_words = set(stopwords.words('english'))
    filtered_words = [word for word in words if word not in stop_words]
    tagged_words = nltk.pos_tag(filtered_words)
    keywords = [word for word, pos in tagged_words if pos.startswith('NN')]
    return keywords

def generate_line_with_keywords(input_text):
    keywords = extract_keywords(input_text)
    for keyword in keywords:
        if keyword != "generate":
            t = (f"Generate a mermaid code for the making of {input_text.split('of')[-1].strip()} in a well defined and structured form and the flowchart should be user friendly.")
            break
    return t


