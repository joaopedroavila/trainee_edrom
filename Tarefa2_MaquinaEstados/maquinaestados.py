#codigo
from transitions import Machine

class DayToDay(object):
	pass
universitario = DayToDay()



#estados
states=['dormindo', 'tomandocafe', 'estudando', 'bebendo']

#transições
transitions = [
	{'trigger': 'acordar', 'source': 'dormindo', 'dest': 'tomandocafe'},
	{'trigger': 'provaamanha', 'source': 'tomandocafe', 'dest': 'estudando'},
	{'trigger': 'cansei', 'source': 'estudando', 'dest': 'dormindo'},
	{'trigger': 'nadaprafazer', 'source': 'dormindo', 'dest': 'bebendo'},
	{'trigger': 'malzao', 'source': 'bebendo', 'dest': 'dormindo'},
]

#definindo minha maquina
machine = Machine(model=universitario, states=states, transitions=transitions, initial='dormindo')

#mudando os estados

universitario.state	#deve dizer dormindo
print(universitario.state)
universitario.trigger('acordar')
universitario.state	#tomando cafe
print(universitario.state)
universitario.provaamanha()
print(universitario.state)