import streamlit as st
import time
import pandas as pd

def decrypt(ciphertext, shift):
    decrypted = []
    shift = shift % 26  #To ensure proper shift
    
    for char in ciphertext:
        if char.isalpha():  
            if char.islower():  
                decrypted.append(chr((ord(char) - ord('a') - shift) % 26 + ord('a')))
            elif char.isupper():  
                decrypted.append(chr((ord(char) - ord('A') - shift) % 26 + ord('A')))
        else:
            decrypted.append(char)
    return ''.join(decrypted)

def bruteforce(ciphertext):
    results = []
    for i in range(1, 26): 
        results.append((i, decrypt(ciphertext, i)))
    return results

# Streamlit UI
st.title("Caesar Cipher Decryption")
ciphertext = st.text_input("Enter the ciphertext:")

if st.button("Decrypt"):
    if ciphertext:
        start_time = time.time()
        results = bruteforce(ciphertext)
        end_time = time.time()
        time_taken = end_time - start_time
        
        st.write("Attempting to brute force Caesar Cipher:")
        
        df_results = pd.DataFrame(results, columns=['Shift', 'Decrypted Text'])
        st.dataframe(df_results, hide_index = True, use_container_width = True) 

        #Display the time taken
        st.write(f"Time taken to brute force: {time_taken:.5f} seconds")
    else:
        st.warning("Please enter a ciphertext to decrypt.")
