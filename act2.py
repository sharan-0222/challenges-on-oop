class flashcard:
    def __init__(self,word,meaning):
        self.word=word
        self.meaning=meaning

    def __str__(self):
      return self.word+'('+self.meaning+')'


flash=[]
while True:
     word= input("Enter the word:")
     meaning= input("Enter the meaning:")
     flash.append(flashcard(word,meaning))
     option=int(input("do you want to add more flashcards? 1 for yes, 0 for no:"))
     if option==0:
            break
     
print("the flashcards are:")
for i in flash:
    print(">",i)