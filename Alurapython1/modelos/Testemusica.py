class Musica:
    nome=""
    artista=""
    duracao=""

badromance=Musica()
badromance.artista="LadyGaga"
badromance.nome="BadRomance"
badromance.duracao="4 minutos e 54 segundos"
#espaço
prettygirl=Musica()
prettygirl.nome="PrettyGirl"
prettygirl.artista="Clairo"
prettygirl.duracao="3 minutos"
#espaço
feelgood=Musica()
feelgood.nome="FeelGood INC."
feelgood.artista="Gorillaz"
feelgood.duracao="3 minutos e 41 segundos"
#espaço

musicas=[badromance, prettygirl, feelgood]
print(vars(badromance))