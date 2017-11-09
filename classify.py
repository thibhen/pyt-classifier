
from textblob.classifiers import NaiveBayesClassifier
from textblob import TextBlob


# ISSUE : training is case sesitive !!!

print "INFO : Model Initialization - BEGIN"

with open('training.csv', 'r') as fp:
     cl = NaiveBayesClassifier(fp, format="csv")

print "INFO : Model Initialization - END"

def classify(message):
  tags = cl.classify(message.lower())
 
  print "DEBUG : '",message,"'  - Result " , tags 
  return tags 

