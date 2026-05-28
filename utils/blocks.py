from utils.utils import *

identifiers = {
    1000 : ("POD Version Block", read_null_terminated_string),
    1001 : ("Scene Data Block", None),
    1002 : ("Export Options Block", read_null_terminated_string),
    1003 : ("History Block", read_null_terminated_string),

    2000 : ("Clear Colour", process_32_bit_real_number_array), # Colour
    2001 : ("Ambient Colour", process_32_bit_real_number_array), # Colour
    2002 : ("Num. Cameras", read_unsigned_32_bit_int), 
    2003 : ("Num. Lights", read_unsigned_32_bit_int),
    2004 : ("Num. Meshes", read_unsigned_32_bit_int), 
    2005 : ("Num. Nodes", read_unsigned_32_bit_int), 
    2006 : ("Num. Mesh Nodes", read_unsigned_32_bit_int),
    2007 : ("Num. Textures", read_unsigned_32_bit_int), 
    2008 : ("Num. Materials", read_unsigned_32_bit_int),
    2009 : ("Num. Frames", read_unsigned_32_bit_int),
    
    2010 : ("Camera", None), 
    2011 : ("Light", None), 
    2012 : ("Mesh", None), 
    2013 : ("Node", None),  
    2014 : ("Texture", None),  
    2015 : ("Material", None), 
    2016 : ("Scene Flags", read_unsigned_32_bit_int), 
    2017 : ("FPS", read_unsigned_32_bit_int),
    
    # MATERIAL BLOCKS
    3000 : ("Material Name", read_null_terminated_string),
    3001 : ("Diffuse Texture Index", read_signed_32_bit_int),
    3002 : ("Material Opacity", read_float), # Float/Fixed
    3003 : ("Ambient Colour", process_32_bit_real_number_array), # Float/Fixed Array
    3004 : ("Diffuse Colour", process_32_bit_real_number_array), # Float/Fixed Array
    3005 : ("Specular Colour", process_32_bit_real_number_array), # Float/Fixed Array
    3006 : ("Shininess", read_float), # Float/Fixed
    3007 : ("Effect File Name", read_null_terminated_string),
    3008 : ("Effect Name", read_null_terminated_string),
    3009 : ("Ambient Texture Index", read_signed_32_bit_int),
    3010 : ("Specular Colour Texture Index ", read_signed_32_bit_int),
    3011 : ("Specular Level Texture Index", read_signed_32_bit_int),
    3012 : ("Bump Map Texture Index", read_signed_32_bit_int),
    3013 : ("Emissive Texture Index", read_signed_32_bit_int),
    3014 : ("Glossiness Texture Index", read_signed_32_bit_int),
    3015 : ("Opacity Texture Index", read_signed_32_bit_int),
    3016 : ("Reflection Texture Index", read_signed_32_bit_int),
    3017 : ("Refraction Texture Index", read_signed_32_bit_int),
    3018 : ("Blending RGB Source Value ", read_signed_32_bit_int), # Float/Fixed
    3019 : ("Blending Alpha Source Value", return_hex_data), # Float/Fixed
    3020 : ("Blending RGB Destination Value", return_hex_data), # Float/Fixed
    3021 : ("Blending RGB Destination Value", return_hex_data), # Float/Fixed
    3022 : ("Blending RGB Operation", return_hex_data), # Float/Fixed
    3023 : ("Blending Alpha Operation", return_hex_data), # Float/Fixed
    3024 : ("Blending RGBA Colour", process_32_bit_real_number_array), # Float/Fixed
    3025 : ("Blending Factor Array", process_32_bit_real_number_array), # Float/Fixed
    3026 : ("Material Flags", return_hex_data), # Float/Fixed
    3027 : ("User Data", return_hex_data), # Float/Fixed
    3028 : ("Metallicity", return_hex_data), # Float/Fixed
    3029 : ("Roughness", return_hex_data), # Float/Fixed
    3030 : ("IOR", read_float), # Float
    3032 : ("Reflectivity", read_float), # Float
    3033 : ("SubSurface Scattering", read_float), # Float
    3034 : ("SubSurface Scattering Depth", read_float), # Float
    3035 : ("SubSurface Scattering Colour", return_hex_data), # Float Array
    3036 : ("Emission", read_float), # Float/Fixed
    3037 : ("Emission Luminance", read_float), # Float/Fixed
    3040 : ("Metallicity Texture Index", read_signed_32_bit_int), 
    3041 : ("Roughness Texture Index", read_signed_32_bit_int), 
    
    # TEXTURE BLOCKS
    4000 : ("Texture Name", read_null_terminated_string), 
    
    # NODE BLOCKS
    5000 : ("Node Index", read_signed_32_bit_int), 
    5001 : ("Node Name", read_null_terminated_string), 
    5002 : ("Material Index", read_signed_32_bit_int), 
    5003 : ("Parent Index", read_signed_32_bit_int), 
    5007 : ("Animation Position", process_32_bit_real_number_array), 
    5008 : ("Animation Rotation", process_32_bit_real_number_array),
    5010 : ("Animation Matrix", process_32_bit_real_number_array),
    5012 : ("Animation Flags", read_unsigned_32_bit_int), 
    5013 : ("Animation Position Index", process_signed_32_bit_int_array), 
    5014 : ("Animation Rotation Index", process_signed_32_bit_int_array),
    5015 : ("Animation Scale Index", process_signed_32_bit_int_array),
    5016 : ("Animation Matrix Index", process_signed_32_bit_int_array),
    5017 : ("User Data", ),
    5019 : ("Animation Scale", process_32_bit_real_number_array),
    
    # MESH BLOCKS
    6000 : ("Num. Vertices", read_unsigned_32_bit_int), 
    6001 : ("Num. Faces", read_unsigned_32_bit_int), 
    6002 : ("Num. UVW Channels", read_unsigned_32_bit_int), 
    6003 : ("Vertex Index List", None), # POD Data block
    6004 : ("Strip Length", process_unsigned_32_bit_int_array), 
    6005 : ("Num. Strip", read_unsigned_32_bit_int), 
    6006 : ("Vertex List", None), # POD Data Block
    6007 : ("Normal List", None), # POD Data Block
    6008 : ("Tangent List", None), # POD Data Block
    6009 : ("Binormal List", None), # POD Data Block
    6010 : ("UVW List", None), # POD Data Block
    6011 : ("Vertex Colour List", None), # POD Data Block
    6012 : ("Bone Index List", None), # POD Data Block
    6013 : ("Bone Weights", None), # POD Data Block
    6014 : ("Interleaved Data List", return_hex_data), # POD Data Block
    6015 : ("Bone Batch Index List", return_hex_data), # POD Data Block
    6016 : ("Num. Bone Indices per Batch", return_hex_data), # POD Data Block
    6017 : ("Bone Offset per Batch", return_hex_data), # POD Data Block
    6018 : ("Max. Num. Bones per Batch", return_hex_data), # POD Data Block
    6019 : ("Num. Bone Batches", return_hex_data), # POD Data Block
    6020 : ("Unpack Matrix", process_float_array), 
    6021 : ("Mesh Type", read_unsigned_32_bit_int),
    6022 : ("Adjacency Index List", None), # POD Data Block
    
    # LIGHT BLOCKS
    7000 : ("Target Object Index ", read_unsigned_32_bit_int),
    7001 : ("Light Colour", process_32_bit_real_number_array),
    7002 : ("Light Type", read_unsigned_32_bit_int),
    7003 : ("Constant Attenuation", read_float),
    7004 : ("Linear Attenuation", read_float),
    7005 : ("Quadratic Attenuation", read_float),
    7006 : ("Falloff Angle", read_float),
    7007 : ("Falloff Exponent ", read_float),
    
    # CAMERA BLOCKS
    8000 : ("Target Object Index", read_unsigned_32_bit_int),
    8001 : ("Field of View", read_float),
    8002 : ("Far Plane", read_float),
    8003 : ("Near Plane", read_float),
    8004 : ("FOV Animation", return_hex_data), #ARRAY
    
    # POD DATA BLOCKS 
    9000 : ("Data Type", process_pod_data_block_key), 
    9001 : ("Num. Components", process_pod_data_block_key), 
    9002 : ("Stride", process_pod_data_block_key), 
    9003 : ("Data", return_hex_data),
}

data_block_type = {
    0 : None,
    1 : read_float,
    2 : read_unsigned_32_bit_int,
    3 : read_unsigned_short,
    4 : "RGBA",
    5 : "ARGB",
    6 : "D3DCOLOR",
    7 : "UBYTE4",
    8 : "DEC3N",
    9 : read_fixed_1616,
    10: read_unsigned_byte,
    11: read_signed_short,
    12: "normalised short",
    13: read_signed_byte,
    14: "normalised byte",
    15: "unsigned normalised byte",
    16: "unsigned normalised short",
    17: "unsigned integer"
}