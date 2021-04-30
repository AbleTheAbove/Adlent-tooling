import json, toml



## Players should be saved as toml because I like toml more than json
y = open("character.toml", "r")
x = toml.loads(y.read())
print(x)


import tkinter as tk
window = tk.Tk()
greeting = tk.Label(text=x["name"]["title"])
greeting.pack()


window.mainloop()
