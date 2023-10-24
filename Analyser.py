
''' from textblob import TextBlob

     <p>
        <img src="Background.png" width="700" height="400">
       </p>



    blob = TextBlob("Happy")

    sentiment = blob.sentiment.polarity # -1 to 1
    print(sentiment)'''

     ''' print('<html>')
    print('<title>')
    print('<body><center>')
    print('<form>')
    print('<h1></h1>')


    if sentiment==0:
        print("The text is neutral")
        print('<p1></p1>')

    elif -1<=sentiment<=-0.5:
        print("The text is extremely negative")
        print('<p1></p1>')

    elif 0.5<=sentiment<=1:
        print("The text is extremely positive")
        print('<p1></p1>')

    elif -0.5<sentiment<0:
        print("The text is a bit negative")
        print('<p></p>')

    elif 0<sentiment<0.5:
        print("The text is a bit positive")
        print('<p></p>')  
            
    print('</form></center></body></html>')

'''