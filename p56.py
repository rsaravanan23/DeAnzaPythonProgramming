# p56.py
# Rishi Saravanan
# Python 3.11.9
# Description:
'''
1) Type and run the following program:

2) You are given the encrypted sentence: CLGUBA VF TERNG

Using a Shift of 13, what is the original (decyphered) message?
'''

alphabet = ''
for i in range (65,91,1):
    alphabet += chr(i)
#print ("alphabet = ", alphabet)

shift = 13
print("shift = ", shift)


encrypted = ''

for i in range (65,91,1):

    if i + shift < 91:
        encrypted += chr(i + shift)
    if i + shift >= 91:
        encrypted += chr(65+(i + shift - 91))

#print("encrypted = ", encrypted)

encrypt = {}
decypher = {}
encrypt [' '] = ' '
decypher [' '] = ' '

for i in range (0,len(alphabet),1):
    encrypt [alphabet[i]] = encrypted[i]
    decypher [encrypted[i]] = alphabet[i]



original_message = ''
encrypted_message = "CLGUBA VF TERNG"

for i in range (0,len(encrypted_message),1):

    if encrypted_message[i] == ' ':
        original_message += ' '
    else:
        original_message += decypher[encrypted_message[i]]


#print("original message = ", original_message)
print("encrypt. message = ", encrypted_message)
print("... decyphered = ", end = '')

for i in range (0,len(encrypted_message),1):
    print(decypher[encrypted_message[i]],end = '')


'''

==== RESTART: C:/Users/rishi/AppData/Local/Programs/Python/Python311/p56.py ====
shift =  13
encrypt. message =  CLGUBA VF TERNG
... decyphered = PYTHON IS GREAT

'''

    
