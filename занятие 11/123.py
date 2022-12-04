import json
import requests
from tkinter import*

def buttonAction():
	with open('123.txt','w') as file:
		user = txtField.get()
		url = f"https://api.github.com/users/{user}"
		userInfo = requests.get(url).json()
		enum = ['company','created_at','email','id','name','url']
		data = userInfo.keys()
		for c in data:
			if c in enum:
				file.write(F"{c}:{userInfo[c]}" + '\n')
	head.configure(text = "Данные записаны")


root = Tk()
root.title('Get request')
root.geometry('1920x1080')
root["bg"] = "lightblue"

head = Label(root, bg = "lightblue",fg = "black", text = "Введите имя пользователя GitHub: ", font = ('ObelixPro',30))
head.pack(expand = True)
txtField = Entry(root, width = 50, font = ('ObelixPro', 20))
txtField.pack(expand = True)
button = Button(root, bg = "black", fg = "white", text = "Нажмите сюда!", command = buttonAction)
button.pack(expand = True)

root.mainloop()