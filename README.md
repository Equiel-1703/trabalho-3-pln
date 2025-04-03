# Trabalho 3 de PLN

## Descrição

Este projeto é parte da disciplina de Processamento de Linguagem Natural (PLN) e tem como objetivo desenvolver um modelo NER com base no `pt_core_news_sm` que identifica entidades relacionadas à computação, como linguagens de programação, frameworks, bibliotecas e algoritmos. O modelo foi treinado com artigos da SBC (Sociedade Brasileira de Computação).

Uma aplicação com interface gráfica foi desenvolvida para demonstrar o funcionamento do modelo. A interface foi criada utilizando a biblioteca PyQt6, e usa nosso modelo treinado com 100 épocas. O app permite carregar um PDF e exibir as entidades reconhecidas no texto. A extração de texto do PDF é feita com a biblioteca PyMuPDF, que converte o conteúdo do PDF em texto simples. O texto é pre-processado para remover caracteres especiais e normalizar o texto, facilitando a identificação das entidades. Depois, o modelo NER é aplicado ao texto pré-processado, e as entidades reconhecidas são destacadas na interface gráfica.

## Conjunto de Dados

Este projeto é uma prova de conceito, portanto o conjunto de dados usado foi muito pequeno. Ele se encontra no arquivo `trainer/TrainingData/training_data.py` como um array de tuplas contendo as tags que criamos. Os textos no array foram extraídos de artigos públicos da SBC que estão disponíveis [aqui](https://drive.google.com/drive/folders/1ZltMA-gIdFodY4-lNXMJUITI7YP8JKGe?usp=sharing).

## Instruções de Execução

1. Clone o repositório:

    ```bash

    git clone https://github.com/Equiel-1703/trabalho-3-pln.git
    
    ```

2. Navegue até o diretório do projeto:

    ```bash

    cd trabalho-3-pln

    ```

3. Instale as dependências:

    ```bash

    pip install -U pip setuptools wheel
    pip install -U spacy
    python -m spacy download pt_core_news_sm
    pip install PyQt6

    ```

4. Para executar a aplicação com interface gráfica, execute o seguinte comando:

    ```bash

    python 'PDF Analyzer.py'

    ```

5. Para treinar o modelo com diferentes épocas, execute os seguintes comando:

    ```bash

    cd trainer
    python Trainer.py <número de épocas>

    ```

6. Para testar o modelo com um conjunto de textos teste, execute o seguinte comando:

    ```bash

    cd trainer
    python Tester.py

    ```

## Licença

Este projeto está licenciado sob a [Licença MIT](https://opensource.org/licenses/MIT).
