from random import randint; from datetime import date
import json; import os
listanome = perfil = listacodigo = listaadm = []
cont = comidas = pagamento = preco = 0
pedido = endereco = forma = codigo = pedir = adm = 'y'
dia = date.today().day; mes = date.today().month; ano = date.today().year
pedir = str(input('Você deseja realizar um pedido em nossa loja? [ S / N ] - '))
while pedir in 'Ss':
    nome = str(input('Digite seu nome: ')).strip()
    comidas = int(input('''
!!! 15% DE DESCONTO NO PRIMEIRO PEDIDO !!!
                        
[1] Combo japonês................(R$ 69,90)
[2] Marmita......................(R$ 24,90)
[3] Combo Hambúrguer.............(R$ 44,90)
[4] Pizza........................(R$ 59,90)
[5] Açaí.........................(R$ 19,90)

Qual será o seu pedido hoje? - '''))
    pagamento = int(input('''
[1] Dinheiro
[2] Crédito 
[3] Débito (-10%)
[4] Pix (-15%)

Qual será sua forma de pagamento? - '''))
    if pagamento == 1:
        forma = 'Dinheiro'
    elif pagamento == 2:
        forma = 'Crédito'
    elif pagamento == 3:
        forma = 'Débito'
    elif pagamento == 4:
        forma = 'Pix'
    endereco = str(input('''
Qual o endereço de entrega? - '''))
    if comidas == 1:
        pedido = 'Combo japonês'
    elif comidas == 2:
        pedido = 'Marmita'
    elif comidas == 3:
        pedido = 'Combo Hambúrguer'
    elif comidas == 4:
        pedido = 'Pizza'
    elif comidas == 5:
        pedido = 'Açaí'
    if os.path.exists("listanome.json"):
        with open("listanome.json", "r") as arquivo:
            listanome = json.load(arquivo)
    nomecerto = ('').join(nome)
    listanome.append(nomecerto)
    cont = listanome.count(nomecerto)
    espacomais = len(nomecerto)
    perfil = [nomecerto, pedido, endereco]
    codigo = randint(715928519, 1259178590127)
    if comidas == 1:
        preco = 69.90
    elif comidas == 2:
        preco = 24.90
    elif comidas == 3:
        preco = 44.90
    elif comidas == 4:
        preco = 59.90
    elif comidas == 5:
        preco = 19.90
    if cont == 1:
        preco = preco - (15*preco)/100
        if pagamento == 3:
            preco = preco - (10*preco)/100
        elif pagamento == 4:
            preco = preco - (15*preco)/100
    if pagamento == 3:
            preco = preco - (10*preco)/100
    elif pagamento == 4:
            preco = preco - (15*preco)/100
    while codigo not in listacodigo:
        listacodigo.append(codigo)
    if codigo in listacodigo:
        listacodigo.remove(codigo)
        codigo = randint(715928519, 1259178590127)
        listacodigo.append(codigo)
    if cont == 1:
        print ('='*79, end=''), print ('='*espacomais)
        print (f'Essa é a sua 1° vez pedindo na nossa loja, obrigado pela confiança. Bem vindo {nomecerto}!')
        print ('='*79, end=''), print ('='*espacomais)
    elif cont > 1  and cont < 10:
        print ('='*63, end=''), print ('='*espacomais)
        print (f'Essa é a sua {cont}° vez pedindo na nossa loja, bem vindo de volta {nomecerto}!')
        print ('='*63, end=''), print ('='*espacomais)
    elif cont >= 10  and cont < 100:
        print ('='*64, end=''), print ('='*espacomais)
        print (f'Essa é a sua {cont}° vez pedindo na nossa loja, bem vindo de volta {nomecerto}!')
        print ('='*64, end=''), print ('='*espacomais)
    elif cont >= 100  and cont < 1000:
        print ('='*65, end=''), print ('='*espacomais)
        print (f'Essa é a sua {cont}° vez pedindo na nossa loja, bem vindo de volta {nomecerto}!')
        print ('='*65, end=''), print ('='*espacomais)
    print (f'''Seu pedido foi cadastrado com sucesso! {perfil} Dia: {dia}.{mes}.{ano}
*''')
    if pagamento > 1:
        print (f'''Seu pagamento de R${preco:.2f} deverá ser efetuado via {forma}.
*''')
        print (f'O código do seu pedido é: {codigo}')
    elif pagamento == 1:
        print (f'''Seu pagamento de R${preco:.2f} será efetuado via {forma} no endereço {endereco}.
*''')
        print (f'O código do seu pedido é: {codigo}')
    with open("listanome.json", "w") as arquivo:
        json.dump(listanome, arquivo)
    pedir = 'y'
    pedir = str(input('Você deseja realizar outro pedido em nossa loja? [ S / N ] - '))