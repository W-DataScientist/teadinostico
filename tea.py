import streamlit as st

st.title("Questionário de Diagnóstico de Transtorno do Espectro Autista (TEA)")

st.write("Olá! Vamos começar com um questionário de 30 perguntas relacionadas ao TEA. Ao final, você poderá clicar no botão 'Diagnosticar' para obter o resultado.")

st.subheader("Informações Pessoais")

sex = st.radio("Sexo:", ("Masculino", "Feminino"), key="sex")
age = st.slider("Idade:", min_value=1, max_value=60, step=1, key="age")

st.subheader("Questionário")

pontuacao = []

st.subheader("1. Evita contato visual com outras pessoas?")
st.write("Exemplo...")
resposta = st.radio("", ("Não", "Pouco", "Muito"), key="q1")
if resposta == "Não":
    pontuacao.append(0)
elif resposta == "Pouco":
    pontuacao.append(1)
else:
    pontuacao.append(2)
st.write("---")

st.subheader("2. Dificuldade em entender as emoções e expressões faciais dos outros?")
st.write("Exemplo...")
resposta = st.radio("", ("Não", "Pouco", "Muito"), key="q2")
if resposta == "Não":
    pontuacao.append(0)
elif resposta == "Pouco":
    pontuacao.append(1)
else:
    pontuacao.append(2)
st.write("---")

st.subheader("3. Dificuldade em iniciar ou manter conversas?")
st.write("Exemplo...")
resposta = st.radio("", ("Não", "Pouco", "Muito"), key="q3")
if resposta == "Não":
    pontuacao.append(0)
elif resposta == "Pouco":
    pontuacao.append(1)
else:
    pontuacao.append(2)
st.write("---")

st.subheader("4. Interesses restritos ou obsessivos por determinados temas?")
st.write("Exemplo...")
resposta = st.radio("", ("Não", "Pouco", "Muito"), key="q4")
if resposta == "Não":
    pontuacao.append(0)
elif resposta == "Pouco":
    pontuacao.append(1)
else:
    pontuacao.append(2)
st.write("---")

st.subheader("5. Apresenta comportamentos repetitivos ou ritualizados?")
st.write("Exemplo...")
resposta = st.radio("", ("Não", "Pouco", "Muito"), key="q5")
if resposta == "Não":
    pontuacao.append(0)
elif resposta == "Pouco":
    pontuacao.append(1)
else:
    pontuacao.append(2)
st.write("---")

st.subheader("6. Sensibilidade a determinados sons, texturas ou luzes?")
st.write("Exemplo...")
resposta = st.radio("", ("Não", "Pouco", "Muito"), key="q6")
if resposta == "Não":
    pontuacao.append(0)
elif resposta == "Pouco":
    pontuacao.append(1)
else:
    pontuacao.append(2)
st.write("---")

st.subheader("7. Dificuldade em lidar com mudanças na rotina?")
st.write("Exemplo...")
resposta = st.radio("", ("Não", "Pouco", "Muito"), key="q7")
if resposta == "Não":
    pontuacao.append(0)
elif resposta == "Pouco":
    pontuacao.append(1)
else:
    pontuacao.append(2)
st.write("---")

st.subheader("8. Dificuldade em entender piadas, metáforas ou sarcasmo?")
st.write("Exemplo...")
resposta = st.radio("", ("Não", "Pouco", "Muito"), key="q8")
if resposta == "Não":
    pontuacao.append(0)
elif resposta == "Pouco":
    pontuacao.append(1)
else:
    pontuacao.append(2)
st.write("---")

st.subheader("9. Dificuldade em compreender regras sociais e se adaptar a diferentes contextos?")
st.write("Exemplo...")
resposta = st.radio("", ("Não", "Pouco", "Muito"), key="q9")
if resposta == "Não":
    pontuacao.append(0)
elif resposta == "Pouco":
    pontuacao.append(1)
else:
    pontuacao.append(2)
st.write("---")

st.subheader("10. Dificuldade em se colocar no lugar dos outros?")
st.write("Exemplo...")
resposta = st.radio("", ("Não", "Pouco", "Muito"), key="q10")
if resposta == "Não":
    pontuacao.append(0)
elif resposta == "Pouco":
    pontuacao.append(1)
else:
    pontuacao.append(2)
st.write("---")

st.subheader("11. Dificuldade em expressar suas próprias emoções?")
st.write("Exemplo...")
resposta = st.radio("", ("Não", "Pouco", "Muito"), key="q11")
if resposta == "Não":
    pontuacao.append(0)
elif resposta == "Pouco":
    pontuacao.append(1)
else:
    pontuacao.append(2)
st.write("---")

st.subheader("12. Dificuldade em entender instruções complexas?")
st.write("Exemplo...")
resposta = st.radio("", ("Não", "Pouco", "Muito"), key="q12")
if resposta == "Não":
    pontuacao.append(0)
elif resposta == "Pouco":
    pontuacao.append(1)
else:
    pontuacao.append(2)
st.write("---")

st.subheader("13. Dificuldade em se organizar e planejar tarefas?")
st.write("Exemplo...")
resposta = st.radio("", ("Não", "Pouco", "Muito"), key="q13")
if resposta == "Não":
    pontuacao.append(0)
elif resposta == "Pouco":
    pontuacao.append(1)
else:
    pontuacao.append(2)
st.write("---")

st.subheader("14. Dificuldade em lidar com situações inesperadas?")
st.write("Exemplo...")
resposta = st.radio("", ("Não", "Pouco", "Muito"), key="q14")
if resposta == "Não":
    pontuacao.append(0)
elif resposta == "Pouco":
    pontuacao.append(1)
else:
    pontuacao.append(2)
st.write("---")

st.subheader("15. Dificuldade em manter a atenção por longos períodos?")
st.write("Exemplo...")
resposta = st.radio("", ("Não", "Pouco", "Muito"), key="q15")
if resposta == "Não":
    pontuacao.append(0)
elif resposta == "Pouco":
    pontuacao.append(1)
else:
    pontuacao.append(2)
st.write("---")

st.subheader("16. Dificuldade em se adaptar a ambientes barulhentos ou com muitos estímulos?")
st.write("Exemplo...")
resposta = st.radio("", ("Não", "Pouco", "Muito"), key="q16")
if resposta == "Não":
    pontuacao.append(0)
elif resposta == "Pouco":
    pontuacao.append(1)
else:
    pontuacao.append(2)
st.write("---")

st.subheader("17. Dificuldade em entender expressões faciais e linguagem corporal?")
st.write("Exemplo...")
resposta = st.radio("", ("Não", "Pouco", "Muito"), key="q17")
if resposta == "Não":
    pontuacao.append(0)
elif resposta == "Pouco":
    pontuacao.append(1)
else:
    pontuacao.append(2)
st.write("---")

st.subheader("18. Dificuldade em fazer amizades e manter relacionamentos?")
st.write("Exemplo...")
resposta = st.radio("", ("Não", "Pouco", "Muito"), key="q18")
if resposta == "Não":
    pontuacao.append(0)
elif resposta == "Pouco":
    pontuacao.append(1)
else:
    pontuacao.append(2)
st.write("---")

st.subheader("19. Dificuldade em entender e seguir regras sociais?")
st.write("Exemplo...")
resposta = st.radio("", ("Não", "Pouco", "Muito"), key="q19")
if resposta == "Não":
    pontuacao.append(0)
elif resposta == "Pouco":
    pontuacao.append(1)
else:
    pontuacao.append(2)
st.write("---")

st.subheader("20. Dificuldade em lidar com mudanças de rotina ou transições?")
st.write("Exemplo...")
resposta = st.radio("", ("Não", "Pouco", "Muito"), key="q20")
if resposta == "Não":
    pontuacao.append(0)
elif resposta == "Pouco":
    pontuacao.append(1)
else:
    pontuacao.append(2)
st.write("---")

st.subheader("21. Dificuldade em entender instruções verbais complexas?")
st.write("Exemplo...")
resposta = st.radio("", ("Não", "Pouco", "Muito"), key="q21")
if resposta == "Não":
    pontuacao.append(0)
elif resposta == "Pouco":
    pontuacao.append(1)
else:
    pontuacao.append(2)
st.write("---")

st.subheader("22. Dificuldade em se concentrar em tarefas que não lhe interessam?")
st.write("Exemplo...")
resposta = st.radio("", ("Não", "Pouco", "Muito"), key="q22")
if resposta == "Não":
    pontuacao.append(0)
elif resposta == "Pouco":
    pontuacao.append(1)
else:
    pontuacao.append(2)
st.write("---")

st.subheader("23. Dificuldade em entender piadas, metáforas ou sarcasmo?")
st.write("Exemplo...")
resposta = st.radio("", ("Não", "Pouco", "Muito"), key="q23")
if resposta == "Não":
    pontuacao.append(0)
elif resposta == "Pouco":
    pontuacao.append(1)
else:
    pontuacao.append(2)
st.write("---")

st.subheader("24. Dificuldade em se adaptar a ambientes com muitas pessoas?")
st.write("Exemplo...")
resposta = st.radio("", ("Não", "Pouco", "Muito"), key="q24")
if resposta == "Não":
    pontuacao.append(0)
elif resposta == "Pouco":
    pontuacao.append(1)
else:
    pontuacao.append(2)
st.write("---")

st.subheader("25. Dificuldade em entender e responder a perguntas?")
st.write("Exemplo...")
resposta = st.radio("", ("Não", "Pouco", "Muito"), key="q25")
if resposta == "Não":
    pontuacao.append(0)
elif resposta == "Pouco":
    pontuacao.append(1)
else:
    pontuacao.append(2)
st.write("---")

st.subheader("26. Dificuldade em lidar com situações sociais desconhecidas?")
st.write("Exemplo...")
resposta = st.radio("", ("Não", "Pouco", "Muito"), key="q26")
if resposta == "Não":
    pontuacao.append(0)
elif resposta == "Pouco":
    pontuacao.append(1)
else:
    pontuacao.append(2)
st.write("---")

st.subheader("27. Dificuldade em entender e seguir regras sociais implícitas?")
st.write("Exemplo...")
resposta = st.radio("", ("Não", "Pouco", "Muito"), key="q27")
if resposta == "Não":
    pontuacao.append(0)
elif resposta == "Pouco":
    pontuacao.append(1)
else:
    pontuacao.append(2)
st.write("---")

st.subheader("28. Dificuldade em lidar com mudanças inesperadas na rotina?")
st.write("Exemplo...")
resposta = st.radio("", ("Não", "Pouco", "Muito"), key="q28")
if resposta == "Não":
    pontuacao.append(0)
elif resposta == "Pouco":
    pontuacao.append(1)
else:
    pontuacao.append(2)
st.write("---")

st.subheader("29. Dificuldade em entender e interpretar as emoções dos outros?")
st.write("Exemplo...")
resposta = st.radio("", ("Não", "Pouco", "Muito"), key="q29")
if resposta == "Não":
    pontuacao.append(0)
elif resposta == "Pouco":
    pontuacao.append(1)
else:
    pontuacao.append(2)
st.write("---")

st.subheader("30. Dificuldade em se comunicar de forma efetiva?")
st.write("Exemplo...")
resposta = st.radio("", ("Não", "Pouco", "Muito"), key="q30")
if resposta == "Não":
    pontuacao.append(0)
elif resposta == "Pouco":
    pontuacao.append(1)
else:
    pontuacao.append(2)
st.write("---")

if st.button("Diagnosticar"):
    total_score = sum(pontuacao)
    
    with st.sidebar:
        st.subheader("Resultado do Diagnóstico")
        
        if total_score >= 60:
            st.write("Diagnóstico: Provável TEA de nível 3.")
            st.write("Nível 3")
            st.write("Requer muito apoio. Dificuldades graves de comunicação social que causam prejuízos graves no funcionamento. Comportamentos restritos e repetitivos causam sofrimento extremo.")
        elif total_score >= 40:
            st.write("Diagnóstico: Provável TEA de nível 2.")
            st.write("Nível 2")
            st.write("Requer apoio substancial. Dificuldades notáveis de comunicação social. Comportamentos restritos e repetitivos aparecem com frequência e são evidentes para observadores casuais.")
        elif total_score >= 20:
            st.write("Diagnóstico: Provável TEA de nível 1.")
            st.write("Nível 1")
            st.write("Requer apoio. Dificuldades de comunicação social sem ajuda in situ. Comportamentos restritos e repetitivos causam interferência significativa no funcionamento em um ou mais contextos.")
        else:
            st.write("Diagnóstico: Baixa probabilidade de TEA.")
            st.write("Baixa probabilidade")
