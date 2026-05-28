import struct
# SE ASUME QUE LOS DATOS BINARIOS ESTÁN REPRESENTADOS EN LITTLE ENDIAN

# Solo funciona cuando la division entre el tamaño del 
# array y el numero de partes a dividir es exacto
def split_byte_array(size, data):
    to_return = []
    length = len(data)
    begining = 0
    end = size
    
    while end <= length:
        to_return.append(data[begining:end])
        begining = end
        end += size
    
    return to_return
 
def read_float(data):
    return struct.unpack('<f', data)[0]

def read_fixed_1616(data):
    return read_unsigned_32_bit_int(data)/pow(2, 16)

def read_unsigned_32_bit_int(data):
    return struct.unpack('<I', data)[0]

def read_signed_32_bit_int(data):
    return struct.unpack('<i', data)[0]

def read_unsigned_short(data):
    return struct.unpack('<H', data)[0]

def read_signed_short(data):
    return struct.unpack('<h', data)[0]

def read_signed_byte(data):
    return struct.unpack('<b', data)[0]

def read_unsigned_byte(data):
    return struct.unpack('<B', data)[0]

def read_null_terminated_string(data):
    return data[0:-1].decode("utf-8")

def process_32_bit_real_number_array(data):
    return split_byte_array(4, data)

def process_signed_32_bit_int_array(data):
    splited_array = split_byte_array(4, data)
    toret = []
    for pos in splited_array:
        toret.append(read_signed_32_bit_int(pos))
        
    return toret

def process_unsigned_32_bit_int_array(data):
    splited_array = split_byte_array(4, data)
    toret = []
    for pos in splited_array:
        toret.append(read_unsigned_32_bit_int(pos))
        
    return toret

def process_float_array(data):
    splited_array = split_byte_array(4, data)
    toret = []
    for pos in splited_array:
        toret.append(read_float(pos))
        
    return toret

def return_hex_data(data):
    return data

def process_pod_data_block_key(data, key=None):
    pass