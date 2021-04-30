import toml, tkinter

# Toss this in its own file along with other file io helper functions
def OpenCharacter(path):
  character_file = open(path, "r")
  character = toml.loads(character_file.read())
  character_file.close()
  return character


# This should be a list at some point
x = OpenCharacter("character.toml")

window = tkinter.Tk()
greeting = tkinter.Label(text=x["name"]["title"])
greeting.pack()

window.mainloop()
