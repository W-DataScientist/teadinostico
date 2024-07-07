import streamlit as st

# Título e introdução
st.title("Aplicativo de Diagnóstico de Transtorno do Espectro Autista (TEA)")
st.write("Este aplicativo irá ajudá-lo a identificar o nível de Transtorno do Espectro Autista (TEA) com base em suas respostas a 30 perguntas.")

# Informações do usuário
st.header("Informações do Usuário")
genero = st.radio("Selecione o gênero do paciente:", ("Masculino", "Feminino"), key="genero")
idade = st.number_input("Digite a idade do paciente:", min_value=0, step=1, key="idade")

# Instruções
st.header("Instruções")
st.write("Responda às 30 perguntas abaixo selecionando 'Não', 'Pouco' ou 'Muito' para cada uma delas. Ao final, o aplicativo irá fornecer um diagnóstico indicando o nível de TEA.")

# Questionário de 30 perguntas
st.header("Questionário")
pontuacao = []

st.subheader("1. Evita contato visual com outras pessoas?")
resposta = st.radio("", ("Não", "Pouco", "Muito"), key="q1")
if resposta == "Não":
    pontuacao.append(0)
elif resposta == "Pouco":
    pontuacao.append(1)
else:
    pontuacao.append(2)

st.subheader("2. Dificuldade em entender as emoções e expressões faciais dos outros?")
resposta = st.radio("", ("Não", "Pouco", "Muito"), key="q2")
if resposta == "Não":
    pontuacao.append(0)
elif resposta == "Pouco":
    pontuacao.append(1)
else:
    pontuacao.append(2)

st.subheader("3. Dificuldade em iniciar ou manter conversas?")
resposta = st.radio("", ("Não", "Pouco", "Muito"), key="q3")
if resposta == "Não":
    pontuacao.append(0)
elif resposta == "Pouco":
    pontuacao.append(1)
else:
    pontuacao.append(2)

st.subheader("4. Interesses restritos ou obsessivos por determinados temas?")
resposta = st.radio("", ("Não", "Pouco", "Muito"), key="q4")
if resposta == "Não":
    pontuacao.append(0)
elif resposta == "Pouco":
    pontuacao.append(1)
else:
    pontuacao.append(2)

st.subheader("5. Apresenta comportamentos repetitivos ou ritualizados?")
resposta = st.radio("", ("Não", "Pouco", "Muito"), key="q5")
if resposta == "Não":
    pontuacao.append(0)
elif resposta == "Pouco":
    pontuacao.append(1)
else:
    pontuacao.append(2)

st.subheader("6. Sensibilidade a determinados sons, texturas ou luzes?")
resposta = st.radio("", ("Não", "Pouco", "Muito"), key="q6")
if resposta == "Não":
    pontuacao.append(0)
elif resposta == "Pouco":
    pontuacao.append(1)
else:
    pontuacao.append(2)

st.subheader("7. Dificuldade em lidar com mudanças na rotina?")
resposta = st.radio("", ("Não", "Pouco", "Muito"), key="q7")
if resposta == "Não":
    pontuacao.append(0)
elif resposta == "Pouco":
    pontuacao.append(1)
else:
    pontuacao.append(2)

st.subheader("8. Dificuldade em entender piadas, metáforas ou sarcasmo?")
resposta = st.radio("", ("Não", "Pouco", "Muito"), key="q8")
if resposta == "Não":
    pontuacao.append(0)
elif resposta == "Pouco":
    pontuacao.append(1)
else:
    pontuacao.append(2)

st.subheader("9. Dificuldade em compreender regras sociais e se adaptar a diferentes contextos?")
resposta = st.radio("", ("Não", "Pouco", "Muito"), key="q9")
if resposta == "Não":
    pontuacao.append(0)
elif resposta == "Pouco":
    pontuacao.append(1)
else:
    pontuacao.append(2)

st.subheader("10. Dificuldade em se colocar no lugar dos outros?")
resposta = st.radio("", ("Não", "Pouco", "Muito"), key="q10")
if resposta == "Não":
    pontuacao.append(0)
elif resposta == "Pouco":
    pontuacao.append(1)
else:
    pontuacao.append(2)

st.subheader("11. Dificuldade em expressar suas próprias emoções?")
resposta = st.radio("", ("Não", "Pouco", "Muito"), key="q11")
if resposta == "Não":
    pontuacao.append(0)
elif resposta == "Pouco":
    pontuacao.append(1)
else:
    pontuacao.append(2)

st.subheader("12. Dificuldade em entender instruções complexas?")
resposta = st.radio("", ("Não", "Pouco", "Muito"), key="q12")
if resposta == "Não":
    pontuacao.append(0)
elif resposta == "Pouco":
    pontuacao.append(1)
else:
    pontuacao.append(2)

st.subheader("13. Dificuldade em se organizar e planejar tarefas?")
resposta = st.radio("", ("Não", "Pouco", "Muito"), key="q13")
if resposta == "Não":
    pontuacao.append(0)
elif resposta == "Pouco":
    pontuacao.append(1)
else:
    pontuacao.append(2)

st.subheader("14. Dificuldade em lidar com situações inesperadas?")
resposta = st.radio("", ("Não", "Pouco", "Muito"), key="q14")
if resposta == "Não":
    pontuacao.append(0)
elif resposta == "Pouco":
    pontuacao.append(1)
else:
    pontuacao.append(2)

st.subheader("15. Dificuldade em manter a atenção por longos períodos?")
resposta = st.radio("", ("Não", "Pouco", "Muito"), key="q15")
if resposta == "Não":
    pontuacao.append(0)
elif resposta == "Pouco":
    pontuacao.append(1)
else:
    pontuacao.append(2)

st.subheader("16. Dificuldade em se adaptar a ambientes barulhentos ou com muitos estímulos?")
resposta = st.radio("", ("Não", "Pouco", "Muito"), key="q16")
if resposta == "Não":
    pontuacao.append(0)
elif resposta == "Pouco":
    pontuacao.append(1)
else:
    pontuacao.append(2)

st.subheader("17. Dificuldade em entender expressões faciais e linguagem corporal?")
resposta = st.radio("", ("Não", "Pouco", "Muito"), key="q17")
if resposta == "Não":
    pontuacao.append(0)
elif resposta == "Pouco":
    pontuacao.append(1)
else:
    pontuacao.append(2)

st.subheader("18. Dificuldade em fazer amizades e manter relacionamentos?")
resposta = st.radio("", ("Não", "Pouco", "Muito"), key="q18")
if resposta == "Não":
    pontuacao.append(0)
elif resposta == "Pouco":
    pontuacao.append(1)
else:
    pontuacao.append(2)

st.subheader("19. Dificuldade em entender e seguir regras sociais?")
resposta = st.radio("", ("Não", "Pouco", "Muito"), key="q19")
if resposta == "Não":
    pontuacao.append(0)
elif resposta == "Pouco":
    pontuacao.append(1)
else:
    pontuacao.append(2)

st.subheader("20. Dificuldade em lidar com mudanças de rotina ou transições?")
resposta = st.radio("", ("Não", "Pouco", "Muito"), key="q20")
if resposta == "Não":
    pontuacao.append(0)
elif resposta == "Pouco":
    pontuacao.append(1)
else:
    pontuacao.append(2)

st.subheader("21. Dificuldade em entender instruções verbais complexas?")
resposta = st.radio("", ("Não", "Pouco", "Muito"), key="q21")
if resposta == "Não":
    pontuacao.append(0)
elif resposta == "Pouco":
    pontuacao.append(1)
else:
    pontuacao.append(2)

st.subheader("22. Dificuldade em se concentrar em tarefas que não lhe interessam?")
resposta = st.radio("", ("Não", "Pouco", "Muito"), key="q22")
if resposta == "Não":
    pontuacao.append(0)
elif resposta == "Pouco":
    pontuacao.append(1)
else:
    pontuacao.append(2)

st.subheader("23. Dificuldade em entender piadas, metáforas ou sarcasmo?")
resposta = st.radio("", ("Não", "Pouco", "Muito"), key="q23")
if resposta == "Não":
    pontuacao.append(0)
elif resposta == "Pouco":
    pontuacao.append(1)
else:
    pontuacao.append(2)

st.subheader("24. Dificuldade em se adaptar a ambientes com muitas pessoas?")
resposta = st.radio("", ("Não", "Pouco", "Muito"), key="q24")
if resposta == "Não":
    pontuacao.append(0)
elif resposta == "Pouco":
    pontuacao.append(1)
else:
    pontuacao.append(2)

st.subheader("25. Dificuldade em entender e responder a perguntas?")
resposta = st.radio("", ("Não", "Pouco", "Muito"), key="q25")
if resposta == "Não":
    pontuacao.append(0)
elif resposta == "Pouco":
    pontuacao.append(1)
else:
    pontuacao.append(2)

st.subheader("26. Dificuldade em lidar com situações sociais desconhecidas?")
resposta = st.radio("", ("Não", "Pouco", "Muito"), key="q26")
if resposta == "Não":
    pontuacao.append(0)
elif resposta == "Pouco":
    pontuacao.append(1)
else:
    pontuacao.append(2)

st.subheader("27. Dificuldade em entender e seguir regras sociais implícitas?")
resposta = st.radio("", ("Não", "Pouco", "Muito"), key="q27")
if resposta == "Não":
    pontuacao.append(0)
elif resposta == "Pouco":
    pontuacao.append(1)
else:
    pontuacao.append(2)

st.subheader("28. Dificuldade em lidar com mudanças inesperadas na rotina?")
resposta = st.radio("", ("Não", "Pouco", "Muito"), key="q28")
if resposta == "Não":
    pontuacao.append(0)
elif resposta == "Pouco":
    pontuacao.append(1)
else:
    pontuacao.append(2)

st.subheader("29. Dificuldade em entender e interpretar as emoções dos outros?")
resposta = st.radio("", ("Não", "Pouco", "Muito"), key="q29")
if resposta == "Não":
    pontuacao.append(0)
elif resposta == "Pouco":
    pontuacao.append(1)
else:
    pontuacao.append(2)

st.subheader("30. Dificuldade em se comunicar de forma efetiva?")
resposta = st.radio("", ("Não", "Pouco", "Muito"), key="q30")
if resposta == "Não":
    pontuacao.append(0)
elif resposta == "Pouco":
    pontuacao.append(1)
else:
    pontuacao.append(2)

# Cálculo do nível de TEA
pontuacao_total = sum(pontuacao)

if len(pontuacao) == 30:
    st.header("Resultado do Diagnóstico")
    if pontuacao_total < 30:
        if genero == "Masculino" and idade < 18:
            st.write("Com base nas respostas fornecidas e informações do paciente, ele apresenta sintomas leves de Transtorno do Espectro Autista (TEA) para um homem de sua idade.")
        elif genero == "Masculino" and idade >= 18:
            st.write("Com base nas respostas fornecidas e informações do paciente, ele apresenta sintomas leves de Transtorno do Espectro Autista (TEA) para um homem adulto.")
        elif genero == "Feminino" and idade < 18:
            st.write("Com base nas respostas fornecidas e informações do paciente, ela apresenta sintomas leves de Transtorno do Espectro Autista (TEA) para uma mulher de sua idade.")
        else:
            st.write("Com base nas respostas fornecidas e informações do paciente, ela apresenta sintomas leves de Transtorno do Espectro Autista (TEA) para uma mulher adulta.")
    elif pontuacao_total < 60:
        if genero == "Masculino" and idade < 18:
            st.write("Com base nas respostas fornecidas e informações do paciente, ele apresenta sintomas moderados de Transtorno do Espectro Autista (TEA) para um homem de sua idade.")
        elif genero == "Masculino" and idade >= 18:
            st.write("Com base nas respostas fornecidas e informações do paciente, ele apresenta sintomas moderados de Transtorno do Espectro Autista (TEA) para um homem adulto.")
        elif genero == "Feminino" and idade
