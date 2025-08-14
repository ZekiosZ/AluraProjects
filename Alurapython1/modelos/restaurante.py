class Restaurante:
    nome=""
    categoria=""
    ativo = False
restaurante_praca=Restaurante()
restaurante_praca.nome="Bistrô"
restaurante_praca.categoria="Italiana"
restaurante_praca.ativo=True

restaurante_pizza=Restaurante()
restaurante_pizza.nome="Pizza Place"
restaurante_pizza.categoria="Fast Food"
restaurante_pizza.ativo=True
#separação

categoria=Restaurante.categoria

#Os Testes vou colocar em comentarios
'''if restaurante_praca.ativo==False:
    print("O restaurante esta inativo")
else:
    print("O restaurante esta ativo")
    '''
print("Nome do restaurante:",restaurante_praca.nome,"\nCategoria do restaurante:", restaurante_praca.categoria)