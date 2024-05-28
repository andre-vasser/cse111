import random

def main():
    quantity = 1
    tense = "past"
    print(make_sentence(quantity, tense))

    quantity = 1
    tense = "present"
    print(make_sentence(quantity, tense))

    quantity = 1
    tense = "future"
    print(make_sentence(quantity, tense))

    quantity = 2
    tense = "past"
    print(make_sentence(quantity, tense))

    quantity = 2
    tense = "present"
    print(make_sentence(quantity, tense))

    quantity = 2
    tense = "future"
    print(make_sentence(quantity, tense))

def make_sentence(quantity, tense):
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)
    verb = get_verb(quantity, tense)
    prepositional_phrase = get_prepositional_phrase(quantity)
    sentence = f"{determiner.capitalize()} {noun} {verb} {prepositional_phrase}."
    return sentence

def get_determiner(quantity):
    if quantity == 1:
        determiners = ["the", "one"]
    else:
        determiners = ["some", "many"]
    return random.choice(determiners)

def get_noun(quantity):
    if quantity == 1:
        nouns = ["bird", "boy", "car", "cat", "child",
                 "dog", "girl", "man", "rabbit", "woman"]
    else:
        nouns = ["birds", "boys", "cars", "cats", "children",
                 "dogs", "girls", "men", "rabbits", "women"]
    return random.choice(nouns)

def get_verb(quantity, tense):
    if tense == "past":
        verbs = ["drank", "ate", "grew", "laughed", "thought",
                 "ran", "slept", "talked", "walked", "wrote"]
    elif tense == "present":
        verbs = ["drinks", "eats", "grows", "laughs", "thinks",
                 "runs", "sleeps", "talks", "walks", "writes"]
    elif tense == "future":
        verbs = ["will drink", "will eat", "will grow", "will laugh",
                 "will think", "will run", "will sleep", "will talk",
                 "will walk", "will write"]
    return random.choice(verbs)

def get_preposition():
    prepositions = ["about", "above", "across", "after", "along",
                    "around", "at", "before", "behind", "below",
                    "beyond", "by", "despite", "except", "for",
                    "from", "in", "into", "near", "of",
                    "off", "on", "onto", "out", "over",
                    "past", "to", "under", "with", "without"]
    return random.choice(prepositions)

def get_prepositional_phrase(quantity):
    preposition = get_preposition()
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)
    prepositional_phrase = f"{preposition} {determiner} {noun}"
    return prepositional_phrase

if __name__ == "__main__":
    main()