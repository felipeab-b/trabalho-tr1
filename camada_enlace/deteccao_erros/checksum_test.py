# checksum_test.py
from camada_enlace.deteccao_erros.checksum import add_checksum, verify_checksum
from utils import text_to_bits

texto = "Teste"
bits = text_to_bits(texto)
bits_com_checksum = add_checksum(bits)

print(f"Bits:            {bits}")
print(f"Com checksum:    {bits_com_checksum}")
print(f"Checksum OK:     {verify_checksum(bits_com_checksum)}")
