from settings import get_random_npc

print("Dark Souls Npc generator!\n")

qtde = int(input('How many npcs you want to generate: '))

for i in range(qtde):
	print('------------------------------------------')
	print(f'\n{get_random_npc()}\n')
		
