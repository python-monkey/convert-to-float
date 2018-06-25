def convert_to_float(zahl):
    if zahl.count('.') == 0:
		return float(zahl.replace(',','',(zahl.count(',')-1)).replace(',','.'))
    elif zahl.count(',') == 0:
		return float(zahl.replace('.','',(zahl.count('.')-1)))
	elif zahl.find(',') < zahl.find('.'):
		return float(zahl.replace(',',''))
	else:
		return float(zahl.replace('.','').replace(',','.'))