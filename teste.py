import csv


data = ['2011060100,SBKG,010000Z,15007KT,CAVOK,,,22/20,Q1016,NULL', '2011060101,SBKG,010100Z,15008KT,CAVOK,,,21/20,Q1016,NULL', '2011060102,SBKG,010200Z,16007KT,CAVOK,,,21/20,Q1015,NULL', '2011060103,SBKG,010300Z,15008KT,CAVOK,,,21/20,Q1015,NULL', '2011060109,SBKG,010915Z,12003KT,9999,,SCT010,21/20,Q1015,NULL', '2011060110,SBKG,011000Z,13007KT,9999,,SCT010BKN015,23/21,Q1015,NULL', '2011060111,SBKG,011100Z,14006KT,9999,,SCT015BKN018,24/21,Q1016,NULL', '2011060112,SBKG,011200Z,14006KT,9999,,SCT015BKN018,24/21,Q1016,NULL', '2011060113,SBKG,011300Z,17011KT,9999,,SCT015BKN018,26/21,Q1016,NULL', '2011060114,SBKG,011400Z,13011KT,5000,-RABR,SCT010BKN015,23/21,Q1015,NULL']


#for element in data:
#	final_string = element.split(",")
#	print(final_string[0])

with open('saida.csv', 'w') as csvfile:
	fieldnames = ['Timestamp', 'Airport', 'Timezone', 'DirInten', 'Visibility', 'Weather', 'CG', 'TTD', 'Pressure', 'ReraRets']
	writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
	writer.writeheader()
	
	for element in data:
		fs = element.split(",")
		writer.writerow({'Timestamp':fs[0], 'Airport':fs[1], 'Timezone':fs[2], 'DirInten':fs[3], 'Visibility':fs[4], 'Weather':fs[5], 'CG':fs[6], 'TTD':fs[7], 'Pressure':fs[8], 'ReraRets':fs[9]})





