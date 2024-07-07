import streamlit as st

st.title("Questionário de Diagnóstico de Transtorno do Espectro Autista (TEA)")

st.write("Olá! Vamos começar com um questionário de 30 perguntas relacionadas ao TEA. Ao final, você poderá clicar no botão 'Diagnosticar' para obter o resultado.")

st.subheader("Informações Pessoais")

sex = st.radio("Sexo:", ("Masculino", "Feminino"), key="sex")
age = st.slider("Idade:", min_value=1, max_value=60, step=1, key="age")

st.subheader("Questionário")

questions = [
    "-",
    "1. Evita contato visual com outras pessoas?",
    "Exemplo: Evita olhar diretamente para os olhos de outras pessoas durante uma conversa.",
    "-",
    "2. Dificuldade em entender as emoções e expressões faciais dos outros?",
    "Exemplo: Não consegue identificar quando alguém está triste, feliz ou irritado apenas pela expressão facial.",
    "-",
    "3. Dificuldade em iniciar ou manter conversas?",
    "Exemplo: Tem dificuldade em iniciar uma conversa com alguém novo ou em mantê-la por muito tempo.",
    "---",
    "4. Interesses restritos ou obsessivos por determinados temas?",
    "Exemplo: Tem um interesse muito intenso e exclusivo por carros, que domina grande parte do seu tempo e atenção.",
    "---",
    "5. Apresenta comportamentos repetitivos ou ritualizados?",
    "Exemplo: Realiza determinados movimentos ou ações de forma repetitiva, como bater palmas ou balançar o corpo.",
    "---",
    "6. Sensibilidade a determinados sons, texturas ou luzes?",
    "Exemplo: Fica incomodado com o barulho de aspiradores ou secadores de cabelo, evitando ambientes com esses sons.",
    "---",
    "7. Dificuldade em lidar com mudanças na rotina?",
    "Exemplo: Fica muito angustiado quando sua rotina diária é alterada, como mudar o horário de almoço ou a ordem das atividades.",
    "---",
    "8. Dificuldade em entender piadas, metáforas ou sarcasmo?",
    "Exemplo: Não compreende quando alguém faz uma piada ou usa expressões idiomáticas, interpretando-as de forma literal.",
    "---",
    "9. Dificuldade em compreender regras sociais e se adaptar a diferentes contextos?",
    "Exemplo: Tem dificuldade em entender e seguir as regras de etiqueta em diferentes ambientes, como em uma festa ou em uma reunião de trabalho.",
    "---",
    "10. Dificuldade em se colocar no lugar dos outros?",
    "Exemplo: Não consegue imaginar como a outra pessoa está se sentindo em determinada situação, tendo dificuldade em empatizar.",
    "---",
    "11. Dificuldade em expressar suas próprias emoções?",
    "Exemplo: Tem dificuldade em descrever e comunicar seus sentimentos, como felicidade, tristeza ou raiva.",
    "---",
    "12. Dificuldade em entender instruções complexas?",
    "Exemplo: Não consegue seguir instruções detalhadas para a realização de uma tarefa, precisando de orientação passo a passo.",
    "---",
    "13. Dificuldade em se organizar e planejar tarefas?",
    "Exemplo: Tem dificuldade em organizar suas atividades diárias e planejar o que precisa fazer, ficando desorganizado.",
    "---",
    "14. Dificuldade em lidar com situações inesperadas?",
    "Exemplo: Fica muito ansioso e perturbado quando algo inesperado acontece, como um atraso no transporte ou uma mudança de planos.",
    "---",
    "15. Dificuldade em manter a atenção por longos períodos?",
    "Exemplo: Tem dificuldade em se concentrar em uma atividade por muito tempo, ficando facilmente distraído.",
    "---",
    "16. Dificuldade em se adaptar a ambientes barulhentos ou com muitos estímulos?",
    "Exemplo: Fica muito incomodado e estressado em ambientes com muitos sons, luzes e pessoas, como shoppings ou festas.",
    "---",
    "17. Dificuldade em entender expressões faciais e linguagem corporal?",
    "Exemplo: Não consegue interpretar corretamente os gestos e a linguagem corporal das pessoas, tendo dificuldade em entender o que elas querem comunicar.",
    "---",
    "18. Dificuldade em fazer amizades e manter relacionamentos?",
    "Exemplo: Tem dificuldade em iniciar e manter amizades, preferindo ficar sozinho a interagir com outras pessoas.",
    "---",
    "19. Dificuldade em entender e seguir regras sociais?",
    "Exemplo: Não compreende e não segue as regras de etiqueta e comportamento social, como esperar a sua vez para falar ou respeitar o espaço pessoal dos outros.",
    "---",
    "20. Dificuldade em lidar com mudanças de rotina ou transições?",
    "Exemplo: Fica muito angustiado e perturbado quando sua rotina diária é alterada, como mudar de atividade ou de ambiente.",
    "---",
    "21. Dificuldade em entender instruções verbais complexas?",
    "Exemplo: Não consegue seguir instruções verbais detalhadas, precisando de orientação visual ou escrita para entender o que deve fazer.",
    "---",
    "22. Dificuldade em se concentrar em tarefas que não lhe interessam?",
    "Exemplo: Tem dificuldade em se concentrar em atividades que não lhe atraem, como tarefas escolares ou de trabalho que não são do seu interesse.",
    "---",
    "23. Dificuldade em entender piadas, metáforas ou sarcasmo?",
    "Exemplo: Não compreende quando alguém usa expressões idiomáticas ou faz piadas, interpretando-as de forma literal.",
    "---",
    "24. Dificuldade em se adaptar a ambientes com muitas pessoas?",
    "Exemplo: Fica muito ansioso e estressado em ambientes com muita gente, como festas ou eventos sociais, evitando-os.",
    "---",
    "25. Dificuldade em entender e responder a perguntas?",
    "Exemplo: Tem dificuldade em entender o que lhe está sendo perguntado e em formular uma resposta adequada.",
    "---",
    "26. Dificuldade em lidar com situações sociais desconhecidas?",
    "Exemplo: Fica muito nervoso e desconfortável em situações sociais novas, como conhecer pessoas pela primeira vez.",
    "---",
    "27. Dificuldade em entender e seguir regras sociais implícitas?",
    "Exemplo: Não compreende as regras sociais não ditas, como saber quando é apropriado interromper uma conversa ou quando deve esperar sua vez de falar.",
    "---",
    "28. Dificuldade em lidar com mudanças inesperadas na rotina?",
    "Exemplo: Fica muito perturbado e angustiado quando sua rotina diária é alterada de forma inesperada, como um atraso no transporte ou uma atividade extra.",
    "---",
    "29. Dificuldade em entender e interpretar as emoções dos outros?",
    "Exemplo: Não consegue perceber e compreender os sentimentos das pessoas apenas observando suas expressões faciais e linguagem corporal.",
    "---",
    "30. Dificuldade em se comunicar de forma efetiva?",
    "Exemplo: Tem dificuldade em se expressar claramente, seja verbalmente ou por meio de gestos, prejudicando sua capacidade de se comunicar com os outros.",
    "---",
]

answers = []
for i, question in enumerate(questions):
    if i % 2 == 0:
        answer = st.radio(questions[i], ("Não", "Pouco", "Muito"), key=f"question_{i}")
        answers.append(answer)
        st.write(questions[i+1])
        st.write("---")

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
