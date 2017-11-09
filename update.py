
import csv  

def updateTraining(message,tag):
  print "DEBUG : Update Training Data with message:'",message,"'  - tag:" , tag 
  with open("training.csv", "a") as f:
    writer = csv.writer(f)
    writer.writerow([message.lower(),tag])
    f.close()
  return "OK" 

