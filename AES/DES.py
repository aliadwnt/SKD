from Crypto.Cipher import DES
from Crypto.Util.Padding import pad

def procces_key(key) :
    return key[:8]

text = "Belajar AES"
key = procces_key(b'sayaariel')

BLOCK_SIZE = 8

des = DES.new(key, DES.MODE_ECB)
padded_text = pad(text.encode(), BLOCK_SIZE)
encrypted_text = des.encrypt(padded_text)
decrypted_text = des.decrypt(encrypted_text)

print("Plain Teks : ", text)
print("Hasil Enkripsi : ", encrypted_text)
print("Hasil Dekripsi : ", decrypted_text.decode())


# In[ ]:


# In[2]:


from Crypto.Cipher import DES
from Crypto.Util.Padding import pad

def process_key(key):
    return key[:8]

def bytes_to_letters(byte_array):
    # Convert bytes to a string of letters
    return ''.join([chr(byte % 26 + ord('A')) for byte in byte_array])

text = "Belajar AES"
key = process_key(b'sayaariel')

BLOCK_SIZE = 8

des = DES.new(key, DES.MODE_ECB)
padded_text = pad(text.encode(), BLOCK_SIZE)
encrypted_text = des.encrypt(padded_text)

# Convert encrypted bytes to letters
encrypted_letters = bytes_to_letters(encrypted_text)

decrypted_text = des.decrypt(encrypted_text)

print("Plain Teks : ", text)
print("Hasil Enkripsi : ", encrypted_letters)
print("Hasil Dekripsi : ", decrypted_text.decode())
