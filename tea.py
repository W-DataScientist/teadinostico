import streamlit as st

st.title("Questionário de Diagnóstico de Transtorno do Espectro Autista (TEA)")

st.write("Olá! Vamos começar com um questionário de 30 perguntas relacionadas ao TEA. Ao final, você poderá clicar no botão 'Diagnosticar' para obter o resultado.")

st.subheader("Informações Pessoais")

sex = st.radio("Sexo:", ("Masculino", "Feminino"), key="sex")
age = st.slider("Idade:", min_value=1, max_value=20, step=1, key="age")

st.subheader("Questionário")

pontuacao = []

st.subheader("1. Evita contato visual com outras pessoas?")
resposta = st.radio("", ("Não", "Pouco", "Muito"), key="q1")
if resposta == "Não":
    pontuacao.append(0)
elif resposta == "Pouco":
    pontuacao.append(1)
else:
    pontuacao.append(2)
st.write("---")

st.subheader("2. Dificuldade em entender as emoções e expressões faciais dos outros?")
resposta = st.radio("", ("Não", "Pouco", "Muito"), key="q2")
if resposta == "Não":
    pontuacao.append(0)
elif resposta == "Pouco":
    pontuacao.append(1)
else:
    pontuacao.append(2)
st.write("---")

st.subheader("3. Dificuldade em iniciar ou manter conversas?")
resposta = st.radio("", ("Não", "Pouco", "Muito"), key="q3")
if resposta == "Não":
    pontuacao.append(0)
elif resposta == "Pouco":
    pontuacao.append(1)
else:
    pontuacao.append(2)
st.write("---")

st.subheader("4. Interesses restritos ou obsessivos por determinados temas?")
resposta = st.radio("", ("Não", "Pouco", "Muito"), key="q4")
if resposta == "Não":
    pontuacao.append(0)
elif resposta == "Pouco":
    pontuacao.append(1)
else:
    pontuacao.append(2)
st.write("---")

st.subheader("5. Apresenta comportamentos repetitivos ou ritualizados?")
resposta = st.radio("", ("Não", "Pouco", "Muito"), key="q5")
if resposta == "Não":
    pontuacao.append(0)
elif resposta == "Pouco":
    pontuacao.append(1)
else:
    pontuacao.append(2)
st.write("---")

st.subheader("6. Sensibilidade a determinados sons, texturas ou luzes?")
resposta = st.radio("", ("Não", "Pouco", "Muito"), key="q6")
if resposta == "Não":
    pontuacao.append(0)
elif resposta == "Pouco":
    pontuacao.append(1)
else:
    pontuacao.append(2)
st.write("---")

st.subheader("7. Dificuldade em lidar com mudanças na rotina?")
resposta = st.radio("", ("Não", "Pouco", "Muito"), key="q7")
if resposta == "Não":
    pontuacao.append(0)
elif resposta == "Pouco":
    pontuacao.append(1)
else:
    pontuacao.append(2)
st.write("---")

st.subheader("8. Dificuldade em entender piadas, metáforas ou sarcasmo?")
resposta = st.radio("", ("Não", "Pouco", "Muito"), key="q8")
if resposta == "Não":
    pontuacao.append(0)
elif resposta == "Pouco":
    pontuacao.append(1)
else:
    pontuacao.append(2)
st.write("---")

st.subheader("9. Dificuldade em compreender regras sociais e se adaptar a diferentes contextos?")
resposta = st.radio("", ("Não", "Pouco", "Muito"), key="q9")
if resposta == "Não":
    pontuacao.append(0)
elif resposta == "Pouco":
    pontuacao.append(1)
else:
    pontuacao.append(2)
st.write("---")

st.subheader("10. Dificuldade em se colocar no lugar dos outros?")
resposta = st.radio("", ("Não", "Pouco", "Muito"), key="q10")
if resposta == "Não":
    pontuacao.append(0)
elif resposta == "Pouco":
    pontuacao.append(1)
else:
    pontuacao.append(2)
st.write("---")

st.subheader("11. Dificuldade em expressar suas próprias emoções?")
resposta = st.radio("", ("Não", "Pouco", "Muito"), key="q11")
if resposta == "Não":
    pontuacao.append(0)
elif resposta == "Pouco":
    pontuacao.append(1)
else:
    pontuacao.append(2)
st.write("---")

st.subheader("12. Dificuldade em entender instruções complexas?")
resposta = st.radio("", ("Não", "Pouco", "Muito"), key="q12")
if resposta == "Não":
    pontuacao.append(0)
elif resposta == "Pouco":
    pontuacao.append(1)
else:
    pontuacao.append(2)
st.write("---")

st.subheader("13. Dificuldade em se organizar e planejar tarefas?")
resposta = st.radio("", ("Não", "Pouco", "Muito"), key="q13")
if resposta == "Não":
    pontuacao.append(0)
elif resposta == "Pouco":
    pontuacao.append(1)
else:
    pontuacao.append(2)
st.write("---")

st.subheader("14. Dificuldade em lidar com situações inesperadas?")
resposta = st.radio("", ("Não", "Pouco", "Muito"), key="q14")
if resposta == "Não":
    pontuacao.append(0)
elif resposta == "Pouco":
    pontuacao.append(1)
else:
    pontuacao.append(2)
st.write("---")

st.subheader("15. Dificuldade em manter a atenção por longos períodos?")
resposta = st.radio("", ("Não", "Pouco", "Muito"), key="q15")
if resposta == "Não":
    pontuacao.append(0)
elif resposta == "Pouco":
    pontuacao.append(1)
else:
    pontuacao.append(2)
st.write("---")

st.subheader("16. Dificuldade em se adaptar a ambientes barulhentos ou com muitos estímulos?")
resposta = st.radio("", ("Não", "Pouco", "Muito"), key="q16")
if resposta == "Não":
    pontuacao.append(0)
elif resposta == "Pouco":
    pontuacao.append(1)
else:
    pontuacao.append(2)
st.write("---")

st.subheader("17. Dificuldade em entender expressões faciais e linguagem corporal?")
resposta = st.radio("", ("Não", "Pouco", "Muito"), key="q17")
if resposta == "Não":
    pontuacao.append(0)
elif resposta == "Pouco":
    pontuacao.append(1)
else:
    pontuacao.append(2)
st.write("---")

st.subheader("18. Dificuldade em fazer amizades e manter relacionamentos?")
resposta = st.radio("", ("Não", "Pouco", "Muito"), key="q18")
if resposta == "Não":
    pontuacao.append(0)
elif resposta == "Pouco":
    pontuacao.append(1)
else:
    pontuacao.append(2)
st.write("---")

st.subheader("19. Dificuldade em entender e seguir regras sociais?")
resposta = st.radio("", ("Não", "Pouco", "Muito"), key="q19")
if resposta == "Não":
    pontuacao.append(0)
elif resposta == "Pouco":
    pontuacao.append(1)
else:
    pontuacao.append(2)
st.write("---")

st.subheader("20. Dificuldade em lidar com mudanças de rotina ou transições?")
resposta = st.radio("", ("Não", "Pouco", "Muito"), key="q20")
if resposta == "Não":
    pontuacao.append(0)
elif resposta == "Pouco":
    pontuacao.append(1)
else:
    pontuacao.append(2)
st.write("---")

st.subheader("21. Coloca os brinquedos em filas ou todos um em cima do outro?")
resposta = st.radio("", ("Não", "Pouco", "Muito"), key="q21")
if resposta == "Não":
    pontuacao.append(0)
elif resposta == "Pouco":
    pontuacao.append(1)
else:
    pontuacao.append(2)
st.write("---")

st.subheader("22. Dificuldade em se concentrar em tarefas que não lhe interessam?")
resposta = st.radio("", ("Não", "Pouco", "Muito"), key="q22")
if resposta == "Não":
    pontuacao.append(0)
elif resposta == "Pouco":
    pontuacao.append(1)
else:
    pontuacao.append(2)
st.write("---")

st.subheader("23. Dificuldade em entender piadas, metáforas ou sarcasmo?")
resposta = st.radio("", ("Não", "Pouco", "Muito"), key="q23")
if resposta == "Não":
    pontuacao.append(0)
elif resposta == "Pouco":
    pontuacao.append(1)
else:
    pontuacao.append(2)
st.write("---")

st.subheader("24. Dificuldade em se adaptar a ambientes com muitas pessoas?")
resposta = st.radio("", ("Não", "Pouco", "Muito"), key="q24")
if resposta == "Não":
    pontuacao.append(0)
elif resposta == "Pouco":
    pontuacao.append(1)
else:
    pontuacao.append(2)
st.write("---")

st.subheader("25. Dificuldade em entender e responder a perguntas?")
resposta = st.radio("", ("Não", "Pouco", "Muito"), key="q25")
if resposta == "Não":
    pontuacao.append(0)
elif resposta == "Pouco":
    pontuacao.append(1)
else:
    pontuacao.append(2)
st.write("---")

st.subheader("26. Dificuldade em lidar com situações sociais desconhecidas?")
resposta = st.radio("", ("Não", "Pouco", "Muito"), key="q26")
if resposta == "Não":
    pontuacao.append(0)
elif resposta == "Pouco":
    pontuacao.append(1)
else:
    pontuacao.append(2)
st.write("---")

st.subheader("27. Dificuldade em entender e seguir regras sociais implícitas?")
resposta = st.radio("", ("Não", "Pouco", "Muito"), key="q27")
if resposta == "Não":
    pontuacao.append(0)
elif resposta == "Pouco":
    pontuacao.append(1)
else:
    pontuacao.append(2)
st.write("---")

st.subheader("28. Anda na ponta dos pés?")
resposta = st.radio("", ("Não", "Pouco", "Muito"), key="q28")
if resposta == "Não":
    pontuacao.append(0)
elif resposta == "Pouco":
    pontuacao.append(1)
else:
    pontuacao.append(2)
st.write("---")

st.subheader("29. Dificuldade em entender e interpretar as emoções dos outros?")
resposta = st.radio("", ("Não", "Pouco", "Muito"), key="q29")
if resposta == "Não":
    pontuacao.append(0)
elif resposta == "Pouco":
    pontuacao.append(1)
else:
    pontuacao.append(2)
st.write("---")

st.subheader("30. Dificuldade em se comunicar de forma efetiva?")
resposta = st.radio("", ("Não", "Pouco", "Muito"), key="q30")
if resposta == "Não":
    pontuacao.append(0)
elif resposta == "Pouco":
    pontuacao.append(1)
else:
    pontuacao.append(2)
st.write("---")

st.subheader("31. Tem dificuldade de receber um 'NÃO' e se agride?")
resposta = st.radio("", ("Não", "Pouco", "Muito"), key="q31")
if resposta == "Não":
    pontuacao.append(0)
elif resposta == "Pouco":
    pontuacao.append(1)
else:
    pontuacao.append(2)
st.write("---")

st.subheader("32. Gosta de objetos ou brinquedos que gira e fica horas observando?")
resposta = st.radio("", ("Não", "Pouco", "Muito"), key="q32")
if resposta == "Não":
    pontuacao.append(0)
elif resposta == "Pouco":
    pontuacao.append(1)
else:
    pontuacao.append(2)
st.write("---")

st.subheader("33. De forma inesperada deixou de fazer algo que comumente fazia?")
resposta = st.radio("", ("Não", "Pouco", "Muito"), key="q33")
if resposta == "Não":
    pontuacao.append(0)
elif resposta == "Pouco":
    pontuacao.append(1)
else:
    pontuacao.append(2)
st.write("---")

st.subheader("34. Aponta para o que quer ao inves de falar?")
resposta = st.radio("", ("Não", "Pouco", "Muito"), key="q34")
if resposta == "Não":
    pontuacao.append(0)
elif resposta == "Pouco":
    pontuacao.append(1)
else:
    pontuacao.append(2)
st.write("---")

if st.button("Diagnosticar"):
    total_score = sum(pontuacao)

    st.write("---")
    st.subheader("Resultado do Diagnóstico")
    
    if total_score >= 65:
        st.write("Provável TEA de nível 3.")
        st.write("Considerações:")
        st.write("Requer muito apoio. Dificuldades graves de comunicação social que causam prejuízos graves no funcionamento. Comportamentos restritos e repetitivos causam sofrimento extremo.")
    elif total_score >= 45:
        st.write("Provável TEA de nível 2.")
        st.write("Considerações:")
        st.write("Requer apoio substancial. Dificuldades notáveis de comunicação social. Comportamentos restritos e repetitivos aparecem com frequência e são evidentes para observadores casuais.")
    elif total_score >= 22:
        st.write("Provável TEA de nível 1.")
        st.write("Considerações:")
        st.write("Requer apoio. Dificuldades de comunicação social sem ajuda in situ. Comportamentos restritos e repetitivos causam interferência significativa no funcionamento em um ou mais contextos.")
    else:
        st.write("Baixa probabilidade de TEA.")
        st.write("Considerações:")
        st.write("Baixa probabilidade de TEA")
