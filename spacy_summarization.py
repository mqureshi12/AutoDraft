import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from heapq import nlargest


#Defining the type of model and the stopwords of the paragraphs
nlp = spacy.load("en_core_web_sm")
stopwords = list(STOP_WORDS)

#documment1 = """Machine learning (ML) is the scientific study of algorithms and statistical models that computer systems use to progressively improve their performance on a specific task. Machine learning algorithms build a mathematical model of sample data, known as "training data", in order to make predictions or decisions without being explicitly programmed to perform the task. Machine learning algorithms are used in the applications of email filtering, detection of network intruders, and computer vision, where it is infeasible to develop an algorithm of specific instructions for performing the task. Machine learning is closely related to computational statistics, which focuses on making predictions using computers. The study of mathematical optimization delivers methods, theory and application domains to the field of machine learning. Data mining is a field of study within machine learning, and focuses on exploratory data analysis through unsupervised learning.In its application across business problems, machine learning is also referred to as predictive analytics."""

#document2 = """Our Father who art in heaven, hallowed be thy name. Thy kingdom come. Thy will be done, on earth as it is in heaven. Give us this day our daily bread; and forgive us our trespasses, as we forgive those who trespass against us; and lead us not into temptation, but deliver us from evil"""

#docx = nlp(documment1)

#for token in docx:
    #print(token.text)

def text_summarizer(raw_docx, summary_level = 5):

    """
    Function that summarizes a text and keeps the most important points.

    Inputs: - raw_docx = string variable that represents the document content that will be summarized.
            - summary_level = integer value that represents how summarized the document needs to be.
                              small input means not very summarized and large input means very summarized.
    """

    raw_text = raw_docx #string that will be summarized
    docx = nlp(raw_text) #string that will be run through the nlp model

    word_frequencies = freq_calc(docx)

    summarized_sents = sentence_calc(docx, word_frequencies, summary_level)

    #makes the final paragraph into a string and prints it
    final_par = [w.text for w in summarized_sents]

    summary = ' '.join(final_par)

    print(summary)

    return summary



def freq_calc(document):

    """
    Helper method that calculates the frequency of each word in the paragraph.

    Input: - document = string representation of the document that needs to be summarized.
    Output: - word_freq = dictionary of individual word frequency with word as key and frequency as value.
    """

    word_freq = {} #dictionary that will hold each word and its frequency value


    #adds the words to the dictionary and calculates each ones frequency
    for word in document:

        if word.text not in stopwords:

            if word.text not in word_freq.keys():
                word_freq[word.text] = 1
            else:
                word_freq[word.text] += 1

    #Calculate the level of importance of each word and return it
    maximum_freq = max(word_freq.values())

    for word in word_freq.keys():

        word_freq[word] = (word_freq[word] / maximum_freq)

    return word_freq


def sentence_calc(document, freq_of_words, level):

    """
    Helper function that determines the importance of each sentence in order to be included
    in the summary or not.

    Inputs: - document = string representation of the document that needs to be summarized.
            - freq_of_words = dictionary of individual word frequency with word as key and frequency as value.
            - level: integer value that represents how summarized the document needs to be.
                            small input means not very summarized and large input means very summarized.

    Output: - list of sentences that made it to the final summary based on the level.
    """

    sentence_list = [sentence for sentence in document.sents] #gets each sentence in the document

    sentence_scores = {} #dictionary that relates a sentence to its importance score

    for sent in sentence_list:

        for word in sent:

            if word.text.lower() in freq_of_words.keys():

                if len(sent.text.split(' ')) < 30:

                    #adds the sentences to the dictionary and also their score
                    if sent not in sentence_scores.keys():
                        sentence_scores[sent] = freq_of_words[word.text.lower()]
                    else:
                        sentence_scores[sent] += freq_of_words[word.text.lower()]

    #based on the score makes a list of the sentences that are above the level
    summarized_sentences = nlargest(level, sentence_scores, key = sentence_scores.get)

    return summarized_sentences


#text_summarizer(documment1, 7)