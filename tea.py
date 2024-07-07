import streamlit as st

st.title("Questionário de Diagnóstico de Transtorno do Espectro Autista (TEA)")

st.write("Olá! Vamos começar com um questionário de 30 perguntas relacionadas ao TEA. Ao final, você poderá clicar no botão 'Diagnosticar' para obter o resultado.")

st.subheader("Informações Pessoais")

sex = st.radio("Sexo:", ("Masculino", "Feminino"), key="sex")
age = st.slider("Idade:", min_value=0, max_value=100, step=1, key="age")

st.subheader("Questionário")

questions = [
    "1. Dificuldade em se comunicar e interagir com outras pessoas?",
    "2. Dificuldade em entender e responder a expressões faciais e emoções dos outros?",
    "3. Dificuldade em iniciar ou manter conversas?",
    "4. Dificuldade em entender e seguir instruções simples?",
    "5. Dificuldade em entender e seguir regras sociais?",
    "6. Dificuldade em entender e responder a perguntas?",
    "7. Dificuldade em entender e responder a brincadeiras e piadas?",
    "8. Dificuldade em entender e responder a mudanças de rotina?",
    "9. Dificuldade em entender e responder a situações inesperadas?",
    "10. Dificuldade em entender e responder a situações sociais complexas?",
    "11. Dificuldade em manter contato visual durante as interações?",
    "12. Dificuldade em entender e responder a gestos e linguagem corporal?",
    "13. Dificuldade em entender e responder a mudanças de tom de voz?",
    "14. Dificuldade em entender e responder a metáforas e expressões idiomáticas?",
    "15. Dificuldade em entender e responder a piadas e sarcasmo?",
    "16. Dificuldade em entender e responder a instruções verbais?",
    "17. Dificuldade em entender e responder a perguntas abertas?",
    "18. Dificuldade em entender e responder a pedidos de clarificação?",
    "19. Dificuldade em entender e responder a mudanças de assunto?",
    "20. Dificuldade em entender e responder a interrupções durante uma conversa?",
    "21. Dificuldade em entender e responder a pedidos de ajuda?",
    "22. Dificuldade em entender e responder a elogios e críticas?",
    "23. Dificuldade em entender e responder a pedidos de opinião?",
    "24. Dificuldade em entender e responder a pedidos de feedback?",
    "25. Dificuldade em entender e responder a pedidos de explicação?",
    "26. Dificuldade em entender e responder a pedidos de confirmação?",
    "27. Dificuldade em entender e responder a pedidos de desculpas?",
    "28. Dificuldade em entender e responder a pedidos de agradecimento?",
    "29. Dificuldade em entender e responder a pedidos de desculpas?",
    "30. Dificuldade em entender e responder a pedidos de ajuda?",
]

answers = []
for i, question in enumerate(questions):
    answer = st.radio(question, ("Não", "Pouco", "Muito"), key=f"question_{i}")
    answers.append(answer)

if st.button("Diagnosticar"):
    total_score = sum([2 if answer == "Muito" else 1 if answer == "Pouco" else 0 for answer in answers])
    
    if total_score >= 60:
        st.write("Resultado: Provável diagnóstico de TEA de nível 3.")
        st.write("Nível 3: Requer muito apoio. Dificuldades graves de comunicação social que causam prejuízos graves no funcionamento. Comportamentos restritos e repetitivos causam sofrimento extremo.")
    elif total_score >= 40:
        st.write("Resultado: Provável diagnóstico de TEA de nível 2.")
        st.write("Nível 2: Requer apoio substancial. Dificuldades notáveis de comunicação social. Comportamentos restritos e repetitivos aparecem com frequência e são evidentes para observadores casuais.")
    elif total_score >= 20:
        st.write("Resultado: Provável diagnóstico de TEA de nível 1.")
        st.write("Nível 1: Requer apoio. Dificuldades de comunicação social sem ajuda in situ. Comportamentos restritos e repetitivos causam interferência significativa no funcionamento em um ou mais contextos.")
    else:
        st.write("Resultado: Baixa probabilidade de TEA.")
        
    st.write(f"Sua pontuação total é: {total_score}")
