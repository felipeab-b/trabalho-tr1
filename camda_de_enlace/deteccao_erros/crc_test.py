from crc import add_crc, verify_crc
from utils import text_to_bits

texto = "Teste"
bits = text_to_bits(texto)
bits_com_crc = add_crc(bits)

print(f"Bits:         {bits}")
print(f"Com CRC:      {bits_com_crc}")
print(f"CRC OK:       {verify_crc(bits_com_crc)}")