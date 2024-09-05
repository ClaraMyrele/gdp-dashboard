# Explorador de Voos - Estilo Kayak

Esta é uma aplicação interativa de busca de voos, inspirada no estilo do **Kayak Explore**, que permite aos usuários filtrarem voos com base na cidade de partida, chegada, data da viagem e companhia aérea. Utilizando **Streamlit**, a aplicação exibe os resultados em uma interface amigável e interativa, com previsão de preços baseada em um modelo de regressão.

## Funcionalidades

- **Filtros de busca**: Escolha a cidade de partida, destino, data e companhia aérea.
- **Previsão de preços**: Utiliza um modelo de machine learning (Gradient Boosting Regressor) para prever o preço dos voos.
- **Interface interativa**: Fácil de usar, com visualização dinâmica dos resultados.

## Pré-requisitos

Antes de rodar a aplicação, certifique-se de ter o **Python** instalado. Além disso, será necessário instalar as seguintes bibliotecas:

```bash
pip install streamlit numpy pandas scikit-learn
