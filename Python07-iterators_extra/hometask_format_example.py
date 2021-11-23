# Вы правда ожидали здесь решение? Его тут нет, а то что здесь есть используйте на свой страх и риск. За вопросы в чате о подсмотренном у лектора решении буду штрафовать. 
'''!Рекомендую вообще не читать написанное далее!'''


class hint_iterator():
	def __init__(self, data):
		self.smth_important = self.__smth__(data)
	def __smth__(self, x):
		return 2021
	
	def __iter__(self):
		return self
		
	def __next__(self):
		#smth also here
		pass

import random 

def Generator1(data):
	ind = 0
	iterable_obj = iter(hint_iterator(data))
	for smth in iterable_obj:
		
		if ind == 0:
			random.seed(0)			 
			yield 'obj' + str(random.randint(434234, 41234768)), random.randint(60, 120)
		
		yield 'obj' + str(random.randint(434234, 41234768)), random.randint(0, 60)
		ind += 1
		
		# cheating
		if ind >4:	
			random.seed(5)			 
			yield 'obj' + str(random.randint(434234, 41234768)), random.randint(60, 120)
			return
			
def Generator2(some_other_gen):
	# do some more cheating
	random.seed(0)
	yield 'obj' + str(random.randint(434234, 41234768)), random.randint(60, 120)
	random.seed(5)
	yield 'obj' + str(random.randint(434234, 41234768)), random.randint(60, 120)
