from flashcard import Card, Flashcard, Deck

def test_card_init():
    c = Card("Q", "A")
    assert c.question == "Q"
    assert c.answer =="A"

def test_flashcard_inherits_card():
    f = Flashcard("Q", "A", "tag")
    assert isinstance(f, Card)
    assert f.tag == "tag"

def test_add_card():
    deck = Deck()
    f = Flashcard("Q ", "A", "tag")
    deck.add_card(f)
    assert len(deck.cards) == 1

def test_list_cards():
    deck = Deck()
    deck.add_card(Flashcard("Q", "A", "tag"))
    result = deck.list_cards()
    assert result == [("Q", "A", "tag")]

def test_regex_search():
    deck = Deck()
    deck.add_card(Flashcard("What is the capital of england", "London", "Geography"))
    deck.add_card(Flashcard("How many years did WW2 last", "6 years", "History"))
    matches = deck.search("What")
    assert len(matches) == 1
    assert matches[0].question == "What is the capital of england"