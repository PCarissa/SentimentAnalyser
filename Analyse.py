from flask import Flask, render_template, request
from textblob import TextBlob
app = Flask(__name__)


@app.route('/',methods=["Post" ,"Get"])
def main():
       if request.method == "POST":
             text= request.form.get("Text")
             blob = TextBlob(str(text))
             sentiment = blob.sentiment.polarity
             if sentiment==0:
                   return render_template('ANA.html',message= "NEUTRAL 😐")
             elif -1<=sentiment<=-0.5:
                   return render_template('ANA.html', message= "EXTREMELY NEGATIVE 😡")
             elif 0.5<=sentiment<=1:
                    return render_template('ANA.html',message="EXTREMELY POSITIVE 😄")
             elif -0.5<sentiment<0:
                    return render_template('ANA.html', message= "NEGATIVE 😠")
             elif 0<sentiment<0.5:
                   return render_template('ANA.html',message="POSITIVE 😀")
             else:
                  return render_template("ANA.html")

       return render_template("ANA.html")

       

if __name__ == '__main__':
   app.run(debug='True')


