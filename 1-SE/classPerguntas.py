from random import *
class Pergunta:
	def __init__(self):
		self.level = [
		['Seu Pet está agitado?','agitado'],
		['O seu Pet está comendo bem?','alimentado'],
		['O ambiente é adequado?','ambiente_adequado'],
		['O seu Pet fez atividade física?','se_movimenta'],		
		]

	def texto(self):
		string = self.level[0]
		del self.level[0]
		return string
