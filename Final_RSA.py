from tkinter import *


def clickhere():

    global user_input_p, user_input_q, user_input_msg, output, output1
    root.destroy()

    secondWindow = Tk()
    secondWindow.title("RSA")
    secondWindow.geometry("1000x700")
    secondWindow.resizable(0, 0)
    secondWindow.configure(bg='black')

    rsa = Label(secondWindow, text="RSA ALGORITHM", font=(
        "caliber", 50, 'bold'), bg="black", fg='#4AF96A')
    rsa.place(x=200, y=0)

    number1 = Label(secondWindow, text="Enter First Prime Number : ",
                    font=("caliber", 20), bg='black', fg='#4AF96A')
    number1.place(x=50, y=100)

    user_input_p = Entry(secondWindow, width=18, bd=4, font=("caliber", 20))
    user_input_p.place(x=432, y=105, height=35)

    number2 = Label(secondWindow, text="Enter Second Prime Number : ", font=(
        "caliber", 20), bg='black', fg='#4AF96A')
    number2.place(x=50, y=150)

    user_input_q = Entry(secondWindow, width=18, bd=4, font=("caliber", 20))
    user_input_q.place(x=430, y=155, height=35)

    message = Label(secondWindow, text="Enter Text : ",
                    font=("caliber", 20), bg='black', fg='#4AF96A')
    message.place(x=50, y=200)

    user_input_msg = Entry(secondWindow, width=18, bd=4, font=("caliber", 20))
    user_input_msg.place(x=430, y=205, height=35)

    takeinput = Button(secondWindow, text="Exit", font=('Caliber', 20, 'bold'), bg='black',
                       activebackground='black', fg='#4AF96A', relief=GROOVE, bd=5, command=secondWindow.destroy)
    takeinput.place(x=800, y=180)

    clearinput = Button(secondWindow, text="Clear Screen", font=('Caliber', 20, 'bold'), bg='black',
                        activebackground='black', fg='#4AF96A', relief=GROOVE, bd=5, command=clear_input)
    clearinput.place(x=750, y=100)

    process = Button(secondWindow, text='Process', font=('Caliber', 20, 'bold'), bg='black',
                     activebackground='black', fg='#4AF96A', relief=GROOVE, bd=5, command=start_processing)
    process.place(x=400, y=300)

    encrypted_value = Label(secondWindow, text="Encrypted Value : ", font=(
        "caliber", 20), bg='black', fg='#4AF96A')
    encrypted_value.place(x=50, y=400)

    output = Text(secondWindow, width=20, height=5, font=("caliber", 20))
    output.place(x=50, y=450)

    decrypted_value = Label(secondWindow, text="Decrypted Value : ", font=(
        "caliber", 20), bg='black', fg='#4AF96A')
    decrypted_value.place(x=650, y=400)

    output1 = Text(secondWindow, width=20, height=5, font=("caliber", 20))
    output1.place(x=650, y=450)

    secondWindow.mainloop()


def clear_input():
    user_input_p.delete(0, END)
    user_input_q.delete(0, END)
    user_input_msg.delete(0, END)
    output.delete('1.0', END)
    output1.delete('1.0', END)


# global output, p,
def start_processing():
    global user_input_p, user_input_q, user_input_msg
    global p, q, msg

    p = int(user_input_p.get())

    q = int(user_input_q.get())

    msg = user_input_msg.get()
    # global p, q, msg

    n = p * q
    phi = (p-1)*(q-1)

    e = find_e(phi)
    d = find_d(e, phi)

    cypher_text = ''
    for ch in msg:
        ch = ord(ch)
        cypher_text += chr((ch ** e) % n)

    plain_text = ''
    for ch in cypher_text:
        ch = ord(ch)
        plain_text += chr((ch ** d) % n)

    output.insert(END, cypher_text)
    output1.insert(END, plain_text)


def find_e(phi: int):
    e = 2
    while e < phi:
        if gcd(e, phi) == 1:
            return e
        e += 1


def find_d(e: int, phi: int):
    d = 2
    while d < phi:
        if ((d*e) % phi) == 1:
            return d
        d += 1


def gcd(x: int, y: int):
    small, large = (x, y) if x < y else (y, x)

    while small != 0:
        temp = large % small
        large = small
        small = temp

    return large


global root
root = Tk()

root.title("RSA")
root.geometry("900x510")
root.resizable(0, 0)

background = PhotoImage(file="896790.png")

back = Label(root, image=background).place(x=-50, y=-20, width=990, height=550)

clickhere = Button(root, text='Click Here', font=('Caliber', 20, 'bold'), bg='black', activebackground='black',
                   fg='#4AF96A', relief=GROOVE, bd=5, command=clickhere).place(x=370, y=400, width=200)

root.mainloop()
