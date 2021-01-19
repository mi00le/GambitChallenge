import json

f = open('data.txt','r')


def variableNames():	
	dictVar =  {1: 'flow rate (m^3/h)',
				3: 'energy flow rate (GJ/h)',
				5: 'velocity (m/s)',
				7: 'fluid sound speed (m/s)',
				9: 'positive accumulator',
				11: 'positive decimal fraction',
				13: 'negative accumulator',
				15: 'negative decimal fraction',
				17: 'positive energy accumulator',
				19: 'positive energy decimal accumulator',
				21: 'negative energy accumulator',
				23: 'negative energy decimal accumulator',
				25: 'net accumulator',
				27: 'net decimal fraction',
				29: 'net energy accumulator',
				31: 'net energy decimal fraction',
				33: 'temperature inlet (C)',
				35: 'temperature outlet (C)',
				37: 'analog input AI3',
				39: 'analog input AI4',
				41: 'analog input AI5',
				43: 'current input at AI3 (mA)',
				45: 'current input at AI3 (mA)',
				47: 'current input at AI3 (mA)',
				49: 'system passowrd',
				51: 'password for hardware',
				53: 'calendar',
				56: 'day+hour for auto-save',
				59: 'key to input',
				60: 'go to window',
				61: 'LCD back-lit lights for number of seconds',
				62: 'times for the beeper',
				72: 'error code',
				77: 'PT100 resistance of inlet (Ohm)',
				79: 'PT100 resistance of outlet (Ohm)',
				81: 'total travel time (microSecond)',
				83: 'delta travel time (ninoSecond)',
				85: 'upstream travel time (microSecond)',
				87: 'downstream travel time (microSecond)',
				89: 'output current (mA)',
				92: 'working step and signal quality',
				93: 'upstream strength',
				94: 'downstream strength',
				96: 'language used',
				97: 'rate of measured travel time',
				99: 'reynolds number'}
	return dictVar



def convert2HumanData(machineData, dictVar):
	humanData = {}
	for key in machineData:
		if key in [1, 3, 5, 7, 11, 15, 19, 23, 27, 31, 33, 35, 37, 39, 41, 43,
					45, 47, 77, 79, 81, 83, 85, 87, 89, 97, 99]:

			# key:  1  regA:  7579
			regA = machineData[key]
			regB = machineData[key+1]


			humanData[dictVar[key]] = {"A": machineData[key], "human": real4Conversion(regA, regB)}
		elif key in [9, 13, 17, 21, 25, 29]:
			regA = machineData[key]
			regB = machineData[key+1]
			humanData[dictVar[key]] = {"A": machineData[key], "human": real4Conversion(regA, regB)}
		elif key in [49, 51, 53, 56]:
			if key == 53:
				humanData[dictVar[key]] = {"A": machineData[key], "human": [machineData[key], 
															machineData[key+1], machineData[key+2]]}

			elif key == 49:
				humanData[dictVar[key]] = {"A": machineData[key],"human": [machineData[key], machineData[key+1]]}

			else:
				humanData[dictVar[key]] = {"A": machineData[key], "human": machineData[key]}
		elif key in [59, 60, 61, 62, 92, 93, 94, 96]:
			regA = machineData[key]
			humanData[dictVar[key]] = {"A": machineData[key], "human": integerConversion(regA, key)}
		elif key == 72:
			humanData[dictVar[key]] = {"A": machineData[key],"human": machineData[key]}
	
	return humanData

def real4Conversion(regA, regB):

	# convert to binary

	bin_form = format(regB, '016b') + format(regA, '016b')

	# reverse sequence
	bin_form = bin_form[::-1]

	
	sign_value = 0.0
	exponent_value = 0.0
	fraction_value = 1.0


	for i in range(len(bin_form)):
		if i < 23:
			if int(bin_form[i]) == 1:
				# convert fraction value
				fraction_value += int(bin_form[i]) *2**(i-23)
		elif i >= 23 and i <= 30:
			exponent_value += int(bin_form[i]) *2**(i-23)
		else:
			sign_value = (-1)**int(bin_form[i])

	value = sign_value * fraction_value * 2**(exponent_value-127)
	return value


"""
Description of integerConversion:
	The function converts integer-type modbus data to human readable data.

Input:
	regA: The register value of a modbus data
	key: The corresponding key of regA

Output:
	Returns the corresponding human-value of regA.
"""

def integerConversion(regA, key):
	if key == 96:
		if regA == 0:
			return 'English'
		elif regA == 1:
			return 'Chinese'
		else:
			return 'Other language'

	elif key == 92:
		bin_form = format(regA, '016b')
		workingStepBin = bin_form[0:8]
		signalQualityBin = bin_form[8:16]
		return [int(workingStepBin, 2), int(signalQualityBin, 2)]
	else:
		return regA

def start():
	[datetimestamp,machineData] = readDataFile(f)
	dictVar = variableNames()
	humanData = convert2HumanData(machineData, dictVar)

	result = json.dumps(humanData) 
	s = open("output.txt", "w")
	input=result.replace('},','\n\n')
	s.write(input)





def readDataFile(txt):

	machineData = {}
	for line in txt:
		if '-' in line: 
			datetimestamp = line.split('\n')[0] # Extracting the datetime information from the url
		else:
			machineData[int(line.split(':')[0])] = int(line.split(':')[1])
	return [datetimestamp, machineData]


start()


