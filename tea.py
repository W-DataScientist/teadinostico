import streamlit as st

st.title("Questionário de Diagnóstico de Transtorno do Espectro Autista (TEA)")

st.write("Olá! Vamos começar com um questionário de 30 perguntas relacionadas ao TEA. Ao final, você poderá ver o resultado do seu diagnóstico.")

st.subheader("Informações Pessoais")

sex = st.radio("Sexo:", ("Masculino", "Feminino"), key="sex")
age = st.slider("Idade:", min_value=1, max_value=60, step=1, key="age")

st.subheader("Questionário")

pontuacao = []

for i in range(1, 31):
    st.subheader(f"{i}. Dificuldade em {questions[i-1]}?")
    resposta = st.radio("", ("Não", "Pouco", "Muito"), key=f"question_{i}")
    if resposta == "Não":
        pontuacao.append(0)
    elif resposta == "Pouco":
        pontuacao.append(1)
    else:
        pontuacao.append(2)
    st.write("---")

total_score = sum(pontuacao)

st.subheader("Resultado do Diagnóstico")

if total_score >= 60:
    st.write("Diagnóstico: Provável TEA de nível 3.")
    st.write("Considerações:")
    st.write("Nível 3: Requer muito apoio. Dificuldades graves de comunicação social que causam prejuízos graves no funcionamento. Comportamentos restritos e repetitivos causam sofrimento extremo.")
elif total_score >= 40:
    st.write("Diagnóstico: Provável TEA de nível 2.")
    st.write("Considerações:")
    st.write("Nível 2: Requer apoio substancial. Dificuldades notáveis de comunicação social. Comportamentos restritos e repetitivos aparecem com frequência e são evidentes para observadores casuais.")
elif total_score >= 20:
    st.write("Diagnóstico: Provável TEA de nível 1.")
    st.write("Considerações:")
    st.write("Nível 1: Requer apoio. Dificuldades de comunicação social sem ajuda in situ. Comportamentos restritos e repetitivos causam interferência significativa no funcionamento em um ou mais contextos.")
else:
    st.write("Diagnóstico: Baixa probabilidade de TEA.")
    st.write("Considerações:")
    st.write("Sua pontuação indica uma baixa probabilidade de Transtorno do Espectro Autista.")

st.write(f"Sua pontuação total é: {total_score}")
