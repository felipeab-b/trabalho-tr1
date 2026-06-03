def text_to_bits(text):
    bits = ""
    for byte in bytearray(text, 'utf-8'):
        bits += format(byte, '08b')
    return bits

def bits_to_text(bits):
    text = ""
    for i in range(0, len(bits), 8):
        byte = bits[i:i+8]
        text += chr(int(byte, 2))
    return text
