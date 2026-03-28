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
    

class Deck:
    def __init__(self):
        self.cards = []     #making a list to store flashcards

    def add_card(self, flashcard):
        self.cards.append(flashcard)          #adding a flashcard to deck  

    def list_cards(self):
        return [card.tuple() for card in self.cards]

    def search(self, pattern):
        regex = re.compile(pattern, re.IGNORECASE)
        return [card for card in self.cards if rgex.search(card.question)]       #getting the cards that match the pattern 

    def save_to_csv(self, filename="flashcards.csv"):          #saving all the flashcards to a csv file
        with open(filename,  "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["question", "answer", "tag"])
            for card in self.cards:
                writer.writerow([card.question, card.answer, card.tag])

    def load_from_csv(self, filename="flashcards.csv"):
        try:
            with open(filename, "r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    card = Flashcard(row["question"], row["answer"], row["tag"])
                    self.cards.append(card)
        except FileNotFoundError:
            pass
