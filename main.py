import requests
from tkinter import *
from tkinter.messagebox import showinfo, showerror
import json


def send_sms(number, message):
    url = 'https://www.fast2sms.com/dev/bulk'
    params = {
        'authorization': 'ldrDmt9iR7bHzUZshuGqWIVTvKPwC6FLcyM4JBAegxN1QOkfp2lm5WbB4XIkTQ1UMsYFNDL023CjPtRO',
        'sender_id': 'FSTSMS',
        'message': message,
        'language': 'english',
        'route': 'p',
        'numbers': number
    }

    response = requests.get(url, params=params)
    dic = response.json()
    return dic


#send_sms("9305184249", 'this is me!')
def btn_click():
    number = textNumber.get()
    msg = textMsg.get('1.0', END)
    ans = send_sms(number, msg)
    if ans['return'] == True and ans['message'] == 'Message sent successfully to NonDND numbers':
        showinfo('Send Success', 'Successfully Sent!')
    else:
        showerror('Error', ans['message'])


root = Tk()
root.config(bg='#3498DB')
root.title('Message Sender')
# root.iconbitmap('download.png')
root.geometry('400x600')

image = PhotoImage(file='download.png')

headingImage = Label(root, image=image)
headingImage.pack(side=TOP)
label1 = Label(root, text='Recipient Number', font=('Helvetica', 16, 'bold'))
label1.pack(side=TOP, pady=9)
textNumber = Entry(root, font=('Helvetica', 22, 'bold'))

textNumber.pack(fill=X, pady=20)
label2 = Label(root, text='Message', font=('Helvetica', 16, 'bold'))
label2.pack(side=TOP, pady=4)
textMsg = Text(root, height=6)
textMsg.pack(fill=X)

sendBtn = Button(root, text='SEND SMS', relief='ridge',
                 activeforeground='green', font=(
                     "Helvetica", 18), command=btn_click)

sendBtn.pack(pady=7)
author = Label(root, text="@G.S.")
author.config(font=("Courier", 44))
author.pack(side=BOTTOM)

root.mainloop()
