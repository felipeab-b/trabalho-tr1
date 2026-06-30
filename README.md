# SimulaRede — Simulador de Camada Física e Enlace

[![Status](https://img.shields.io/badge/status-concluído-brightgreen)](.)
[![Python](https://img.shields.io/badge/Python-3.11%2B-blue?logo=python)](.)
[![UnB](https://img.shields.io/badge/UnB-Teleinform%C3%A1tica%20e%20Redes%201-darkgreen)](.)
[![License](https://img.shields.io/badge/licen%C3%A7a-Acad%C3%AAmica-lightgrey)](.)

> Simulador das camadas Física e de Enlace do modelo OSI, implementando protocolos de modulação banda-base, modulação por portadora, enquadramento de dados, fragmentação de quadros, detecção e correção de erros, ruído gaussiano no canal e interface gráfica GTK.

**Disciplina:** Teleinformática e Redes 1 — CIC/UnB
**Professor:** Marcelo Antonio Marotta
**Aluno:** Felipe Avelar Borborema Ferreira — 241025210

---

## Índice

- [Visão Geral](#visão-geral)
- [Arquitetura](#arquitetura)
- [Funcionalidades Implementadas](#funcionalidades-implementadas)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Como Executar](#como-executar)
- [Tecnologias](#tecnologias)

---

## Visão Geral

O **SimulaRede** simula o caminho que uma mensagem percorre desde a digitação pelo usuário até a recepção, passando pelas camadas de Enlace e Física de uma rede de computadores. O sistema é dividido em três partes — **Transmissor (TX)**, **Canal** e **Receptor (RX)** — que rodam como threads independentes, comunicando-se por sockets TCP reais (`AF_INET`/`SOCK_STREAM`) sobre o endereço de loopback, reproduzindo de forma simplificada uma comunicação cliente-servidor real.

```
[Usuário digita texto]
        ↓
┌───────────────────────────────────┐
│         CAMADA DE ENLACE (TX)     │
│  Bits → Detecção/Correção         │
│       → Fragmentação → Quadros    │
└────────────────┬──────────────────┘
                 ↓
┌───────────────────────────────────┐
│         CAMADA FÍSICA (TX)        │
│  Quadros → Banda-Base → Portadora │
└────────────────┬──────────────────┘
                 ↓
        [TCP: TX → Canal (porta 9001)]
                 ↓
          [Canal com Ruído Gaussiano n(x,σ)]
                 ↓
        [TCP: Canal → RX (porta 9002)]
                 ↓
┌───────────────────────────────────┐
│         CAMADA FÍSICA (RX)        │
│  Sinal → Demod. Portadora         │
│       → Decod. Banda-Base         │
└────────────────┬──────────────────┘
                 ↓
┌───────────────────────────────────┐
│         CAMADA DE ENLACE (RX)     │
│  Quadros → Remontagem             │
│       → Verificação/Correção      │
└────────────────┬──────────────────┘
                 ↓
[Usuário vê texto recuperado + gráficos]
```

---

## Arquitetura

O TX, o Canal e o RX executam como **threads independentes** dentro do mesmo processo (junto com a thread principal da interface gráfica), comunicando-se via **sockets TCP reais** sobre `localhost`, usando um protocolo simples de mensagens com cabeçalho de tamanho (*length-prefix*) para evitar problemas de sincronização entre as conexões.

```
GUI (thread principal)
  └── ao enviar:
       Thread RX     → servidor TCP na porta 9002 (aguarda o Canal)
       Thread Canal  → servidor TCP na porta 9001 (aguarda o TX)
                      → cliente TCP que envia para o RX na porta 9002
       Thread TX     → cliente TCP que conecta na porta 9001
```

A ordem de inicialização das threads (RX → Canal → TX) garante que cada servidor já esteja em modo de escuta antes do próximo lado tentar se conectar.

---

## Funcionalidades Implementadas

### Camada Física

**Modulação Digital (Banda-Base)** — sempre aplicada, é a base de qualquer transmissão
- **NRZ-Polar** — bit 1 = +V, bit 0 = −V
- **Manchester** — transição obrigatória no meio do bit
- **Bipolar** — bit 0 = 0V, bit 1 alterna entre +V e −V

**Modulação por Portadora** — opcional, aplicada sobre o sinal de banda-base já gerado
- **ASK** — Amplitude Shift Keying
- **FSK** — Frequency Shift Keying (com fase contínua entre símbolos)
- **QPSK** — Phase Shift Keying com 4 fases (2 bits/símbolo)
- **16-QAM** — Quadrature Amplitude Modulation com componentes I/Q (4 bits/símbolo)

**Canal de Comunicação**
- Ruído gaussiano configurável `n(x, σ)` aplicado ao sinal em V/W
- Comunicação via socket TCP real entre TX, Canal e RX

### Camada de Enlace

**Enquadramento** — com opção de fragmentação automática por tamanho máximo de quadro
- **Contagem de caracteres** (cabeçalho com a quantidade exata de bits do payload)
- **FLAG com inserção de bytes** (com byte de escape ESC)
- **FLAG com inserção de bits** (bit stuffing)
- **Nenhum** — sem enquadramento

**Detecção de Erros**
- **Bit de paridade** par
- **Checksum** em complemento de um
- **CRC-32** (polinômio IEEE 802), implementado do zero, sem bibliotecas externas
- **Nenhum** — sem verificação

**Correção de Erros**
- **Hamming (7,4)** — corrige automaticamente um erro de 1 bit por bloco

### Interface e Infraestrutura
- GUI em GTK 3 (não-terminal), com seletores para todos os protocolos acima
- Controles de ruído (média *x* e desvio padrão *σ*) e tamanho máximo de quadro
- Painéis lado a lado mostrando cada etapa do pipeline no TX e no RX
- Gráficos do sinal de banda-base e do sinal modulado por portadora
- Diagrama de constelação para QPSK e 16-QAM
- Logs com timestamp de cada etapa da comunicação via socket, para depuração e validação do funcionamento das threads

---

## Estrutura do Projeto

```
trabalho-tr1/
├── interface.py             # GUI GTK — janela, gráficos, controles
├── simulador.py             # Orquestra as threads de TX, Canal e RX
├── transmissor.py           # Thread TX — pipeline completo de envio
├── canal.py                 # Servidor/cliente TCP do canal + ruído gaussiano
├── receptor.py              # Thread RX — pipeline completo de recepção
├── protocolo_tcp.py         # Protocolo de mensagens TCP com length-prefix
├── registro.py              # Mapeamento entre nomes de protocolos e suas funções
├── utils.py                 # Conversão entre texto e bits
├── style.css                # Estilo visual da interface
│
├── camada_fisica/
│   ├── banda_base/
│   │   ├── nrz_polar.py
│   │   ├── manchester.py
│   │   └── bipolar.py
│   └── portadora/
│       ├── ask.py
│       ├── fsk.py
│       ├── qpsk.py
│       └── qam16.py
│
├── camada_enlace/
│   ├── enquadramento/
│   │   ├── contagem.py
│   │   ├── flag_bytes.py
│   │   ├── flag_bits.py
│   │   └── fragmentacao.py   # fragmentação/remontagem em múltiplos quadros
│   ├── deteccao_erros/
│   │   ├── paridade.py
│   │   ├── checksum.py
│   │   └── crc.py
│   └── correcao_erros/
│       └── hamming.py
│
└── *_test.py                 # testes unitários de cada módulo
```

---

## Como Executar

### Pré-requisitos

```bash
sudo apt install python3-gi python3-gi-cairo gir1.2-gtk-3.0
pip install numpy matplotlib --break-system-packages
```

### Executar

```bash
python -m interface
```

Na interface, digite a mensagem, escolha a codificação de banda-base (obrigatória), a modulação por portadora (opcional), o tipo de enquadramento, o mecanismo de detecção/correção de erros, os parâmetros de ruído gaussiano e o tamanho máximo de quadro, e clique em **Enviar**.

---

## Tecnologias

| Tecnologia | Uso |
|---|---|
| Python 3.11+ | Linguagem principal |
| GTK 3 (PyGObject) | Interface gráfica |
| Matplotlib | Plotagem dos sinais e diagrama de constelação |
| NumPy | Geração de sinais, modulação e ruído gaussiano |
| socket (AF_INET) | Comunicação TCP real entre TX, Canal e RX |
| threading | Execução concorrente de TX, Canal, RX e GUI |