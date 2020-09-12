from flask import Flask,url_for,render_template,request

# NLP Pkg
from spacy_summarization import text_summarizer #this text_summarizer is the function name on the spazy_summarization file
# Other Pkgs
import spacy
nlp = spacy.load('en')
# not adding web scrapping pkgs because we aren't going to use the document feature

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['GET','POST'])
def analyze():
    if request.method == 'POST':
        rawtext = request.form['rawtext']
        # Summarization
        final_summary = text_summarizer(rawtext) #rawtext is going to be given from our function in the python codes
        # ReadingTime
        #we dont care about reading time
    return render_template('index.html',final_summary=final_summary)


if __name__ == '__main__':
    app.run(debug=True)