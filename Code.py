import nltk
nltk.download('punkt')
nltk.download('wordnet')
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import tkinter as tk
import random
from PIL import Image, ImageTk

# Load the dataset
with open(r"C:\Users\RIDHIMA KAPOOR\OneDrive\Desktop\Chatbotss\Data set\file.txt", 'r', encoding='utf-8') as file:
    dataset = file.read()

# Preprocess the dataset
sent_tokens = nltk.sent_tokenize(dataset)
word_tokens = nltk.word_tokenize(dataset.lower())

lemmatizer = nltk.stem.WordNetLemmatizer()
remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)

def LemTokens(tokens):
    return [lemmatizer.lemmatize(token) for token in tokens]

def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))

# TF-IDF Vectorization
TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
tfidf_matrix = TfidfVec.fit_transform(sent_tokens)

# Function to generate response
def response(user_response):
    robo_response = ''
    user_tfidf = TfidfVec.transform([user_response])
    cosine_similarities = cosine_similarity(user_tfidf, tfidf_matrix)
    idx = cosine_similarities.argsort()[0][-1]
    flat = cosine_similarities.flatten()
    flat.sort()
    req_tfidf = flat[-1]

    if req_tfidf == 0:
        robo_response = "I am sorry! I don't understand your question."
    else:
        robo_response = sent_tokens[idx]

    return robo_response

# Function to handle user input
def handle_input():
    user_response = user_input.get()
    user_input.delete(0, tk.END)  # Clear input field after submission

    if user_response.lower() == 'bye':  # Check if user wants to exit
        root.destroy()  # Close the tkinter window
        return

    bot_response = response(user_response)
    conversation_text.config(state=tk.NORMAL)  # Enable text box to insert conversation
    conversation_text.insert(tk.END, "You: " + user_response + "\n")
    conversation_text.insert(tk.END, "Bot: " + bot_response + "\n")
    conversation_text.config(state=tk.DISABLED)  # Disable text box after inserting conversation

def start_conversation():
    start_button.config(text="Okay", command=okay_action)  # Change button text and command
    heading="WARNING!!!!!!!!!!"
    line="\nI AM JUST A BOT, PLEASE CONSULT A REAL\n LAWYER BEFORE TAKING ANY LEGAL ACTION\n CLICK “OKAY” TO CONTINUE \n"
    para=""
    main_menu_label.config(text=heading)
    sub_label.config(text=line)
    sub_label2.config(text=para)
 
def okay_action():
    main_menu_frame.pack_forget()  # Hide the main menu frame
    conversation_frame.pack()# Show the conversation frame
    button.pack_forget()
def button_clicked():
    print("image")
    

heading="LAND LEGAL BOT"
line=" A property law advisory bot"
para="\n I'm your property law expert, Ask me anything about \n Indian property law, from ownership to taxes, and I'll \n guide you through the legal jungle with quick,\naccurate answers.\n"

# Initialize   Tknter
root = tk.Tk()
root.title("LAND LEGAL BOT(LLB)")
root.geometry("2000x1900")
root.configure(bg="light blue")  # Set background  color to light blue

#image button
image = tk.PhotoImage(file=r"C:\Users\RIDHIMA KAPOOR\OneDrive\Desktop\Chatbotss\LOGO3.png")
button = tk.Button(root, image=image, command=button_clicked)
button.pack(padx=10, pady=10)

# Main Menu Frame
main_menu_frame = tk.Frame(root, bg="light blue")
main_menu_frame.pack(side=tk.TOP)  # Place main menu frame at the top

# Main Menu Label
main_menu_label = tk.Label(main_menu_frame, text=heading, font=("ARIAL", 25,'bold'), bg="light blue",fg="red")
main_menu_label.pack(padx=10, pady=10)

#sub label
sub_label = tk.Label(main_menu_frame, text=line, font=("arial", 22,'bold'), bg="light blue",fg="#001C52")
sub_label.pack(padx=10, pady=10)

# Sub Labe2
sub_label2 = tk.Label(main_menu_frame, text="\n I'm your property law expert, Ask me anything about \n Indian property law, from ownership to taxes, and I'll \n guide you through the legal jungle with quick,\naccurate answers.\n", font=("arial", 18), bg="light blue")
sub_label2.pack(padx=10, pady=10)

# Start Button
start_button = tk.Button(main_menu_frame, text="Start", command=start_conversation, width=15, height=2, font=("arial", 18,'bold'),fg="red",bg="blue",activebackground="white")
start_button.pack(padx=10, pady=10)

# Conversation Frame
conversation_frame = tk.Frame(root, bg="light blue")

# Bot introduction label
intro_label = tk.Label(conversation_frame, text="BOT: My name is LLB. Let's have a conversation. Also, if you want to exit any time, just type 'Bye'.",font=('arial',12,"bold"), bg="light blue")
intro_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

# Text block for conversation
conversation_text = tk.Text(conversation_frame, height=30, width=150, state=tk.DISABLED)
conversation_text.grid(row=1, column=0, padx=10, pady=10)

#write here label
write_label = tk.Label(conversation_frame, text="*write your input here and click submit-",font=('arial',10,"bold"), bg="light blue")
write_label.grid(row=2,column=0, padx=10, pady=10)

# Text entry for user response
user_input = tk.Entry(conversation_frame, width=100)
user_input.grid(row=3, column=0, padx=10, pady=10)

# Button to submit user response
submit_button = tk.Button(conversation_frame, text="Submit", command=handle_input)
submit_button.grid(row=4, column=0, padx=10, pady=10)

# Hide the conversation frame initially
conversation_frame.pack_forget()

# Start the GUI event loop
root.mainloop()
