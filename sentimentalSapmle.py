Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> from textblob import TextBlob
>>> a = TextBlob("I am the best programmer ever")
>>> a.sentiment.polarity
1.0
>>> a = TextBlob("I am the worst programmer ever")
>>> a.sentiment.polarity
-1.0
>>> a = TextBlob("I love my parents")
>>> a.sentiment.polarity
0.5
>>> a = TextBlob("I am a programmer")
>>> a.sentiment.polarity
0.0
>>> a.sentiment











