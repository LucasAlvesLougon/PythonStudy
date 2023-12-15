# If...Else statements, Operadores Lógicos e Comparação

#tenho_sede = False

#if tenho_sede:
#    print("Beber agua")

#print("Vida que segue")

#esta_frio = True

#if esta_frio:
#    print("Vestir um casaco")
#else:
#    print("Vestir camiseta")

tenho_sede = True
tenho_fome = False
estou_em_dieta = False

'''if tenho_sede or tenho_fome:  # Operador lógico OR(ou)
    print("Vou na cozinha")
else:
    print("Fico vendo netflix")'''

'''if tenho_sede and tenho_fome: # Operador lógico AND(e)
    print("Vou na cozinha")
else:
    print("Fico vendo netflix")'''

'''if tenho_sede and tenho_fome:
    print("Fazer sanduiche e coca")
elif tenho_sede and not(tenho_fome): # Operador de negação NOT(Não)
    if estou_em_dieta:
        print("Tomar agua")
    else:
        print("Tomar uma coquinha")
elif not(tenho_sede) and (tenho_fome):
    print("Fazer um sanduiche")
else:
    print("Ficar vendo netflix")'''

num1 = 5
num2 = 32

'''if num1 == num2:
    print("num1 é igual a num2")
elif num1 != num2:
    print("num1 é diferente de num2")'''

if num1 >= num2:
    print("num1 é maior que num2")
elif num1 <= num2:
    print("num1 é menor que num2")


''' Operadores logicos
or -> ou 
and -> e
not -> negação'''

''' Operadores de comparação
== -> igual
!= -> diferente
>  -> maior
<  -> menor
>= -> maior ou igual
<= -> menor ou igual'''