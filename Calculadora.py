from tkinter import *

#Início do Programa
root = Tk()
root.title("Calculadora")

#Funções dos botões
def Clique(numero):
    digitos = tela.get()
    tela.delete(0, END)
    tela.insert(0, str(digitos) + str(numero))

def Limpar():
    tela.delete(0, END)

def Apagar():
    numero = tela.get()[:-1]
    tela.delete(0, END)
    tela.insert(0, numero)
    if numero == "":
        tela.insert(0, "0")


def Adicao():
    add1 = tela.get()
    global numadd1
    global matematica
    matematica = "add"
    numadd1 = int(add1)
    tela.delete(0, END)

def Subtracao():
    sub1 = tela.get()
    global numsub1
    global matematica
    matematica = "sub"
    numsub1 = int(sub1)
    tela.delete(0, END)

def Multiplicacao():
    mul1 = tela.get()
    global nummul1
    global matematica
    matematica = "mul"
    nummul1 = int(mul1)
    tela.delete(0, END)

def Divisao():
    div1 = tela.get()
    global numdiv1
    global matematica
    matematica = "div"
    numdiv1 = int(div1)
    tela.delete(0, END)

def Igual():
    x = tela.get()
    num2 = int(x)
    tela.delete(0, END)
    if matematica == "add":
        tela.insert(0, numadd1 + num2)
    elif matematica == "sub":
        tela.insert(0, numsub1 - num2)
    elif matematica == "mul":
        tela.insert(0, nummul1 * num2)
    elif matematica == "div":
        tela.insert(0, numdiv1 / num2)


#Definição dos itens
tela = Entry(root, width=12, font=("courier", 46))
botao_1 = Button(root, text="1", font="courier", padx=45, pady=45, command=lambda: Clique(1))
botao_2 = Button(root, text="2", font="courier", padx=45, pady=45, command=lambda: Clique(2))
botao_3 = Button(root, text="3", font="courier", padx=45, pady=45, command=lambda: Clique(3))
botao_4 = Button(root, text="4", font="courier", padx=45, pady=45, command=lambda: Clique(4))
botao_5 = Button(root, text="5", font="courier", padx=45, pady=45, command=lambda: Clique(5))
botao_6 = Button(root, text="6", font="courier", padx=45, pady=45, command=lambda: Clique(6))
botao_7 = Button(root, text="7", font="courier", padx=45, pady=45, command=lambda: Clique(7))
botao_8 = Button(root, text="8", font="courier", padx=45, pady=45, command=lambda: Clique(8))
botao_9 = Button(root, text="9", font="courier", padx=45, pady=45, command=lambda: Clique(9))
botao_0 = Button(root, text="0", font="courier", padx=45, pady=45, command=lambda: Clique(0))
botao_mais = Button(root, text="+", font="courier", padx=45, pady=45, command=lambda: Adicao())
botao_menos = Button(root, text="-", font="courier", padx=45, pady=45, command=lambda: Subtracao())
botao_vezes = Button(root, text="X", font="courier", padx=45, pady=45, command=lambda: Multiplicacao())
botao_dividir = Button(root, text="÷", font="courier", padx=45, pady=45, command=lambda: Divisao())
botao_apagar = Button(root, text="←", font="courier", padx=45, pady=45, command=lambda: Apagar())
botao_limpar = Button(root, text="↺", font="courier", padx=45, pady=45, command=lambda: Limpar())
botao_igual = Button(root, text="=", font="courier", padx=220, pady=45, command=lambda: Igual())



#Layout do Grid
tela.grid(column=1, columnspan=4, row=1)
botao_7.grid(column=1, row=2)
botao_8.grid(column=2, row=2)
botao_9.grid(column=3, row=2)
botao_mais.grid(column=4, row=2)
botao_4.grid(column=1, row=3)
botao_5.grid(column=2, row=3)
botao_6.grid(column=3, row=3)
botao_menos.grid(column=4, row=3)
botao_1.grid(column=1, row=4)
botao_2.grid(column=2, row=4)
botao_3.grid(column=3, row=4)
botao_vezes.grid(column=4, row=4)
botao_limpar.grid(column=1, row=5)
botao_0.grid(column=2, row=5)
botao_apagar.grid(column=3, row=5)
botao_dividir.grid(column=4, row=5)
botao_igual.grid(column=1, columnspan=4, row=6)

#loop
root.mainloop()
