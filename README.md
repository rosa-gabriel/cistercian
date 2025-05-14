# Cistercian Numerals

Este é um aplicativo com interface gráfica (GUI) desenvolvido em Python com `tkinter`, que converte números arábicos (de 1 a 9999) para o sistema numérico **cisterciense**, uma forma histórica de representar números em uma única barra vertical.

O sistema também possui suporte à identificação automática de números a partir de imagens, usando uma simulação com a biblioteca **Pillow** para processar as imagens.

## Funcionalidades

* Conversão de números de 1 a 9999 para numerais cistercienses.
* Visualização gráfica do numeral gerado.
* Upload de imagem com um numeral manuscrito e identificação automatizada do número .
* Interface simples e intuitiva com `tkinter`.

## Pré-requisitos

Antes de executar o projeto, você precisa ter instalado em seu ambiente:

* Python 3.8 ou superior
* pip

## Instalação

1. Clone o repositório:

```bash
git clone https://github.com/rosa-gabriel/cistercian.git
cd cistercian
```

2. Instale as dependências:

```bash
pip install Pillow tkinter
```

> O projeto utiliza a biblioteca **Pillow** para carregar e processar imagens, possibilitando a leitura e exibição de arquivos `.png`, `.jpg`, `.jpeg` e `.bmp`.

## Como Executar

Para iniciar o programa, execute o seguinte comando no terminal:

```bash
python main.py
```

