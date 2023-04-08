import tkinter as tk
from tkinter import *
from Speaky import Speaky

class ChatbotUI:
    def __init__(self):
        self.bot = Speaky()
        self.bot.train("data.txt")
        self.bot.train1("DialogueTrain.txt")
        
        self.window = tk.Tk()
        self.window.title("Speaky - Votre Inteligance rendu artificiel")
        
        self.history = tk.Listbox(self.window, width=200, height=30)
        self.history.pack(padx=10, pady=10)
        
        self.entry = tk.Entry(self.window, width=50)
        self.entry.pack(padx=10, pady=10)
        self.entry.bind("<Return>", self.handle_input)
        
        self.send_button = tk.Button(self.window, text="Envoyer", command=self.handle_input)
        self.send_button.pack(padx=10, pady=10)
        response = "Salut je suis speaky je suis la pour vous aidez"
        self.history.insert(tk.END, "Speaky: {}".format(response))
        
        self.window.mainloop()
    
    def handle_input(self, event=None):
        user_input = self.entry.get()
        self.entry.delete(0, tk.END)
        self.history.insert(tk.END, "vous: {}".format(user_input))
        if user_input.lower() in self.bot.goodbyes:
            response = "Au revoir!"
            self.history.insert(tk.END, "Speaky: {}".format(response))
        elif user_input.lower() in self.bot.greetings:
            response = "Salut!"
            self.history.insert(tk.END, "Speaky: {}".format(response))
        elif user_input.lower() in self.bot.help_msgs:
            response = "Je peut t'aider ?!"
            self.history.insert(tk.END, "Speaky: {}".format(response))
        elif user_input.lower() in self.bot.Coubeh:
            response = "QuoiCoubeh"
            self.history.insert(tk.END, "Speaky: {}".format(response))
        elif user_input.lower() in self.bot.hein:
            response = "heinpayaye QuoiCoubeh QuoiCoubeh QuoiCoubeh"
            self.history.insert(tk.END, "Speaky: {}".format(response))
        elif user_input.lower() in self.bot.joke:
            response = "J'ai une blague sur les orphelin ... Ah non je l'ai abandone"
            self.history.insert(tk.END, "Speaky: {}".format(response))
        elif user_input.lower() in self.bot.pub:
            response = "Les deux bon streamer est les seul sont https://www.twitch.tv/0verline est https://www.twitch.tv/chezpoluxxvous"
            self.history.insert(tk.END, "Speaky: {}".format(response))
        else:
            response = self.bot.generate_response(user_input)
            self.history.insert(tk.END, "Speaky: {}".format(response))

ChatbotUI()
