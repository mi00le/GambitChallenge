import struct
import binascii

f = open('data.txt','r')


input_list = [(1,2),(3,4),(5,6),(7,8),(9,10),(11,12),(13,14),(15,16),(17,18),(19,20),(21,22),(23,24),(25,26),(27,28),(29,30),(31,32),(33,34),(35,36),(37,38),(39,40),(41,42),(43,44),(45,46),(47,48),(49,50),(51,),(53,55),(56,),(59,),(60,),(61,),(62,),(72,),(77,78),(79,80),(81,82),(83,84),(85,86),(87,88),(89,90),(92,),(93,),(94,),(96,),(97,98),(99,100)]

# https://docs.python.org/3/library/struct.html

def start():
    [date,data] = readDataFile(f)
    humanData = (data)

    def reg_to_float(reg_1, reg_2):

        #registers into hex strings
        hex_1 = hex(int(reg_2))[2:]
        hex_2 = hex(int(reg_1))[2:]
        #String concat
        the_hex = hex_1 + hex_2
        return struct.unpack('>f', binascii.unhexlify(the_hex))[0]

    def reg_to_long(reg_1, reg_2):

        #registers into hex strings
        hex_1 = hex(int(reg_2))[2:]
        hex_2 = hex(int(reg_1))[2:]
        #String concat
        the_hex = hex_1 + hex_2
        if len(the_hex) == (8):      
            return struct.unpack('>l', binascii.unhexlify(the_hex))[0]
        else:
            return int(the_hex)
   
    def reg_to_int(reg):
        bin_str = bin(reg)
        #Last four bits, the 2 argument means that its using binary
        return int(bin_str[4:],2)
    
    def reg_to_integer(reg):
        bin_str = bin(reg)
        return int(bin_str,2)

    def reg_to_bcd(reg):
        bin_str = bin(reg)
        return int(bin_str,2)

    def two_reg_to_bcd(reg_1, reg_2):
        hex_1 = hex(int(reg_2))[2:]
        hex_2 = hex(int(reg_1))[2:]
        #String concat
        the_hex = hex_1 + hex_2
        return int(the_hex,16)

    for i in input_list:
        if i == (92,):         
            reg_value = humanData[92]
            decode = reg_to_int(reg_value)
            print (i, decode)
        elif i == (59,):
            reg_value = humanData[59]
            decode = reg_to_integer(reg_value)
            print (i, decode)
        elif i == (60,):
            reg_value = humanData[60]
            decode = reg_to_integer(reg_value)
            print (i, decode)
        elif i == (61,):
            reg_value = humanData[61]
            decode = reg_to_integer(reg_value)
            print (i, decode)
        elif i == (62,):
            reg_value = humanData[62]
            decode = reg_to_integer(reg_value)
            print (i, decode)
        elif i == (93,):
            reg_value = humanData[93]
            decode = reg_to_integer(reg_value)
            print (i, decode)
        elif i == (94,):
            reg_value = humanData[94]
            decode = reg_to_integer(reg_value)
            print (i, decode)
        elif i == (96,):
            reg_value = humanData[96]
            decode = reg_to_integer(reg_value)
            print (i, decode)
    #Function calls for converting register input values into Binary code decimal

        elif i == (51,):
            reg_value = humanData[51]
            decode = reg_to_bcd(reg_value)
            print (i, decode)
        elif i == (56,):
            reg_value = humanData[56]
            decode = reg_to_bcd(reg_value)
            print (i, decode)
        elif i == (53,55):
            reg_value_1 = humanData[53]
            reg_value_2 = humanData[55]
            decode = two_reg_to_bcd(reg_value_1, reg_value_2)
            print (i, decode)
        elif i == (49,50):
            reg_value_1 = humanData[49]
            reg_value_2 = humanData[50]
            decode = two_reg_to_bcd(reg_value_1, reg_value_2)
            print (i, decode)        

    #Function calls for converting register input values into LONG        
        elif i == (21,22):
            reg_value_1 = humanData[21]
            reg_value_2 = humanData[22]
            decode = reg_to_long(reg_value_1, reg_value_2)
            print (i, decode)
        elif i == (9,10):
            reg_value_1 = humanData[9]
            reg_value_2 = humanData[10]
            decode = reg_to_long(reg_value_1, reg_value_2)
            print (i, decode)
        elif i == (13,14):
            reg_value_1 = humanData[13]
            reg_value_2 = humanData[14]
            decode = reg_to_long(reg_value_1, reg_value_2)
            print (i, decode)
        elif i == (17,18):
            reg_value_1 = humanData[17]
            reg_value_2 = humanData[18]
            decode = reg_to_long(reg_value_1, reg_value_2)
            print (i, decode)
        elif i == (25,26):
            reg_value_1 = humanData[25]
            reg_value_2 = humanData[26]
            decode = reg_to_long(reg_value_1, reg_value_2)
            print (i, decode)
        elif i == (29,30):
            reg_value_1 = humanData[29]
            reg_value_2 = humanData[30]
            decode = reg_to_long(reg_value_1, reg_value_2)
            print (i, decode)

    #Function calls for converting register input values into REAL4 format       
        elif i == (1,2):
            reg_value_1 = humanData[1]
            reg_value_2 = humanData[2]
            decode = reg_to_float(reg_value_1, reg_value_2)
            print (i, decode)
        elif i == (3,4):
            reg_value_1 = humanData[3]
            reg_value_2 = humanData[4]
            decode = reg_to_float(reg_value_1, reg_value_2)
            print (i, decode)
        elif i == (5,6):
            reg_value_1 = humanData[5]
            reg_value_2 = humanData[6]
            decode = reg_to_float(reg_value_1, reg_value_2)
            print (i, decode)
        elif i == (7,8):
            reg_value_1 = humanData[7]
            reg_value_2 = humanData[8]
            decode = reg_to_float(reg_value_1, reg_value_2)
            print (i, decode)
        elif i == (11,12):
            reg_value_1 = humanData[11]
            reg_value_2 = humanData[12]
            decode = reg_to_float(reg_value_1, reg_value_2)
            print (i, decode)
        elif i == (19,20):
            reg_value_1 = humanData[19]
            reg_value_2 = humanData[20]
            decode = reg_to_float(reg_value_1, reg_value_2)
            print (i, decode) 
        elif i == (23,24):
            reg_value_1 = humanData[23]
            reg_value_2 = humanData[24]
            decode = reg_to_float(reg_value_1, reg_value_2)
            print (i, decode)
        elif i == (31,32):
            reg_value_1 = humanData[31]
            reg_value_2 = humanData[32]
            decode = reg_to_float(reg_value_1, reg_value_2)
            print (i, decode)
        elif i == (35,36):
            reg_value_1 = humanData[35]
            reg_value_2 = humanData[36]
            decode = reg_to_float(reg_value_1, reg_value_2)
            print (i, decode) 
        elif i == (33,34):
            reg_value_1 = humanData[33]
            reg_value_2 = humanData[34]
            print(reg_value_1,reg_value_2)
            decode = reg_to_float(reg_value_1, reg_value_2)
            print (i, decode)
        elif i == (37,38):
            reg_value_1 = humanData[37]
            reg_value_2 = humanData[38]
            decode = reg_to_float(reg_value_1, reg_value_2)
            print (i, decode)
        elif i == (39,40):
            reg_value_1 = humanData[39]
            reg_value_2 = humanData[40]
            decode = reg_to_float(reg_value_1, reg_value_2)
            print (i, decode)
        elif i == (41,42):
            reg_value_1 = humanData[41]
            reg_value_2 = humanData[42]
            decode = reg_to_float(reg_value_1, reg_value_2)
            print (i, decode)
        elif i == (43,44):
            reg_value_1 = humanData[43]
            reg_value_2 = humanData[44]
            decode = reg_to_float(reg_value_1, reg_value_2)
            print (i, decode)
        elif i == (45,46):
            reg_value_1 = humanData[43]
            reg_value_2 = humanData[44]
            decode = reg_to_float(reg_value_1, reg_value_2)
            print (i, decode)
        elif i == (47,48):
            reg_value_1 = humanData[47]
            reg_value_2 = humanData[48]
            decode = reg_to_float(reg_value_1, reg_value_2)
            print (i, decode)



def readDataFile(txt):

    data = {}
    for line in txt:
        if '-' in line: 
            date = line.split('\n')[0] 
        else:
            data[int(line.split(':')[0])] = int(line.split(':')[1])
    return [date, data]


start()


