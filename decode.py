# coding: utf-8

import sys
import csv
import re

# open input file
redemet = open(sys.argv[1], 'r')
final_file = sys.argv[2]

data = []
datamax = 0
datamaxcond = 0
datamaxvento = 0

# tirar COR das mensagens (2013) - ok
# o vento (KT) pode ter um complemento que tem V ou G (pode aparecer ou não)  

# a visibilidade tambem pode vir assim: 7000 3000NW (N, S, E, O, NE, SE, NW, SW)
# VCSH

# decoding line information

print("# ----------- Começando tratamento ----------- ")

def decode_line(line):
	global datamax
	global datamaxcond
	global datamaxvento

	
	line = re.sub('(\d{2})(\d{2})(?= Q)', '\\1/\\2', line)
	line = re.sub('(Q\d{0,3}) ', '\\1', line)

	line = line.replace("=", "").strip()
	line = line.replace(" COR", "")
	lista = line.split(' ')

	print(lista)

	timestamp = lista[0]
	airport = lista[3]
	timezone = lista[4]
	dir_int = ''

	listvento = []
	
	
	weather = ''
	cloud_group = ''
	pressure = ''

	
	
	visibility = 'olarrr'
	#visibitily_comp = ''
	rerarets = 'na'

	complete_string = ''
	
	listc = []
	listcond = []
	

	for word in lista:

		if "KT" in word:
			dir_int = word
		elif len(word) == 2 or len(word) == 3:
			listcond.append(word)
		elif "SCT" in word or "FEW" in word or "BKN" in word or "OVC" in word:
			listc.append(word)
		elif "/" in word:
			t_td = word
		elif "Q" in word:
			pressure = word
		elif "RERA" in word or "RETS":
			rera = word
		elif "V" in word and len(word) == 7:
			listvento.append(word)
	
	if datamax < len(listc):
		datamax = len(listc) 

	if datamaxcond < len(listcond):
		datamaxcond = len(listcond)

	if datamaxvento < len(listvento):
		datamaxvento = len(listvento)

	complete_string = [timestamp, airport, timezone, dir_int, listvento, visibility, listcond, listc, t_td, pressure, rerarets]
	#print(complete_string)
	data.append(complete_string)


# iterating on redmet file
for observation in redemet:
	if "Mensagem METAR" not in observation:
		decode_line(observation)

for element in data:
	#print(element[4])
	while len(element[4]) <= datamaxvento:
		element[4].append("na")
	element[4] = ','.join(element[4])

	while len(element[6]) < datamaxcond:
		element[6].append("na")
	element[6] = ','.join(element[6])

	while len(element[7]) < datamax:
		element[7].append("na")
	element[7] = ','.join(element[7])



with open(final_file, 'w') as csvfile:
	fieldnames = ['Timestamp', 'Airport', 'Timezone', 'DirInten'] + ['Complven%d' % x for x in range(datamaxvento)] + ['Visibility'] + ['Weather%d' % x for x in range(datamaxcond)] + ['CG%d'% y for y in range(datamax)] + ['TTD', 'Pressure', 'ReraRets']
	
	csvfile.write(','.join(fieldnames) + "\n")

	for element in data:
		#print(element)
		csvfile.write(','.join(element) + "\n")


print("# ----------- Arquivo finalizado -----------")








