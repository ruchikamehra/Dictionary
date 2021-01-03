import json
import tkinter
from tkinter import messagebox

instruction = tkinter.Tk()
instruction.title("INSTRUCTIONS")
Text = tkinter.Text(instruction, bg="light yellow", width=60, height=30, font=('Courier', 10))
Text.pack()
Text.tag_configure('big', font=('Verdana', 20, 'bold'))
Text.insert(tkinter.END, '\t\tINSTRUCTION\t\n', 'big')
instructions = """
\t\t Welcome to the dictionary\n\n
1. If you want to search a word,then write the word in the word box and then click the search button.\n
2. If you are not satisfied with the word, then you can edit the word by  writing the meaning in the 'entermeaning' box and press the 'edit' button.\n
3. If the meaning of the word is not present in the dictionary, you can add the word by writing the meaning in the 'entermeaning box' and then press the add button.
"""
Text.insert(tkinter.END, instructions, 'color')
Text.tag_configure('color', font=('Arial', 12), foreground='black')
button = tkinter.Button(instruction, text="okay", command=instruction.destroy).pack(side='top')

instruction.mainloop()
window = tkinter.Tk()
window.title("DICTIONARY")
data = json.load(open("data.json", encoding='utf-8'))


def call_me():
    word = e.get()
    word = word.lower()
    wordtext.delete("0.1", tkinter.END)
    if word in data:
        mean = data[word]
        wordtext.insert(tkinter.END, mean)
        print(mean)
    else:
        reason = "kindly add this word first \n", "check your connection"
        wordtext.insert(tkinter.END, reason)


def edit_me():
    word = e.get()
    meaning_word = entertext.get("0.1", tkinter.END)
    data[word] = meaning_word
    with open("data.json", 'w') as json_file:
        json.dump(data, json_file)


def add_me():
    word = e.get()
    if word in data:
        messagebox.showinfo("ERROR",
                            "word is already added, cannot be added again")
    else:
        meaning_word = entertext.get("0.1", tkinter.END)
        data[word] = meaning_word
        with open("data.json", 'w') as json_file:
            json.dump(data, json_file)


top_frame = tkinter.Frame(window, bg="white", bd=0, highlightbackground="black", highlightcolor="black")
top_frame.grid(row=0, column=0, sticky="W")
label_head = tkinter.Label(top_frame, text="WORD", font=('arial', 10, 'bold'))
label_head.grid(row=0, column=0)
e = tkinter.Entry(top_frame, width=50)
e.grid(row=1, column=0)

wordtext = tkinter.Text(top_frame, bg="pink", width=60, height=30, font=('Courier', 10, 'italic'))
wordtext.grid(row=2, column=0)
side_frame = tkinter.Frame(window, bg="white")
side_frame.grid(row=0, column=1, sticky="W")
tkinter.Button(side_frame, text="search", width=25, height=4, command=lambda: call_me()).grid(row=0, column=0, padx=1,
                                                                                              pady=1)
tkinter.Button(side_frame, text="add", width=25, height=4, command=lambda: add_me()).grid(row=1, column=0, padx=1,
                                                                                          pady=1)
tkinter.Button(side_frame, text="edit", width=25, height=4, command=lambda: edit_me()).grid(row=2, column=0, padx=1,
                                                                                            pady=1)
bottom_frame = tkinter.Frame(window, bg="white")
bottom_frame.grid(row=1, column=0)
label2 = tkinter.Label(bottom_frame, text="ENTER MEANING", font=('arial', 10, 'bold'))
label2.grid(row=0, column=0)
entertext = tkinter.Text(bottom_frame, width=60, height=2, bg="light pink")
entertext.grid(row=1, column=0)
window.mainloop()
