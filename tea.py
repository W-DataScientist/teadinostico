import streamlit as st

st.title("Questionário de Diagnóstico de Transtorno do Espectro Autista (TEA)")

st.write("Olá! Vamos começar com um questionário de 30 perguntas relacionadas ao TEA. Ao final, você poderá clicar no botão 'Diagnosticar' para obter o resultado.")

st.subheader("Informações Pessoais")

sex = st.radio("Sexo:", ("Masculino", "Feminino"))
age = st.number_input("Idade:", min_value=0, step=1)

st.subheader("Questionário")

questions = [
    "Você tem dificuldade em se comunicar e interagir com outras pessoas?",
    "Você tem dificuldade em entender e responder a expressões faciais e emoções dos outros?",
    "Você tem dificuldade em iniciar ou manter conversas?",
    "Você tem dificuldade em entender e seguir instruções simples?",
    "Você tem dificuldade em entender e seguir regras sociais?",
    "Você tem dificuldade em entender e responder a perguntas?",
    "Você tem dificuldade em entender e responder a brincadeiras e piadas?",
    "Você tem dificuldade em entender e responder a mudanças de rotina?",
    "Você tem dificuldade em entender e responder a situações inesperadas?",
    "Você tem dificuldade em entender e responder a situações sociais complexas?",
    "Você tem dificuldade em manter contato visual durante as interações?",
    "Você tem dificuldade em entender e responder a gestos e linguagem corporal?",
    "Você tem dificuldade em entender e responder a mudanças de tom de voz?",
    "Você tem dificuldade em entender e responder a metáforas e expressões idiomáticas?",
    "Você tem dificuldade em entender e responder a piadas e sarcasmo?",
    "Você tem dificuldade em entender e responder a instruções verbais?",
    "Você tem dificuldade em entender e responder a perguntas abertas?",
    "Você tem dificuldade em entender e responder a pedidos de clarificação?",
    "Você tem dificuldade em entender e responder a mudanças de assunto?",
    "Você tem dificuldade em entender e responder a interrupções durante uma conversa?",
    "Você tem dificuldade em entender e responder a pedidos de ajuda?",
    "Você tem dificuldade em entender e responder a elogios e críticas?",
    "Você tem dificuldade em entender e responder a pedidos de opinião?",
    "Você tem dificuldade em entender e responder a pedidos de feedback?",
    "Você tem dificuldade em entender e responder a pedidos de explicação?",
    "Você tem dificuldade em entender e responder a pedidos de confirmação?",
    "Você tem dificuldade em entender e responder a pedidos de desculpas?",
    "Você tem dificuldade em entender e responder a pedidos de agradecimento?",
    "Você tem dificuldade em entender e responder a pedidos de desculpas?",
    "Você tem dificuldade em entender e responder a pedidos de ajuda?",
]

answers = []
for question in questions:
    answer = st.radio(question, ("Não", "Pouco", "Muito"))
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
