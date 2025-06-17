Calculadora de Esforços em Postes de Redes de Distribuição
📖 Sobre o Projeto
Esta é uma ferramenta web desenvolvida em Python com Streamlit para automatizar o cálculo de esforços mecânicos em postes de redes de distribuição aérea. O aplicativo calcula a força resultante a partir de múltiplas direções de esforço, considerando diferentes tipos de cabos (Média Tensão Compacta, Baixa Tensão Secundária e Iluminação Pública) e, ao final, recomenda o poste mais adequado com base em normas técnicas e regras de projeto.

O objetivo principal é agilizar o processo de dimensionamento de postes, reduzir a probabilidade de erros manuais e gerar relatórios e visualizações consistentes para projetos de engenharia elétrica.

✨ Funcionalidades
Cálculo em Lote: Permite calcular múltiplos postes em uma única sessão.

Identificação Personalizada: Cada poste pode ser nomeado com um identificador de projeto (ex: "P-01", "E-102").

Cálculo Direcional Composto: Calcula o esforço total para cada direção, somando as contribuições dos cabos de Média Tensão, Baixa Tensão e Iluminação Pública.

Lógica de Vão Inteligente: Se um vão inserido pelo usuário não existir na base de dados, a ferramenta utiliza automaticamente o próximo vão superior disponível para garantir um dimensionamento seguro.

Recomendação Automática de Poste: Sugere o poste mais econômico que atende às exigências de esforço e altura, seguindo regras de negócio como:

Altura mínima de 12m se houver rede compacta.

Altura mínima de 9m se não houver rede compacta.

Esforço nominal mínimo de 400 daN.

Exportação de Relatórios: Gera um arquivo .xlsx (Excel) com o resumo detalhado de todos os postes calculados.

Visualização Gráfica: Para cada poste, salva um diagrama de vetores (.png) que mostra visualmente cada força direcional e a resultante final.

🚀 Como Usar a Ferramenta
1. Acessando o Aplicativo Online
A maneira mais fácil de usar é através do link do aplicativo publicado no Streamlit Community Cloud. (Insira aqui o link do seu app depois de publicá-lo).

2. Executando Localmente
Se preferir rodar o aplicativo no seu próprio computador:

Pré-requisitos:

Python 3.8+ instalado.

As bibliotecas listadas no arquivo requirements.txt.

Passos:

a. Clone este repositório para a sua máquina:

git clone https://github.com/seu-usuario/calculadora-postes.git

b. Navegue até a pasta do projeto e instale as dependências:

cd calculadora-postes
pip install -r requirements.txt

c. Execute o aplicativo:

streamlit run app.py

O aplicativo será aberto automaticamente no seu navegador padrão.

🛠️ Tecnologias Utilizadas
Python: Linguagem principal do projeto.

Streamlit: Framework para a criação da interface web interativa.

Pandas: Para manipulação de dados e criação do relatório em Excel.

NumPy: Para os cálculos matemáticos e vetoriais.

Matplotlib: Para a geração e salvamento dos gráficos de vetores.

⚠️ Aviso Legal
Esta ferramenta foi desenvolvida como um auxílio para projetos de engenharia elétrica, baseada nos dados e normas fornecidas. Os resultados devem ser sempre verificados e validados por um profissional qualificado e legalmente habilitado antes de serem aplicados em um projeto real. O autor não se responsabiliza pelo uso indevido das informações geradas.
