from camada_fisica.banda_base.nrz_polar import codificar_nrz, decodificar_nrz
from camada_fisica.banda_base.manchester import codificar_manchester, decodificar_manchester
from camada_fisica.banda_base.bipolar import codificar_bipolar, decodificar_bipolar
from camada_fisica.portadora.ask import codificar_ask, decodificar_ask
from camada_fisica.portadora.fsk import codificar_fsk, decodificar_fsk
from camada_fisica.portadora.qpsk import codificar_qpsk, decodificar_qpsk
from camada_fisica.portadora.qam16 import codificar_qam16, decodificar_qam16

from camada_enlace.enquadramento.contagem import enquadrar_contagem, desenquadrar
from camada_enlace.enquadramento.flag_bytes import enquadrar_flag_bytes, desenquadrar_flag_bytes
from camada_enlace.enquadramento.flag_bits import enquadrar_flag_bits, desenquadrar_flag_bits

from camada_enlace.deteccao_erros.paridade import add_paridade, verify_paridade
from camada_enlace.deteccao_erros.checksum import add_checksum, verify_checksum
from camada_enlace.deteccao_erros.crc import add_crc, verify_crc

from camada_enlace.correcao_erros.hamming import hamming74_codificar, hamming74_decodificar


def _identidade_codificar(sinal_base):
    return sinal_base


def _identidade_decodificar(sinal):
    return sinal


def _sem_enquadramento(bits):
    return bits


def _sem_desenquadramento(bits):
    return bits


def _sem_edc_adicionar(bits):
    return bits


def _sem_edc_verificar(bits):
    return bits  


MODULACOES_BANDA_BASE = {
    'nrz': (codificar_nrz, decodificar_nrz),
    'manchester': (codificar_manchester, decodificar_manchester),
    'bipolar': (codificar_bipolar, decodificar_bipolar),
}

MODULACOES_PORTADORA = {
    'nenhum': (_identidade_codificar, _identidade_decodificar),
    'ask': (codificar_ask, decodificar_ask),
    'fsk': (codificar_fsk, decodificar_fsk),
    'qpsk': (codificar_qpsk, decodificar_qpsk),
    'qam16': (codificar_qam16, decodificar_qam16),
}

ENQUADRAMENTOS = {
    'nenhum': (_sem_enquadramento, _sem_desenquadramento),
    'contagem': (enquadrar_contagem, desenquadrar),
    'flag_bytes': (enquadrar_flag_bytes, desenquadrar_flag_bytes),
    'flag_bits': (enquadrar_flag_bits, desenquadrar_flag_bits),
}

DETECCAO_CORRECAO = {
    'nenhum': (_sem_edc_adicionar, _sem_edc_verificar, 'correcao'),
    'paridade': (add_paridade, verify_paridade, 'verificacao'),
    'checksum': (add_checksum, verify_checksum, 'verificacao'),
    'crc': (add_crc, verify_crc, 'verificacao'),
    'hamming': (hamming74_codificar, hamming74_decodificar, 'correcao'),
}