from tkinter import*
from PIL import Image, ImageTk
import speech_to_text
import action
root = Tk()
root.title("My AI Assistant")
root.geometry("550x675")
root.resizable(False, False)
root.config(bg="#6F8FAF")

#ask fun
def ask():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something...")
        audio = recognizer.listen(source)

        try:
            ask_val = recognizer.recognize_google(audio)
            bot_val = action.Action(ask_val)
            text.insert(END, 'User ---> ' + ask_val + "\n")
            if bot_val is not None:
                text.insert(END, "BOT ---> " + str(bot_val) + "\n")
            if bot_val == "Okay sir":
                root.destroy()
        except sr.UnknownValueError:
            text.insert(END, "BOT ---> Sorry, I didn't catch that.\n")
        except sr.RequestError:
            text.insert(END, "BOT ---> Sorry, there was a connection issue.\n")





def send():
    print("send")

def del_text():
    print("Delete")



#frame
frame= LabelFrame(root, padx=100,pady=7,borderwidth=3,relief="raised")
frame.config(background="#6f8faf")
frame.grid(row=0,column=1, padx=55, pady=10)

#text label
text_label=Label(frame,text="AI Assistant", font=("comic sans ms", 14,"bold"),background="#356696")
text_label.grid(row=0, column=0, padx=20, pady=10)

#image
image=ImageTk.PhotoImage(Image.open("image/assitant.png"))
image_label= Label(frame, image=image)
image_label.grid(row=1, column=0,pady=20)



#adding a text widgget
text= Text(root,font=('courier 10 bold'), bg="#356696")
text.grid(row=2,column=0)
text.place(x= 100, y=375,width=375, height=100)

#entry widget
entry =Entry(root, justify=CENTER)
entry.place(x=100,y=500, width=350, height=30)

#button 1
Button1= Button(root,text="Ask", bg="#356696", pady=16,padx=40, borderwidth=3, relief=SOLID, command=ask)
Button1.place(x=70, y=575)

#button 2
Button2= Button(root,text="Send", bg="#356696", pady=16,padx=40, borderwidth=3, relief=SOLID, command=send)
Button2.place(x=400, y=575)

#buttton 3
Button3= Button(root,text="Delete", bg="#356696", pady=16,padx=40, borderwidth=3, relief=SOLID, command=del_text)
Button3.place(x=225, y=575)


root.mainloop()
