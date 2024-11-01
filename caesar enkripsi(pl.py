def caesar_enkripsi(plaintext, kunci):
    hasil_enkripsi = []
    
    # Loop untuk setiap karakter di dalam plaintext
    for karakter in plaintext:
        # Jika karakter adalah huruf besar
        if karakter.isupper():
            # Menggeser karakter dalam rentang A-Z
            karakter_tergeser = chr((ord(karakter) - ord('A') + kunci) % 26 + ord('A'))
            hasil_enkripsi.append(karakter_tergeser)
        # Jika karakter adalah huruf kecil
        elif karakter.islower():
            # Menggeser karakter dalam rentang a-z
            karakter_tergeser = chr((ord(karakter) - ord('a') + kunci) % 26 + ord('a'))
            hasil_enkripsi.append(karakter_tergeser)
        else:
            # Jika bukan huruf (misalnya spasi), tidak diubah
            hasil_enkripsi.append(karakter)
    
    # Menggabungkan hasil enkripsi menjadi string dan mengembalikannya
    return ''.join(hasil_enkripsi)

# Plaintext dan kunci
plaintext = "WAWAN IENDY PRASTYA"
kunci = len(plaintext)  # Menggunakan panjang plaintext sebagai kunci

# Mengenkripsi pesan menggunakan sandi Caesar
ciphertext = caesar_enkripsi(plaintext, kunci)

print("Plaintext: ", plaintext)
print("Ciphertext: ", ciphertext)