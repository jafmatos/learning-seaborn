# 📊 02_Aprendendo_Seaborn

Repositório estruturado para o domínio prático do **Seaborn** na Ciência de Dados, focado na filosofia **80/20 (Princípio de Pareto)** — dominando os 20% das ferramentas e conceitos que resolvem 80% dos problemas reais de Análise Exploratória de Dados (EDA) e comunicação de insights.

Este projeto faz parte da preparação para processos seletivos e desafios técnicos em consultorias de dados e inteligência artificial (como a **Sauter Digital**).

---

## 🚀 Como Executar o Projeto

Este projeto utiliza o gerenciador de pacotes ultra-rápido [`uv`](https://github.com/astral-sh/uv).

### 1. Ativar o Ambiente Virtual
```bash
source .venv/bin/activate
```

### 2. Executar o Script de Demonstração
Gera os 6 gráficos essenciais em alta resolução na pasta `outputs/`:
```bash
python exemplos_essenciais.py
```

---

## 📚 Documentação Completa

O guia completo com teoria, arquitetura, visualizações essenciais, boas práticas de storytelling e dicas para entrevistas técnicas está disponível em:

👉 **[seaborn_guide.md](file:///home/jos/Desktop/Ci%C3%AAncia%20de%20Dados/02_Aprendendo_Seaborn/seaborn_guide.md)**

---

## 📂 Estrutura do Projeto

```text
02_Aprendendo_Seaborn/
├── seaborn_guide.md           # Guia definitivo: teoria, matriz de decisão, código e interpretação
├── README.md                  # Apresentação do projeto e instruções
├── pyproject.toml             # Dependências gerenciadas via uv
├── uv.lock                    # Lockfile de dependências
├── exemplos_essenciais.py     # Script Python executável com os 6 gráficos-chave
└── outputs/                   # Gráficos de alta resolução gerados (300 DPI)
    ├── 01_histplot_distribuicao.png
    ├── 02_scatterplot_relacao.png
    ├── 03_boxplot_outliers.png
    ├── 04_barplot_medias.png
    ├── 05_heatmap_correlacao.png
    └── 06_pairplot_screening.png
```

---

## 🎯 Os 6 Gráficos Essenciais (Resumo Rápido)

1. **`sns.histplot(kde=True)`**: Distribuições contínuas, assimetria (skewness), caudas longas e bimodalidade.
2. **`sns.scatterplot(x, y, hue, style, size)`**: Relação multivariada, linearidade, dispersão em funil (heterocedasticidade) e clusters.
3. **`sns.boxplot(x, y, hue)`**: Comparação de medianas, dispersão (IQR) e detecção de anomalias/outliers.
4. **`sns.barplot(x, y, hue)`**: Comparação de métricas agregadas (médias) com intervalo de confiança (95%) para avaliar significância estatística.
5. **`sns.heatmap(df.corr(), annot=True)`**: Matriz de correlação de Pearson para diagnóstico de multicolinearidade em Machine Learning.
6. **`sns.pairplot(df, hue, corner=True)`**: Diagnóstico exploratório inicial de separabilidade entre classes.

---

## 💡 O Diferencial para Consultorias (Sauter Digital)

No **[seaborn_guide.md](file:///home/jos/Desktop/Ci%C3%AAncia%20de%20Dados/02_Aprendendo_Seaborn/seaborn_guide.md)**, você encontra:
* **Bases de Dados Nativas:** Como listar (`sns.get_dataset_names()`) e carregar (`sns.load_dataset()`) dados reais de treino em segundos.
* **Matriz de Decisão e Árvore de Escolha:** Como saber instantaneamente qual gráfico usar conforme o tipo e quantidade de variáveis (Numérica Contínua, Discreta, Categórica, Temporal).
* **Anatomia Visual Exata:** O que cada linha, barra ou caixa representa matematicamente.
* **Diagnóstico Estatístico:** O que a forma dos dados está revelando (assimetria, bimodalidade, heterocedasticidade, outliers).
* **Decisão Prática de Modelagem:** Transformação logarítmica, tratamento de outliers e descarte de multicolinearidade.
* **Data Storytelling Corporativo:** O framework de 4 passos para apresentar descobertas para clientes e líderes técnicos.

