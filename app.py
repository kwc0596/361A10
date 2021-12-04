import tkinter as tk
import requests, jsonify
from threading import Thread
from service import wiki_query

api = "http://api.quotable.io/random"
quoteinfo=[]
quotes=[]

zero=0
quote_number=zero

window=tk.Tk()

window.geometry ("1000x400")

window.configure (bg="black")

def preload_quotes():
    global quotes

    print("Loading")
    for quoteNum in range(15) :
        random_quote=requests.get(api). json()
        content=random_quote ["content"]
        author=random_quote ["author"]
        quote=content+"\n\n"+"By "+author
        quoteinfo.append (str(author))
        print (content)
        quotes.append (quote)
    print("Loading is finished.")
window.title ("Random Quote Generator")

window.grid_columnconfigure (0, weight = 1)




preload_quotes ()

def get_random_quote ():
    
    global quote_wiki

    global quotes

    global quote_label

    global quote_number
    

    quote_label.configure (text = quotes[quote_number])

    info = wiki_query( quoteinfo [quote_number] )

    quote_wiki.configure (text = info)

    quote_number = quote_number + 1


    if quotes [quote_number] == quotes [-3] :

        thread = Thread (target = preload_quotes)

        thread.start ()



 
# Design of frontend
quote_label = tk.Label (window, text="You can click on this button to create a random #",
                        pady=20,
                        wraplength=1000,
                        height=8,
                        
                        
                        font =("Arial", 15))
quote_label.grid(row = 0, stick ="WE", padx=20,column=0, pady = 10)
quote_wiki = tk.Label(window)
quote_wiki.grid(row=0,  stick="S", padx=20, column=0, pady=10)

button = tk.Button (text = "Generate a Quote",fg = "#948f8f", command = get_random_quote,bg = '#0052dd', 
                    activebackground = "black", font = ("Arial", 15))
button.grid (row = 1, padx = 20, column = 0, stick = "WE",  pady = 10)

#Execute the program

if __name__=="__main__" :
    window.mainloop ()
