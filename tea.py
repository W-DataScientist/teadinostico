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

for i in range(1, 31):
    st.subheader(f"{i}. Dificuldade em se comunicar e interagir socialmente?")
    resposta = st.radio("", ("Não", "Pouco", "Muito"), key=f"radio_{i}")
    if resposta == "Não":
        pontuacao.append(0)
    elif resposta == "Pouco":
        pontuacao.append(1)
    else:
        pontuacao.append(2)

# Cálculo do nível de TEA
pontuacao_total = sum(pontuacao)
if pontuacao_total < 30:
    st.header("Resultado do Diagnóstico")
    if genero == "Masculino" and idade < 18:
        st.write("Com base nas respostas fornecidas e informações do paciente, ele apresenta sintomas leves de Transtorno do Espectro Autista (TEA) para um homem de sua idade.")
    elif genero == "Masculino" and idade >= 18:
        st.write("Com base nas respostas fornecidas e informações do paciente, ele apresenta sintomas leves de Transtorno do Espectro Autista (TEA) para um homem adulto.")
    elif genero == "Feminino" and idade < 18:
        st.write("Com base nas respostas fornecidas e informações do paciente, ela apresenta sintomas leves de Transtorno do Espectro Autista (TEA) para uma mulher de sua idade.")
    else:
        st.write("Com base nas respostas fornecidas e informações do paciente, ela apresenta sintomas leves de Transtorno do Espectro Autista (TEA) para uma mulher adulta.")
elif pontuacao_total < 60:
    st.header("Resultado do Diagnóstico")
    if genero == "Masculino" and idade < 18:
        st.write("Com base nas respostas fornecidas e informações do paciente, ele apresenta sintomas moderados de Transtorno do Espectro Autista (TEA) para um homem de sua idade.")
    elif genero == "Masculino" and idade >= 18:
        st.write("Com base nas respostas fornecidas e informações do paciente, ele apresenta sintomas moderados de Transtorno do Espectro Autista (TEA) para um homem adulto.")
    elif genero == "Feminino" and idade < 18:
        st.write("Com base nas respostas fornecidas e informações do paciente, ela apresenta sintomas moderados de Transtorno do Espectro Autista (TEA) para uma mulher de sua idade.")
    else:
        st.write("Com base nas respostas fornecidas e informações do paciente, ela apresenta sintomas moderados de Transtorno do Espectro Autista (TEA) para uma mulher adulta.")
else:
    st.header("Resultado do Diagnóstico")
    if genero == "Masculino" and idade < 18:
        st.write("Com base nas respostas fornecidas e informações do paciente, ele apresenta sintomas graves de Transtorno do Espectro Autista (TEA) para um homem de sua idade.")
    elif genero == "Masculino" and idade >= 18:
        st.write("Com base nas respostas fornecidas e informações do paciente, ele apresenta sintomas graves de Transtorno do Espectro Autista (TEA) para um homem adulto.")
    elif genero == "Feminino" and idade < 18:
        st.write("Com base nas respostas fornecidas e informações do paciente, ela apresenta sintomas graves de Transtorno do Espectro Autista (TEA) para uma mulher de sua idade.")
    else:
        st.write("Com base nas respostas fornecidas e informações do paciente, ela apresenta sintomas graves de Transtorno do Espectro Autista (TEA) para uma mulher adulta.")
