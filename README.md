# Aprendizado-em-Python 

Repositório para incluir meus aprendizados em python. 

Projetos variados como Python, Computação Cietífica com Python, Machine Learning e Análise de Dados.

1º Projeto Cifra de César.

A Cifra de César é um dos métodos de criptografia mais antigos e simples. Ela foi usada por Júlio César para proteger mensagens secretas. A ideia básica é substituir cada letra do texto original por outra letra que está um número fixo de posições à frente no alfabeto. Esse número fixo é chamado de deslocamento (ou shift).

Como Funciona:
Deslocamento: Cada letra do texto é "deslocada" por um número fixo de posições no alfabeto.
Por exemplo, com um deslocamento de 3:
A letra A se torna D.
A letra B se torna E.
A letra Z se torna C (o alfabeto "volta" ao início após o Z).
Descriptografia: Para descriptografar, basta aplicar o deslocamento no sentido inverso.
Características:
É uma cifra de substituição, onde cada letra é substituída por outra.
Simples de implementar, mas não é segura para criptografia moderna, pois pode ser facilmente quebrada com análise de frequência.


Texto Original e Deslocamento:
O texto a ser criptografado é 'Hello World'.
O deslocamento (shift) é definido como 3.
Alfabeto:
O alfabeto usado é 'abcdefghijklmnopqrstuvwxyz'. O código só criptografa letras minúsculas.

Processamento de Cada Caractere:
O código percorre cada caractere do texto original.
Se o caractere for um espaço, ele é adicionado ao texto criptografado sem alteração.

Se o caractere for uma letra do alfabeto, o código:
Encontra a posição da letra no alfabeto.
Aplica o deslocamento para encontrar a nova letra.
Usa o operador % para garantir que, se o deslocamento ultrapassar o final do alfabeto, ele "volte" ao início.
Se o caractere não for uma letra (como números ou pontuações), ele é adicionado ao texto criptografado sem alteração.
Resultado Final:
O texto criptografado é armazenado na variável encrypted_text.
Para 'Hello World' e um deslocamento de 3, o resultado é 'khoor zruog'.

---------------------------

2º Projeto Ressonância MLP

Este projeto utiliza redes neurais artificiais (MLP – Multi-Layer Perceptron) para prever valores contínuos a partir de dados de entrada. O objetivo é testar diferentes configurações de neurônios e funções de ativação, avaliando qual modelo apresenta melhor desempenho.

Como Funciona:

Carregamento dos dados: Os datasets de treino e teste são lidos do Google Drive (ou enviados manualmente).

Separação em variáveis: As colunas x1, x2, x3 são usadas como entradas (features) e a coluna d como saída (target).

Configuração dos modelos: São definidos hiperparâmetros fixos (taxa de aprendizado, número de épocas) e diferentes combinações de neurônios e funções de ativação (tanh, relu, logistic).

Treinamento: Cada configuração é treinada com o MLPRegressor da biblioteca scikit-learn.

Avaliação: O código calcula métricas como MAE, MSE, RMSE, MAPE e R² para medir a qualidade das previsões.

Visualizações: São gerados gráficos da curva de perda, comparação entre valores reais e previstos, e dispersão dos resultados.

Seleção do melhor modelo: O modelo com menor perda final é escolhido como o mais adequado para os dados.

Características:

Permite comparar diferentes arquiteturas de rede neural.

Usa métricas estatísticas para validar o desempenho.

Inclui gráficos para análise visual dos resultados.

É um exemplo prático de aplicação de Machine Learning com Python em regressão.

Resultado Final:  
O código identifica automaticamente a melhor configuração de rede neural para os dados fornecidos, mostrando métricas de desempenho e gráficos que ajudam a entender como o modelo se comporta em relação aos valores reais.
