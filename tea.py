import streamlit as st

# Título e introdução
st.title("Aplicativo de Diagnóstico de Transtorno do Espectro Autista (TEA)")
st.write("Este aplicativo irá ajudá-lo a identificar o nível de Transtorno do Espectro Autista (TEA) com base em suas respostas a 30 perguntas.")

# Informações do usuário
st.header("Informações do Usuário")
gender = st.radio("Selecione o gênero do paciente:", ("Masculino", "Feminino"))
age = st.number_input("Digite a idade do paciente:", min_value=0, step=1)

# Instruções
st.header("Instruções")
st.write("Responda às 30 perguntas abaixo selecionando 'Não', 'Pouco' ou 'Muito' para cada uma delas. Ao final, o aplicativo irá fornecer um diagnóstico indicando o nível de TEA.")

# Questionário de 30 perguntas
st.header("Questionário")
scores = []

st.subheader("1. Dificuldade em se comunicar e interagir socialmente?")
answer = st.radio("", ("Não", "Pouco", "Muito"))
if answer == "Não":
    scores.append(0)
elif answer == "Pouco":
    scores.append(1)
else:
    scores.append(2)

st.subheader("2. Evita contato visual com outras pessoas?")
answer = st.radio("", ("Não", "Pouco", "Muito"))
if answer == "Não":
    scores.append(0)
elif answer == "Pouco":
    scores.append(1)
else:
    scores.append(2)

st.subheader("3. Dificuldade em entender as emoções e expressões faciais dos outros?")
answer = st.radio("", ("Não", "Pouco", "Muito"))
if answer == "Não":
    scores.append(0)
elif answer == "Pouco":
    scores.append(1)
else:
    scores.append(2)

st.subheader("4. Dificuldade em iniciar ou manter conversas?")
answer = st.radio("", ("Não", "Pouco", "Muito"))
if answer == "Não":
    scores.append(0)
elif answer == "Pouco":
    scores.append(1)
else:
    scores.append(2)

st.subheader("5. Interesses restritos ou obsessivos por determinados temas?")
answer = st.radio("", ("Não", "Pouco", "Muito"))
if answer == "Não":
    scores.append(0)
elif answer == "Pouco":
    scores.append(1)
else:
    scores.append(2)

st.subheader("6. Apresenta comportamentos repetitivos ou ritualizados?")
answer = st.radio("", ("Não", "Pouco", "Muito"))
if answer == "Não":
    scores.append(0)
elif answer == "Pouco":
    scores.append(1)
else:
    scores.append(2)

st.subheader("7. Sensibilidade a determinados sons, texturas ou luzes?")
answer = st.radio("", ("Não", "Pouco", "Muito"))
if answer == "Não":
    scores.append(0)
elif answer == "Pouco":
    scores.append(1)
else:
    scores.append(2)

st.subheader("8. Dificuldade em lidar com mudanças na rotina?")
answer = st.radio("", ("Não", "Pouco", "Muito"))
if answer == "Não":
    scores.append(0)
elif answer == "Pouco":
    scores.append(1)
else:
    scores.append(2)

st.subheader("9. Dificuldade em entender piadas, metáforas ou sarcasmo?")
answer = st.radio("", ("Não", "Pouco", "Muito"))
if answer == "Não":
    scores.append(0)
elif answer == "Pouco":
    scores.append(1)
else:
    scores.append(2)

st.subheader("10. Dificuldade em compreender regras sociais e se adaptar a diferentes contextos?")
answer = st.radio("", ("Não", "Pouco", "Muito"))
if answer == "Não":
    scores.append(0)
elif answer == "Pouco":
    scores.append(1)
else:
    scores.append(2)

st.subheader("11. Dificuldade em se colocar no lugar dos outros?")
answer = st.radio("", ("Não", "Pouco", "Muito"))
if answer == "Não":
    scores.append(0)
elif answer == "Pouco":
    scores.append(1)
else:
    scores.append(2)

st.subheader("12. Dificuldade em expressar suas próprias emoções?")
answer = st.radio("", ("Não", "Pouco", "Muito"))
if answer == "Não":
    scores.append(0)
elif answer == "Pouco":
    scores.append(1)
else:
    scores.append(2)

st.subheader("13. Dificuldade em entender instruções complexas?")
answer = st.radio("", ("Não", "Pouco", "Muito"))
if answer == "Não":
    scores.append(0)
elif answer == "Pouco":
    scores.append(1)
else:
    scores.append(2)

st.subheader("14. Dificuldade em se organizar e planejar tarefas?")
answer = st.radio("", ("Não", "Pouco", "Muito"))
if answer == "Não":
    scores.append(0)
elif answer == "Pouco":
    scores.append(1)
else:
    scores.append(2)

st.subheader("15. Dificuldade em lidar com situações inesperadas?")
answer = st.radio("", ("Não", "Pouco", "Muito"))
if answer == "Não":
    scores.append(0)
elif answer == "Pouco":
    scores.append(1)
else:
    scores.append(2)

st.subheader("16. Dificuldade em manter a atenção por longos períodos?")
answer = st.radio("", ("Não", "Pouco", "Muito"))
if answer == "Não":
    scores.append(0)
elif answer == "Pouco":
    scores.append(1)
else:
    scores.append(2)

st.subheader("17. Dificuldade em se adaptar a ambientes barulhentos ou com muitos estímulos?")
answer = st.radio("", ("Não", "Pouco", "Muito"))
if answer == "Não":
    scores.append(0)
elif answer == "Pouco":
    scores.append(1)
else:
    scores.append(2)

st.subheader("18. Dificuldade em entender expressões faciais e linguagem corporal?")
answer = st.radio("", ("Não", "Pouco", "Muito"))
if answer == "Não":
    scores.append(0)
elif answer == "Pouco":
    scores.append(1)
else:
    scores.append(2)

st.subheader("19. Dificuldade em fazer amizades e manter relacionamentos?")
answer = st.radio("", ("Não", "Pouco", "Muito"))
if answer == "Não":
    scores.append(0)
elif answer == "Pouco":
    scores.append(1)
else:
    scores.append(2)

st.subheader("20. Dificuldade em entender e seguir regras sociais?")
answer = st.radio("", ("Não", "Pouco", "Muito"))
if answer == "Não":
    scores.append(0)
elif answer == "Pouco":
    scores.append(1)
else:
    scores.append(2)

st.subheader("21. Dificuldade em lidar com mudanças de rotina ou transições?")
answer = st.radio("", ("Não", "Pouco", "Muito"))
if answer == "Não":
    scores.append(0)
elif answer == "Pouco":
    scores.append(1)
else:
    scores.append(2)

st.subheader("22. Dificuldade em entender instruções verbais complexas?")
answer = st.radio("", ("Não", "Pouco", "Muito"))
if answer == "Não":
    scores.append(0)
elif answer == "Pouco":
    scores.append(1)
else:
    scores.append(2)

st.subheader("23. Dificuldade em se concentrar em tarefas que não lhe interessam?")
answer = st.radio("", ("Não", "Pouco", "Muito"))
if answer == "Não":
    scores.append(0)
elif answer == "Pouco":
    scores.append(1)
else:
    scores.append(2)

st.subheader("24. Dificuldade em entender piadas, metáforas ou sarcasmo?")
answer = st.radio("", ("Não", "Pouco", "Muito"))
if answer == "Não":
    scores.append(0)
elif answer == "Pouco":
    scores.append(1)
else:
    scores.append(2)

st.subheader("25. Dificuldade em se adaptar a ambientes com muitas pessoas?")
answer = st.radio("", ("Não", "Pouco", "Muito"))
if answer == "Não":
    scores.append(0)
elif answer == "Pouco":
    scores.append(1)
else:
    scores.append(2)

st.subheader("26. Dificuldade em entender e responder a perguntas?")
answer = st.radio("", ("Não", "Pouco", "Muito"))
if answer == "Não":
    scores.append(0)
elif answer == "Pouco":
    scores.append(1)
else:
    scores.append(2)

st.subheader("27. Dificuldade em lidar com situações sociais desconhecidas?")
answer = st.radio("", ("Não", "Pouco", "Muito"))
if answer == "Não":
    scores.append(0)
elif answer == "Pouco":
    scores.append(1)
else:
    scores.append(2)

st.subheader("28. Dificuldade em entender e seguir regras sociais implícitas?")
answer = st.radio("", ("Não", "Pouco", "Muito"))
if answer == "Não":
    scores.append(0)
elif answer == "Pouco":
    scores.append(1)
else:
    scores.append(2)

st.subheader("29. Dificuldade em lidar com mudanças inesperadas na rotina?")
answer = st.radio("", ("Não", "Pouco", "Muito"))
if answer == "Não":
    scores.append(0)
elif answer == "Pouco":
    scores.append(1)
else:
    scores.append(2)

st.subheader("30. Dificuldade em entender e interpretar as emoções dos outros?")
answer = st.radio("", ("Não", "Pouco", "Muito"))
if answer == "Não":
    scores.append(0)
elif answer == "Pouco":
    scores.append(1)
else:
    scores.append(2)

# Cálculo do nível de TEA
total_score = sum(scores)
if total_score < 30:
    st.header("Resultado do Diagnóstico")
    if gender == "Masculino" and age < 18:
        st.write("Com base nas respostas fornecidas e informações do paciente, ele apresenta sintomas leves de Transtorno do Espectro Autista (TEA) para um homem de sua idade.")
    elif gender == "Masculino" and age >= 18:
        st.write("Com base nas respostas fornecidas e informações do paciente, ele apresenta sintomas leves de Transtorno do Espectro Autista (TEA) para um homem adulto.")
    elif gender == "Feminino" and age < 18:
        st.write("Com base nas respostas fornecidas e informações do paciente, ela apresenta sintomas leves de Transtorno do Espectro Autista (TEA) para uma mulher de sua idade.")
    else:
        st.write("Com base nas respostas fornecidas e informações do paciente, ela apresenta sintomas leves de Transtorno do Espectro Autista (TEA) para uma mulher adulta.")
elif total_score < 60:
    st.header("Resultado do Diagnóstico")
    if gender == "Masculino" and age < 18:
        st.write("Com base nas respostas fornecidas e informações do paciente, ele apresenta sintomas moderados de Transtorno do Espectro Autista (TEA) para um homem de sua idade.")
    elif gender == "Masculino" and age >= 18:
        st.write("Com base nas respostas fornecidas e informações do paciente, ele apresenta sintomas moderados de Transtorno do Espectro Autista (TEA) para um homem adulto.")
    elif gender == "Feminino" and age < 18:
        st.write("Com base nas respostas fornecidas e informações do paciente, ela apresenta sintomas moderados de Transtorno do Espectro Autista (TEA) para uma mulher de sua idade.")
    else:
        st.write("Com base nas respostas fornecidas e informações do paciente, ela apresenta sintomas moderados de Transtorno do Espectro Autista (TEA) para uma mulher adulta.")
else:
    st.header("Resultado do Diagnóstico")
    if gender == "Masculino" and age < 18:
        st.write("Com base nas respostas fornecidas e informações do paciente, ele apresenta sintomas graves de Transtorno do Espectro Autista (TEA) para um homem de sua idade.")
    elif gender == "Masculino" and age >= 18:
        st.write("Com base nas respostas fornecidas e informações do paciente, ele apresenta sintomas graves de Transtorno do Espectro Autista (TEA) para um homem adulto.")
    elif gender == "Feminino" and age < 18:
        st.write("Com base nas respostas fornecidas e informações do paciente, ela apresenta sintomas graves de Transtorno do Espectro Autista (TEA) para uma mulher de sua idade.")
    else:
        st.write("Com base nas respostas fornecidas e informações do paciente, ela apresenta sintomas graves de Transtorno do Espectro Autista (TEA) para uma mulher adulta.")
