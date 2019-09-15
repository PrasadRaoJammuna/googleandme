from flask import Flask,request,render_template
from textblob import TextBlob,Word


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')
@app.route('/translate',methods=['POST'])
def translate():
    data=''
    e=''
    try:
        if request.method == "POST":
            #text = request.form.values()
            text = request.form['language']
            data = TextBlob(text).translate(to='en')
        #print(data)
    except:
        e = "Soory! I can't Understand it."

    return render_template('home.html',data ='Translated Text :{}'.format(data),e=e)

@app.route('/sentiment_analysis',methods=['POST'])
def sentiment_analysis():
    try:
        if request.method == "POST":
            #text = request.form.values()
            text = request.form['sent']
            analysis = TextBlob(text)
            score = analysis.sentiment.polarity
            #print(type(score))
            if score > 0:
                score = 'Hey, you are in Positive sentiment.'
            elif score <0:
                score='Oh.! why you are in negative mode.'
            else:
                score ='Hmm..! Ok, you are on the line Nutral.'
    except:
        e = "Soory! Please write a understandable review."
        print(e)

    return render_template('home.html',score=score)


@app.route('/definition',methods=['POST'])
def definition(text='hate'):
    e=''
    mean=[]
    try:
        if request.method == 'POST':
            text = request.form['mean']
            mean = Word(text).definitions
        else:
             e = 'Sorry, I dont have anything about this.'

            
    except:
        e = 'Sorry, I dont have anything about this.'
    return render_template('home.html',e=e,mean=mean[:5])


@app.route('/correct',methods=["POST"])
def correct():
    correct_Sentence=''
    e=''
    try:
        if request.method == 'POST':
            text = request.form['correct']
            correct_Sentence = TextBlob(text).correct()
    except:
        e = "Sorry, what is this..! don't have  sense."
    return render_template('home.html',e=e,correct_Sentence=correct_Sentence)


if __name__ =='__main__':
    app.run(debug=False)
