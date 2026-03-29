# SimulaRede — Simulador de Camada Física e Enlace

[![Status](https://img.shields.io/badge/status-em%20desenvolvimento-yellow)](.)
[![Python](https://img.shields.io/badge/Python-3.11%2B-blue?logo=python)](.)
[![C++](https://img.shields.io/badge/C%2B%2B-17-orange?logo=cplusplus)](.)
[![UnB](https://img.shields.io/badge/UnB-Teleinform%C3%A1tica%20e%20Redes%201-darkgreen)](.)
[![License](https://img.shields.io/badge/licen%C3%A7a-Acad%C3%AAmica-lightgrey)](.)

> Simulador das camadas Física e de Enlace do modelo OSI, implementando protocolos de modulação banda-base, modulação por portadora, enquadramento de dados, detecção e correção de erros com interface gráfica GTK.

**Disciplina:** Teleinformática e Redes 1 — CIC/UnB  
**Professor:**  
**Aluno:** Felipe Avelar

---

## Índice

- [Visão Geral](#-visão-geral)
- [Arquitetura](#-arquitetura)
- [Requisitos do Trabalho](#-requisitos-do-trabalho)
- [Planejamento e Checklist](#-planejamento-e-checklist)
- [Extras e Melhorias](#-extras-e-melhorias)
- [Estrutura do Projeto](#-estrutura-do-projeto)
- [Como Executar](#-como-executar)
- [Tecnologias](#-tecnologias)

---

## Visão Geral

O **SimulaRede** simula o caminho que uma mensagem percorre desde a digitação pelo usuário até a recepção, passando pelas camadas de Enlace e Física de uma rede de computadores. O sistema é dividido em dois lados — **Transmissor (TX)** e **Receptor (RX)** — que rodam como threads paralelas e se comunicam via socket interno, com uma interface gráfica unificada em GTK.

```
[Usuário digita texto]
        ↓
┌───────────────────────────────────┐
│         CAMADA DE ENLACE (TX)     │
│  Bits → Detecção/Correção → Quadro│
└────────────────┬──────────────────┘
                 ↓
┌───────────────────────────────────┐
│         CAMADA FÍSICA (TX)        │
│  Quadro → Modulação → Sinal + Ruído│
└────────────────┬──────────────────┘
                 ↓
          [Canal com Ruído Gaussiano n(x,σ)]
                 ↓
┌───────────────────────────────────┐
│         CAMADA FÍSICA (RX)        │
│  Sinal → Demodulação → Bits       │
└────────────────┬──────────────────┘
                 ↓
┌───────────────────────────────────┐
│         CAMADA DE ENLACE (RX)     │
│  Quadro → Verificação → Texto     │
└────────────────┬──────────────────┘
                 ↓
[Usuário vê texto recuperado + gráficos]
```

---

## Arquitetura

O projeto segue uma arquitetura em camadas com threads separadas para TX e RX:

```
projeto-tr1/
├── simulador.py          # Ponto de entrada — orquestra threads e GUI
├── transmissor.py        # Lógica do lado TX
├── receptor.py           # Lógica do lado RX
├── canal.py              # Meio de comunicação + ruído gaussiano
├── camada_fisica.py      # Todas as modulações digitais e por portadora
├── camada_enlace.py      # Enquadramento, detecção e correção de erros
└── interface_gui.py      # Interface gráfica GTK com gráficos
```

---

## Requisitos do Trabalho

### Camada Física

#### Modulação Digital (Banda-Base)
- [ ] **NRZ-Polar** — bit 1 = +V, bit 0 = -V
- [ ] **Manchester** — transição no meio do bit (1 = sobe, 0 = desce)
- [ ] **Bipolar** — bit 0 = 0V, bit 1 alterna entre +V e -V

#### Modulação por Portadora
- [ ] **ASK** — Amplitude Shift Keying
- [ ] **FSK** — Frequency Shift Keying
- [ ] **QPSK** — Phase Shift Keying com 4 fases (2 bits/símbolo)
- [ ] **16-QAM** — Quadrature Amplitude Modulation (4 bits/símbolo)

### Camada de Enlace

#### Enquadramento
- [ ] **Contagem de caracteres**
- [ ] **FLAG com inserção de bytes/caracteres**
- [ ] **FLAG com inserção de bits**

#### Detecção de Erros
- [ ] **Bit de paridade par**
- [ ] **Checksum** (conforme apresentado em aula)
- [ ] **CRC-32** (polinômio IEEE 802) — sem uso de bibliotecas externas

#### Correção de Erros
- [ ] **Hamming** — detecção e correção de erro de 1 bit

### 🖥️ Interface e Infraestrutura
- [ ] **GUI GTK** (não terminal) com entrada de texto e parâmetros
- [ ] **Gráficos dos sinais** — TX e RX lado a lado
- [ ] **Thread TX e Thread RX** rodando em paralelo
- [ ] **Canal com ruído gaussiano** n(x, σ) em V/W
- [ ] **Socket interno** (socketpair) ligando TX e RX
- [ ] **Sinais implementados em V/W** (valores elétricos reais)

### Relatório (mínimo 3 páginas)
- [ ] Capa com nome do simulador e membros
- [ ] Introdução com visão geral do simulador
- [ ] Implementação com diagramas e decisões de projeto
- [ ] Seção de membros com atividades desenvolvidas
- [ ] Conclusão com dificuldades encontradas

### Arquivos de Código Exigidos
- [ ] `CamadaFisica` — implementação das funções de camada física
- [ ] `CamadaEnlace` — implementação das funções de camada de enlace
- [ ] `InterfaceGUI` — entrada de dados e resultados gráficos
- [ ] `Simulador` — rotina principal chamadora das demais

---

## Planejamento e Checklist

### Setup e Estrutura
- [ ] Criar repositório e estrutura de pastas
- [ ] Escrever README inicial
- [ ] Configurar ambiente Python (venv, dependências)
- [ ] Criar esqueleto dos arquivos com funções vazias
- [ ] Configurar GTK no ambiente de desenvolvimento

### Camada Física: Modulação Digital
- [ ] Implementar conversão texto → bits
- [ ] Implementar NRZ-Polar
- [ ] Implementar Manchester
- [ ] Implementar Bipolar
- [ ] Implementar decodificadores correspondentes
- [ ] Validar com exemplos dos slides

### Camada Física: Modulação por Portadora
- [ ] Implementar gerador de onda portadora senoidal
- [ ] Implementar ASK (+ demodulação)
- [ ] Implementar FSK (+ demodulação)
- [ ] Implementar QPSK com constelação de 4 pontos (+ demodulação)
- [ ] Implementar 16-QAM com constelação de 16 pontos (+ demodulação)

### Canal de Comunicação
- [ ] Implementar socketpair TX ↔ RX
- [ ] Implementar gerador de ruído gaussiano n(x, σ)
- [ ] Aplicar ruído sobre o sinal em V/W
- [ ] Testar comunicação TX → RX isolada

### Camada de Enlace: Enquadramento
- [ ] Implementar contagem de caracteres
- [ ] Implementar FLAG com inserção de bytes
- [ ] Implementar FLAG com inserção de bits
- [ ] Implementar desenquadradores correspondentes

### Camada de Enlace: Detecção de Erros
- [ ] Implementar bit de paridade par
- [ ] Implementar checksum
- [ ] Implementar CRC-32 (IEEE 802) do zero, sem zlib
- [ ] Validar detecção com erros injetados manualmente

### Camada de Enlace: Correção de Erros
- [ ] Implementar codificador Hamming
- [ ] Implementar decodificador/corretor Hamming
- [ ] Validar correção de 1 bit

### Interface Gráfica GTK
- [ ] Montar janela principal com campos de configuração
- [ ] Adicionar campo de entrada de texto
- [ ] Adicionar seletores de modulação, enquadramento, detecção/correção
- [ ] Adicionar controles de ruído (média x e desvio σ)
- [ ] Plotar sinal TX (antes do ruído)
- [ ] Plotar sinal RX (após ruído)
- [ ] Exibir bits em cada etapa do pipeline
- [ ] Exibir texto recuperado no receptor

### Integração e Testes
- [ ] Integrar todas as camadas no simulador.py
- [ ] Testar pipeline completo TX → RX
- [ ] Testar diferentes combinações de modulação + enquadramento + detecção
- [ ] Testar com ruído alto e verificar detecção/correção de erros
- [ ] Verificar legibilidade, comentários e modularização do código

### Relatório e Entrega
- [ ] Escrever introdução e visão geral
- [ ] Escrever seção de implementação com diagramas
- [ ] Escrever conclusão
- [ ] Empacotar código + relatório em .zip
- [ ] Submeter no Moodle

---

## Extras e Melhorias

> Funcionalidades além do exigido para elevar o nível do projeto:

### Visualização
- [ ] **Diagrama de constelação** em tempo real para QPSK e 16-QAM
- [ ] **BER (Bit Error Rate)** calculado e exibido graficamente em função do ruído
- [ ] **Animação do sinal** percorrendo o pipeline etapa por etapa
- [ ] **Comparação lado a lado** de múltiplas modulações para o mesmo sinal

### Funcionalidades
- [ ] **Modo de teste automático** — injeta erros e verifica se a detecção/correção funciona
- [ ] **Exportar sinal** como CSV ou imagem PNG
- [ ] **Histórico de transmissões** na sessão com replay
- [ ] **Modo benchmark** — mede desempenho de cada modulação com diferentes níveis de ruído

### Engenharia
- [ ] **Refatorar módulos críticos em C++** (ex: CRC-32, Hamming) com bindings Python via `ctypes`
- [ ] **Testes unitários** com `pytest` para cada protocolo individualmente
- [ ] **Logging estruturado** de cada etapa do pipeline para debug

---

## Estrutura do Projeto

```
projeto-tr1/
│
├── simulador.py          # Ponto de entrada principal
├── transmissor.py        # Thread TX — pipeline completo de envio
├── receptor.py           # Thread RX — pipeline completo de recepção
├── canal.py              # socketpair + ruído gaussiano
│
├── camada_fisica.py      # Modulações digitais e por portadora
├── camada_enlace.py      # Enquadramento, CRC, Hamming, Paridade
│
├── interface_gui.py      # GUI GTK — janela, gráficos, controles
│
├── tests/
│   ├── test_camada_fisica.py
│   └── test_camada_enlace.py
│
├── docs/
│   └── relatorio.pdf
│
├── requirements.txt
└── README.md
```

---

## Como Executar

### Pré-requisitos

```bash
sudo apt install python3-gi python3-gi-cairo gir1.2-gtk-3.0
pip install -r requirements.txt
```

### Executar

```bash
python simulador.py
```

---

## 🛠️ Tecnologias

| Tecnologia | Uso |
|---|---|
| Python 3.11+ | Linguagem principal |
| GTK 3 (PyGObject) | Interface gráfica |
| Matplotlib | Plotagem dos sinais |
| NumPy | Geração de sinais e ruído gaussiano |
| C++ 17 *(futuro)* | Refatoração de módulos críticos |
| ctypes *(futuro)* | Bindings Python ↔ C++ |
| pytest | Testes unitários |
