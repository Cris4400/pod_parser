from utils.utils import *
from utils.blocks import *
from model.raw_pod_block import *

tag_size = 8

ending_tag_mask = 0x80
identifier_mask = 0x7FFFFFFF 

def pod_reader(input_file):
    result = None
    with open(input_file, 'rb') as file:
        result = pod_binary_reader(file, None)
        
    return result          

def pod_binary_reader(input_file, id):
    reading_tag = True
    data_lenght = 8
    identifier = None
    
    toret = []
    
    while True:
        block = input_file.read(data_lenght)
        
        if not block and data_lenght != 0:
            break
        
        if reading_tag:
            splited_tag = split_byte_array(4, block)
            first_dword = splited_tag[0]
            second_dword = splited_tag[1]
            
            identifier = read_unsigned_32_bit_int(first_dword) & identifier_mask
            is_ending_tag = (first_dword[3] & ending_tag_mask) == 128
            
            if is_ending_tag and identifier == id:
                break
            
            if is_ending_tag:
                continue
            
            data_lenght = read_unsigned_32_bit_int(second_dword)
            reading_tag = False
            continue
        
        name = identifiers.get(identifier, None)
        if not name:
            data_lenght = 8
            reading_tag = True
            continue
        
        if data_lenght == 0:
            toret.append(RawPodBlock(identifier, name[0], None, [pod_binary_reader(input_file, identifier)]))
        else: 
            toret.append(RawPodBlock(identifier, name[0], block, []))
            
        reading_tag = True
        data_lenght = 8   
  
    return toret     