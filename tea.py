import streamlit as st

st.title("Questionário de Diagnóstico de Transtorno do Espectro Autista (TEA)")

st.write("Olá! Vamos começar com um questionário de 30 perguntas relacionadas ao TEA. Ao final, você poderá clicar no botão 'Diagnosticar' para obter o resultado.")

st.subheader("Informações Pessoais")

sex = st.radio("Sexo:", ("Masculino", "Feminino"), key="sex")
age = st.number_input("Idade:", min_value=0, step=1, key="age")

st.subheader("Questionário")

questions = [
    "Você tem dificuldade em se comunicar e interagir com outras pessoas?",
    "Você tem dificuldade em entender e responder a expressões faciais e emoções dos outros?",
    "Você tem dificuldade em iniciar ou manter conversas?",
    # Adicione as 27 perguntas restantes aqui
]

answers = []
for i, question in enumerate(questions):
    answer = st.radio(question, ("Não", "Pouco", "Muito"), key=f"question_{i}")
    answers.append(answer)

if st.button("Diagnosticar"):
    total_score = sum([1 if answer == "Muito" else 0 for answer in answers])
    
    if total_score >= 20:
        st.write("Resultado: Provável diagnóstico de TEA.")
    elif total_score >= 10:
        st.write("Resultado: Possíveis sintomas de TEA.")
    else:
        st.write("Resultado: Baixa probabilidade de TEA.")
        
    st.write(f"Sua pontuação total é: {total_score}")
