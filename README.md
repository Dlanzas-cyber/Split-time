# 🕐 Split-Time App

Uma aplicação web construída com Python e Streamlit que divide um intervalo de tempo em períodos iguais, com opção de sobreposição. Ideal para produtividade, estudo ou turnos.

## ✨ Funcionalidades

- Divide qualquer intervalo horário em blocos iguais
- Permite cortes com ou sem minutos de sobreposição
- Interface simples, visual e adaptada a telemóveis
- Ícone personalizado para adicionar como atalho no ecrã inicial 📱

## 🚀 Como utilizar

1. Abre a aplicação em [https://split-time.streamlit.app](https://split-time.streamlit.app)
2. Define a hora de início e fim
3. Escolhe quantos cortes pretendes
4. (Opcional) Ativa a sobreposição e ajusta os minutos
5. Clica em “Calcular” e vê os períodos gerados!

## 📲 Adicionar como atalho no telemóvel

- Em **Android (Chrome):**  
  → Abre a app, toca nos três pontos no canto superior direito e escolhe “Adicionar ao ecrã principal”

- Em **iPhone (Safari):**  
  → Toca no ícone de partilha e escolhe “Adicionar ao ecrã principal”

O atalho usará o ícone personalizado como se fosse uma app nativa.

## 🛠 Requisitos (se usares localmente)

```bash
pip install -r requirements.txt
streamlit run app.py

