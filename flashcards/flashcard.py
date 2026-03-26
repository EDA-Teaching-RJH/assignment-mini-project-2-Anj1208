import re
import csv
#importing re and csv libraries

class Card:  #base class to store the question and answer of each flashcard
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer



class Flashcard(Card):   
    def __init__(self, question, answer, tag = "general"):    #inherits from card class and adds feature suchas tag
        super().__init__(question, answer)
    
    def dict(self):        #converts flashcard into dictionary
        return{
            "question": self.question,
            "answer": self.answer,
            "tag": self.tag      
        }
    
    def tuple(self):       #converts flashcard into a tuple
        return (self.question, self.answer, self.tag)
    

    