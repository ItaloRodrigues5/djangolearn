print("Hello World!")

print()

#Invertendo caracteres de uma string

xuxa = "Daniel Orivaldo da Silva"

xuxainvertida = "".join(reversed(xuxa)) #Usando método nativo

print(xuxainvertida)

print()

xuxainvertida2 = xuxa[::-1] #Usando lista

print(xuxainvertida2)

#Liberação para rodar ambiente virtual do Django colocando no PowerShell do VS Code
#Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

#Liberação para rodar ambiente virtual do Django colocando no PowerShell do Windows
#Set-ExecutionPolicy Unrestricted