import streamlit as st

st.title("Questionário de Diagnóstico de Transtorno do Espectro Autista (TEA)")

st.write("Olá! Vamos começar com um questionário de 30 perguntas relacionadas ao TEA. Ao final, você poderá clicar no botão 'Diagnosticar' para obter o resultado.")

st.subheader("Informações Pessoais")

sex = st.radio("Sexo:", ("Masculino", "Feminino"), key="sex")
age = st.slider("Idade:", min_value=1, max_value=60, step=1, key="age")

st.subheader("Questionário")

questions = [
    "1. Evita contato visual com outras pessoas?",
    "2. Dificuldade em entender as emoções e expressões faciais dos outros?",
    "3. Dificuldade em iniciar ou manter conversas?",
    "4. Interesses restritos ou obsessivos por determinados temas?",
    "5. Apresenta comportamentos repetitivos ou ritualizados?",
    "6. Sensibilidade a determinados sons, texturas ou luzes?",
    "7. Dificuldade em lidar com mudanças na rotina?",
    "8. Dificuldade em entender piadas, metáforas ou sarcasmo?",
    "9. Dificuldade em compreender regras sociais e se adaptar a diferentes contextos?",
    "10. Dificuldade em se colocar no lugar dos outros?",
    "11. Dificuldade em expressar suas próprias emoções?",
    "12. Dificuldade em entender instruções complexas?",
    "13. Dificuldade em se organizar e planejar tarefas?",
    "14. Dificuldade em lidar com situações inesperadas?",
    "15. Dificuldade em manter a atenção por longos períodos?",
    "16. Dificuldade em se adaptar a ambientes barulhentos ou com muitos estímulos?",
    "17. Dificuldade em entender expressões faciais e linguagem corporal?",
    "18. Dificuldade em fazer amizades e manter relacionamentos?",
    "19. Dificuldade em entender e seguir regras sociais?",
    "20. Dificuldade em lidar com mudanças de rotina ou transições?",
    "21. Dificuldade em entender instruções verbais complexas?",
    "22. Dificuldade em se concentrar em tarefas que não lhe interessam?",
    "23. Dificuldade em entender piadas, metáforas ou sarcasmo?",
    "24. Dificuldade em se adaptar a ambientes com muitas pessoas?",
    "25. Dificuldade em entender e responder a perguntas?",
    "26. Dificuldade em lidar com situações sociais desconhecidas?",
    "27. Dificuldade em entender e seguir regras sociais implícitas?",
    "28. Dificuldade em lidar com mudanças inesperadas na rotina?",
    "29. Dificuldade em entender e interpretar as emoções dos outros?",
    "30. Dificuldade em se comunicar de forma efetiva?",
]

answers = []
for i, question in enumerate(questions):
    answer = st.radio(question, ("Não", "Pouco", "Muito"), key=f"question_{i}")
    answers.append(answer)

if st.button("Diagnosticar"):
    total_score = sum([2 if answer == "Muito" else 1 if answer == "Pouco" else 0 for answer in answers])
    
    with st.sidebar:
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
