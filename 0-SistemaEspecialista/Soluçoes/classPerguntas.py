from random import *
class Pergunta:
	def __init__(self):
		self.level = [
		['O seu parente é um homem?','homem'],
		['O seu parente é filho do teu irmão ou irmã?','filhoirmao'],
		['O seu parente é filho(a) do seu pai ou mãe?','filhopaimae'],
		['O seu parente é filho(a) de sua tia ou tio?','filhotioa'],
		['O seu parente é filho(a) de seu primo ou prima?', 'filhoprimoa'],
		['O seu parente é filho da seu avô ou avó?','filhoavoa'],		
		]

	def texto(self):
		string = self.level[0]
		del self.level[0]
		return string
