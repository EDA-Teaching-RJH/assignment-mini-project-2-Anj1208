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
        return [card for card in self.cards if regex.search(card.question)]       #getting the cards that match the pattern 

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


def main():
    deck = Deck()
    deck.load_from_csv()
    while True:
        print(" Flashcard Menu")
        print("1. Add a flashcard")
        print("2. Show all flashcards")
        print("3. Search all flashcards")
        print("4. Save all flashcards to CSV")
        
        option = input("Choose an option")

        if option == "1":
            question = input("enter the question ")
            answer = input("enter the answer ")
            tag = input("enter a tag ")
            card = Flashcard(question, answer, tag)
            deck.add_card(card)
            print("flashcard added")
        
        elif option =="2":
            cards = deck.list_cards()
            if not cards:
                print("no flashcard found")
        
        elif option =="3":
            pattern = input("enter a regex pattern to search")
            results = deck.search(pattern)
            if not results:
                print("no matches found")

        elif option =="4":
            deck.save_to_csv()
            print("flashcards saved to CSV")

        else:
            print("Invalid option. please try again")

if __name__ == "__main__":
    main()

