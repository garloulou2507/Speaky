import nltk
import numpy as np
import random
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

class Speaky:
    def __init__(self):
        self.n = 5  # nombre de réponses précédentes à prendre en compte
        self.sent_tokens = []
        self.lemmer = WordNetLemmatizer()
        self.stop_words = set(stopwords.words('english'))
        self.TfidfVec = TfidfVectorizer(tokenizer=self.lemTokens, stop_words='english')
        self.tfidf = None
        self.chat_history = []
        self.greetings = ["Bonjour", "Salut", "salutations", "Hey", "Quoi de neuf", "Comment ça va ?"]
        self.goodbyes = ["Au revoir", "Bye", "À bientôt"]
        self.help_msgs = ["Je peux t'aider pour quoi ?", "Aide-moi", "Je peux vous aider ?"]
        self.unknown_msgs = ["Désolé, je n'ai pas compris votre message.", "Pouvez-vous répéter ?", "Pouvez-vous reformuler votre phrase ?"]
        self.Coubeh = ["Quoi ?", "quoi", "quoi ?"]
        self.hein = ["Hein ?", "hein", "Hein"]
        self.joke = ["Raconte une blague", "blague stp"]
        self.pub = ["donne des bon streamer", "pub"]
        self.dialogue_file = "DialogueTrain.txt"

    def save_dialogue(self, user_input, response):
        with open(self.dialogue_file, "a") as f:
            f.write(user_input + "!" + "\n")
            f.write(response + "!" + "\n")

    def generate_response(self, user_input):
        self.chat_history.append(user_input)

        response = ''
        self.sent_tokens.append(user_input)
        self.tfidf = self.TfidfVec.fit_transform(self.sent_tokens)
        vals = cosine_similarity(self.tfidf[-1], self.tfidf)
        idx = vals.argsort()[0][-2]
        flat = vals.flatten()
        flat.sort()
        req_tfidf = flat[-2]

        if req_tfidf == 0:
            response = random.choice(self.unknown_msgs)
        else:
            response = self.sent_tokens[idx]

        # enregistrer le dialogue dans le fichier de dialogue
        self.save_dialogue(user_input, response)

        # ajouter les nouveaux mots au corpus
        self.sent_tokens += nltk.sent_tokenize(response)

        # réajuster la matrice tf-idf
        self.tfidf = self.TfidfVec.fit_transform(self.sent_tokens)

        return response


    def lemTokens(self, tokens):
        return [self.lemmer.lemmatize(token.lower()) for token in tokens if token not in string.punctuation]

    def remove_stopwords(self, tokens):
        return [token for token in tokens if token not in self.stop_words]

    
    def train(self, filename="data.txt"):
        with open(filename, "r", encoding="utf-8") as file:
            raw_data = file.read()
        
        self.sent_tokens = nltk.sent_tokenize(raw_data)
        self.tfidf = self.TfidfVec.fit_transform(self.sent_tokens)


    def train2(self, filename="DialogueTrain.txt"):
        with open(filename, "r", encoding="utf-8") as file:
            raw_data = file.read()
        
        self.sent_tokens = nltk.sent_tokenize(raw_data)
        self.tfidf = self.TfidfVec.fit_transform(self.sent_tokens)


    def train1(self, filename="DialogueTrain.txt"):
        with open(filename, "r", encoding="utf-8") as file:
            raw_data = file.read()
        
        self.sent_tokens = nltk.sent_tokenize(raw_data)
        self.tfidf = self.TfidfVec.fit_transform(self.sent_tokens)    


    def generate_response(self, user_input):
        self.chat_history.append(user_input)

        response = ''
        self.sent_tokens.append(user_input)
        self.tfidf = self.TfidfVec.fit_transform(self.sent_tokens)
        vals = cosine_similarity(self.tfidf[-1], self.tfidf)
        idx = vals.argsort()[0][-2]
        flat = vals.flatten()
        flat.sort()
        req_tfidf = flat[-2]

        if req_tfidf == 0:
            response = random.choice(self.unknown_msgs)
        else:
            response = self.sent_tokens[idx]

        # enregistrer le dialogue dans le fichier de dialogue
        self.save_dialogue(user_input, response)

        # ajouter les nouveaux mots au corpus
        self.sent_tokens += nltk.sent_tokenize(response)

        # réajuster la matrice tf-idf
        self.tfidf = self.TfidfVec.fit_transform(self.sent_tokens)

        return response


    def chat_with_dialogue(self):
        print("Salut je suis Speaky et je vais lire les phrases du fichier de dialogue pour générer des réponses.")

        with open(self.dialogue_file, "r") as f:
            lines = f.readlines()
            for i in range(0, len(lines), 2):
                user_input = lines[i].strip()
                response = self.generate_response(user_input)
                print("vous: ", user_input)
                print("Speaky: ", response)
                self.chat_history.append(user_input)
                self.chat_history.append(response)

        print("Fin du dialogue.") 
