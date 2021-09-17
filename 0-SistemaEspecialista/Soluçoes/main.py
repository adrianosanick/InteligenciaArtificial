from classDiagnostico import *
from classPerguntas import *

se = Diagnostico()
pergunta = Pergunta()


while se.probabilidade() != 100:
	string = pergunta.texto()
	se.pergunta(string[0],string[1])
	print('probabilidade é %d' %(se.probabilidade()))
	print(se.resultado)
	if se.probabilidade() == 100:
		print('O seu Pet está: ',se.resultado[0])	