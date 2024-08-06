<div align="center">
<img src="https://github.com/user-attachments/assets/3befeeeb-0b0f-4b20-b3a9-88cdd80daefb" width="200" height="200"/>
</div>
<h1>Projeto integrado - Deep Learning</h1>

A detecção de tendências no mercado de ações pode auxiliar na tomada de decisões financeiras, possibilitando a maximização de lucros e a minimização de riscos. Utilizando técnicas de Deep Learning, é possível automatizar e melhorar a precisão dessas previsões.

Este projeto é parte do curso de MBA em Data Science e Inteligência Artificial da FIAP, desenvolvido para a empresa fictícia QuantumFinance. O objetivo é criar modelos de Deep Learning para prever ações de compra ou venda baseadas nos últimos 15 dias de movimentação do mercado. As ações analisadas são VALE3, PETR4, BBAS3 e CSNA3.

## Metodologia

1. **Dados**:
   - Screenshots do gráfico de barras de determinada ação contemplando um periodo de 15 dias, os screenshots foram separados em duas pastas: uma pasta estava as capturas que indicavam compra e a outra pasta as que indicavam venda.

     <img src="https://github.com/user-attachments/assets/a5c173eb-9db1-4551-92eb-e8d33b93cac2"  width="50px" height="160px" />
   - Arquivo CSV onde cada linha contem o valor de fechamento da ação e o valor dos ultimos 15 dias

     ```python
     Date,Close,Smoothed_Close,Label,Past_1_Days_Close,Past_2_Days_Close,Past_3_Days_Close,Past_4_Days_Close,Past_5_Days_Close,Past_6_Days_Close,Past_7_Days_Close,Past_8_Days_Close,Past_9_Days_Close,Past_10_Days_Close,Past_11_Days_Close,Past_12_Days_Close,Past_13_Days_Close,Past_14_Days_Close,Past_15_Days_Close
     2019-03-26,36.38615798950195,37.91764846965505,-1,35.54909896850586,35.2972412109375,37.326934814453125,38.1269416809082,39.00105285644531,39.8529167175293,40.156639099121094,39.815879821777344,40.11958312988281,39.51216125488281,39.737266540527344,38.55548858642578,37.24814987182617,37.39586639404297,37.898128509521484
     ```
   - Período: Janeiro de 2000 a dezembro de 2023 para treino e teste.

3. **Pré-processamento dos Dados**:
   - Para a CNN o unico pré processamento foi o
     - Redimensionamento das imagens para o tamanho de 28x28
   - Para a LSTM foram
     - Removidas as colunas "Smoothed_Close", "Close", "Date";
     - Normalização com o MinMaxScaler
  
    **Observação**:
       - O dataset fornecido já estava estruturado para construir o modelo LSTM com um período de 15 dias. No entanto, não necessariamente esse intervalo é o mais informativo. Para investigar isso, desenvolvi um código que testava o modelo com diversos intervalos de dias, variando de 3 a 100. Ou seja, a entrada do nosso modelo variou desde o valor de fechamento até os valores dos últimos cem dias de uma determinada ação. No entanto, não houve uma mudança significativa no desempenho do modelo ao alterar o intervalo de dias fornecido.
4. **Modelagem**:
   - **CNN**:
     ```python
     model = Sequential()
     model.add(Conv2D(32, (5, 5), input_shape=(28, 28, 1), activation='relu'))
     model.add(MaxPooling2D(pool_size=(2, 2)))
     model.add(Conv2D(64, (5, 5), activation='relu'))
     model.add(MaxPooling2D(pool_size=(2, 2)))
     model.add(Dropout(0.2))
     model.add(Flatten())
     model.add(Dense(32, activation='relu'))
     model.add(Dense(16, activation='relu'))
     model.add(Dense(1, activation='sigmoid'))
     ```

   - **LSTM**:
     ```python
     model = Sequential()
     model.add(LSTM(neurons, input_shape=input_shape))
     model.add(Dense(1, activation='sigmoid'))
     model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
     ```

5. **Avaliação**:
   - Geração de métricas como acurácia, matriz de confusão, precision e recall.
   - Backtest - O arquivo ```generate_backtest_data.ipynb``` fica responsável por puxar os dados das 4 ações do ultimo periodo do treinamento até o dia atual e gerar um csv ja formatado para o modelo.

## Resultados
A métrica apresentada será a acurácia, caso deseje conferir as outras basta olhar o arquivo do modelo.
O backtest foi feito para os modelos LSTM somente.

- **CNN**:
  - BBAS3: 87.43%
  - CSNA3: 88.95%
  - PETR4: 86.37%
  - VALE3: 88.78%

- **LSTM**:
  - BBAS3: 76.75%
  - CSNA3: 87.43%
  - PETR4: 84.86%
  - VALE3: 79.70%
  - Para o Backtest, operando com 20 cotas de cada ação, o resultado foi positivo para todas, sendo eles:
   **BBAS3**: R$275.59 ; **CSNA3**: R$195.79 ; **PETR4**: R$378.20 ; **VALE3**: R$237.39

## Conclusão

As redes convolucionais tiveram um resultado consideravelmente melhor que as LSTM, futuras pesquisas poderiam explorar o uso de dados adicionais, como indicadores financeiros e notícias do mercado, bem como testar outras arquiteturas de redes neurais.

A precisão relativamente alta dos modelos **NÃO** sugere necessariamente que estes podem ser usadas para previsões de curto prazo no mercado de ações, este projeto foi feito com fins de aprendizado e **NÃO** deve ser utilizado para fins comerciais.

## Principais arquivos do Projeto

- `cnn.ipynb`: Notebook com a implementação e avaliação dos modelos CNN.
- `lstm.ipynb`: Notebook com a implementação e avaliação dos modelos LSTM.
- `generate_backtest_data.ipynb`: Notebook com a geração dos dados de backtest.

## Como Executar

1. Clone este repositório.
2. Instale as dependências necessárias (listadas no arquivo `requirements.txt`).
3. Execute os notebooks `cnn.ipynb` e `lstm.ipynb` para treinar e avaliar os modelos.

## Referências

- Documentação TensorFlow: [https://www.tensorflow.org/](https://www.tensorflow.org/)
- Dados de Preços Históricos e Gráficos: [link para os dados fornecidos]

