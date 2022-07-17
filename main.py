# Name : Nachiket S Patel 
# Project : IMG Encryption and Decryption Using Triple DES.

from Crypto.Cipher import DES3
from hashlib import md5

while True:
    print('Choose operation to be done:\n\t1- Encryption\n\t2- Decryption')
    operation = input('Your Choice: ')
    if operation not in ['1', '2']:
        break
    file_path = input('File path: ')
       
       
    key = input('TDES key: ')

    key_hash = md5(key.encode('ascii')).digest()
  
    tdes_key = DES3.adjust_key_parity(key_hash)
   
    cipher = DES3.new(tdes_key, DES3.MODE_EAX, nonce=b'0')
    
    with open(file_path, 'rb') as input_file:
        file_bytes = input_file.read()
        
        if operation == '1':
            # Perform Encryption operation
            new_file_bytes = cipher.encrypt(file_bytes)
        else:
            # Perform Decryption operation
            new_file_bytes = cipher.decrypt(file_bytes)
     
    with open(file_path, 'wb') as output_file:
        output_file.write(new_file_bytes)
        print('Operation Done!')
        break    
# Code Complete!