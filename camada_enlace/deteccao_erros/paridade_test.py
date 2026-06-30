from camada_enlace.deteccao_erros.paridade import add_paridade, verify_paridade
from utils import text_to_bits

texto = "Teste"
bits = text_to_bits(texto)
bits_com_paridade = add_paridade(bits)

print(f"Bits:          {bits}")
print(f"Com paridade:  {bits_com_paridade}")
print(f"Paridade OK:   {verify_paridade(bits_com_paridade)}")

print("")

texto2 = "Teste1"
bits2 = text_to_bits(texto2)
bits_com_paridade2 = add_paridade(bits2)

print(f"Bits:          {bits2}")
print(f"Com paridade:  {bits_com_paridade2}")
print(f"Paridade OK:   {verify_paridade(bits_com_paridade2)}")