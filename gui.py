import tkinter as tk
from PIL import ImageTk, Image


root = tk.Tk()
root.geometry("1000x400")

# Drop Down Boxes


def show():
    outLabel = tk.Label(root, text=outputClick.get()).pack(side=tk.RIGHT)


outputOptions = [
    "Output language",
    "English",  # en
    "Hindi",  # hi
    "Spanish",  # es
    "French",  # fr
    "Arabic",  # ar
    "Bengali",  # bn
    "Russian",  # ru
    "Portuguese",  # pt
    "Indonesian",  # id
]
bop = tk.Frame()
bop.pack(side=tk.LEFT)

# drop down menu
outputClick = tk.StringVar()
outputClick.set(outputOptions[0])
outputList = tk.OptionMenu(bop, outputClick, *outputOptions)
outputList.pack()


def cbc(tex):
    return lambda: callback(tex)


def callback(tex):
    language = outputClick.get()
    if language == "Output Language" or language == "English":
        language = "en"
    elif language == "Hindi":
        language = "hi"
    elif language == "Spanish":
        language = "es"
    elif language == "French":
        language = "fr"
    elif language == "Arabic":
        language = "ar"
    elif language == "Bengali":
        language = "bn"
    elif language == "Russian":
        language = "ru"
    elif language == "Portuguese":
        language = "pt"
    elif language == "Indonesian":
        language = "id"

    tex.insert(tk.END, language.format())
    tex.see(tk.END)             # Scroll if necessary


tex = tk.Text(master=root)
tex.pack(side=tk.RIGHT)


tv = 'Start Transcribing'.format()
b = tk.Button(bop, text=tv, command=cbc(tex))
b.pack()

tk.Button(bop, text='Exit', command=root.destroy).pack()

root.mainloop()
