🚀 Rota Inteligente: Otimização de Entregas com Algoritmos de IA
🧠 Desafio

A empresa Sabor Express, especializada em delivery de alimentos na região central da cidade, enfrenta dificuldades para gerenciar suas entregas durante horários de pico.
As rotas são atualmente definidas de forma manual, baseadas na experiência dos entregadores, o que causa atrasos, aumento de custos de combustível e insatisfação dos clientes.

O desafio é desenvolver uma solução inteligente baseada em IA capaz de sugerir as melhores rotas de entrega, considerando a cidade como um grafo — onde os pontos representam bairros/localidades e as arestas representam as ruas, com pesos baseados em distância ou tempo estimado.

Além disso, deve-se aplicar clustering (K-Means) para agrupar entregas próximas, otimizando o trabalho dos entregadores.

🎯 Objetivo

Implementar uma solução de otimização de rotas que:

Utilize algoritmos de busca (A*, BFS, DFS) para encontrar o menor caminho entre os pontos de entrega;

Empregue K-Means para agrupar pedidos próximos;

Gere relatórios e visualizações sobre a eficiência das rotas;

Reduza custos e aumente a eficiência operacional da empresa.

🧩 Abordagem Adotada

Modelagem do problema como grafo:

Cada ponto de entrega é um nó;

As ruas são as arestas com pesos baseados em distância.

Algoritmos utilizados:

A* (A-star): busca heurística para encontrar o menor caminho;

BFS (Busca em Largura) e DFS (Busca em Profundidade): comparação de desempenho e eficiência;

K-Means: agrupamento de entregas por proximidade.

Etapas do projeto:

Criação do grafo e mapeamento dos pontos;

Implementação dos algoritmos de busca;

Agrupamento das entregas com K-Means;

Visualização dos resultados e comparação de desempenho.

📊 Resultados Obtidos

As rotas otimizadas pelo A* reduziram a distância média percorrida em comparação à busca cega (BFS/DFS).

O agrupamento com K-Means permitiu dividir as entregas em zonas otimizadas, reduzindo o tempo médio de entrega.

O sistema demonstra ganho de eficiência operacional e menor custo de combustível.

📈 Limitações: o modelo não considera variações de tráfego em tempo real.
💡 Sugestão de melhoria: integração com APIs de mapas e tráfego (ex: Google Maps API) para rotas dinâmicas.

🗂 Estrutura de Pastas
rota-inteligente/
├── README.md
├── LICENSE
├── data/
│   ├── nodes.csv          # Pontos do grafo (nós)
│   ├── edges.csv          # Ligações entre os pontos
├── src/
│   ├── main.py            # Código principal da solução
│   ├── algorithms/
│   │   ├── a_star.py
│   │   ├── bfs.py
│   │   ├── dfs.py
│   │   └── kmeans.py
├── docs/
│   ├── grafo_diagrama.png # Diagrama ilustrativo do grafo
│   ├── resultados.png     # Visualizações e outputs
├── notebooks/
│   └── rota_inteligente.ipynb  # Notebook com execução no Colab
└── rota_inteligente_outputs/
    ├── cluster_resultados.csv
    └── rotas_otimizadas.png

⚙️ Como Executar
▶️ No Google Colab

Acesse o notebook no link abaixo:
👉 Abrir no Colab

Execute as células em sequência.

Verifique as saídas geradas na pasta rota_inteligente_outputs.

💻 Localmente

Clone o repositório:

git clone https://github.com/Mariana-Lambiasi/rota-inteligente.git
cd rota-inteligente


Instale as dependências:

pip install -r requirements.txt


Execute o projeto:

python src/main.py

📘 Fontes de Pesquisa

UPS – ORION System: otimização de rotas com IA.

Medium – Optimizing Logistics: aplicação de K-Means e heurísticas.

ResearchGate – AI-Powered Route Optimization: integração de IA e sensores IoT.

Kardinal.ai Case Study: entrega de alimentos com otimização contínua de rotas.

🎥 Vídeo Pitch (4 minutos)

📺 [Inserir aqui o link do vídeo no YouTube]
Explique brevemente:

O problema resolvido

A lógica da solução

Demonstração do código e dos resultados

🤝 Como Contribuir

Faça um fork do projeto.

Crie uma nova branch:

git checkout -b feature/sua-feature


Faça commit das alterações:

git commit -m "Descrição da mudança"


Envie para o repositório remoto:

git push origin feature/sua-feature


Abra um Pull Request.

📬 Contato

👩‍💻 Mariana Lambiasi de Carvalho
📧 mariana.carvalho.80804@a.fecaf.com.br
