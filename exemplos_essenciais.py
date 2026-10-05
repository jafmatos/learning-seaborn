"""
Script prático: Os 20% do Seaborn que resolvem 80% dos problemas em Ciência de Dados.
Gera os gráficos essenciais e salva na pasta 'outputs/' para estudo e validação.
"""

from pathlib import Path
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Configurar diretório de saída
output_dir = Path(__file__).parent / "outputs"
output_dir.mkdir(exist_ok=True)

# 2. Configurar tema profissional corporativo (clean, legível)
sns.set_theme(
    style="whitegrid",
    font_scale=1.1,
    rc={"axes.edgecolor": ".8", "grid.color": ".9"}
)

print("Carregando datasets de exemplo ('penguins' e 'tips')...")
penguins = sns.load_dataset("penguins")
tips = sns.load_dataset("tips")

# ---------------------------------------------------------
# 1. Histograma com Curva KDE (Distribuição Univariada)
# ---------------------------------------------------------
print("1. Gerando histplot com KDE...")
plt.figure(figsize=(8, 4.5))
sns.histplot(
    data=penguins,
    x="body_mass_g",
    kde=True,
    hue="species",
    bins=25,
    alpha=0.6
)
plt.title("Distribuição da Massa Corporal por Espécie de Pinguim", pad=15, fontweight="bold")
plt.xlabel("Massa Corporal (g)")
plt.ylabel("Contagem de Indivíduos")
sns.despine()
plt.savefig(output_dir / "01_histplot_distribuicao.png", dpi=300, bbox_inches="tight")
plt.close()

# ---------------------------------------------------------
# 2. Scatterplot Multivariado (Relação e Dispersão)
# ---------------------------------------------------------
print("2. Gerando scatterplot multivariado...")
plt.figure(figsize=(8, 5))
sns.scatterplot(
    data=tips,
    x="total_bill",
    y="tip",
    hue="time",
    style="smoker",
    size="size",
    sizes=(40, 200),
    alpha=0.8
)
plt.title("Relação entre Valor da Conta e Gorjeta por Horário e Ocupação", pad=15, fontweight="bold")
plt.xlabel("Total da Conta ($)")
plt.ylabel("Gorjeta ($)")
sns.despine()
plt.savefig(output_dir / "02_scatterplot_relacao.png", dpi=300, bbox_inches="tight")
plt.close()

# ---------------------------------------------------------
# 3. Boxplot & Comparação Estatística
# ---------------------------------------------------------
print("3. Gerando boxplot...")
plt.figure(figsize=(8, 4.5))
sns.boxplot(
    data=tips,
    x="day",
    y="total_bill",
    hue="sex",
    palette="Set2"
)
plt.title("Distribuição de Contas por Dia da Semana e Sexo do Cliente", pad=15, fontweight="bold")
plt.xlabel("Dia da Semana")
plt.ylabel("Total da Conta ($)")
sns.despine()
plt.savefig(output_dir / "03_boxplot_outliers.png", dpi=300, bbox_inches="tight")
plt.close()

# ---------------------------------------------------------
# 4. Barplot com Métricas Agregadas
# ---------------------------------------------------------
print("4. Gerando barplot...")
plt.figure(figsize=(8, 4.5))
sns.barplot(
    data=tips,
    x="day",
    y="tip",
    hue="day",
    legend=False,
    order=["Thur", "Fri", "Sat", "Sun"],
    palette="Blues_d",
    estimator="mean",    # Padrão é média. Outros: "median" (para outliers/assimetrias), "sum", etc.
    errorbar=("ci", 95)  # Intervalo de Confiança 95%. Use 'sd' (desvio padrão) ou None (sem barra)
)
plt.title("Média da Gorjeta por Dia da Semana (com IC 95%)", pad=15, fontweight="bold")
plt.xlabel("Dia da Semana")
plt.ylabel("Gorjeta Média ($)")
sns.despine()
plt.savefig(output_dir / "04_barplot_medias.png", dpi=300, bbox_inches="tight")
plt.close()

# ---------------------------------------------------------
# 5. Matriz de Correlação com Heatmap
# ---------------------------------------------------------
print("5. Gerando heatmap de correlação...")
plt.figure(figsize=(7, 5))
numeric_penguins = penguins.select_dtypes(include="number")
corr = numeric_penguins.corr()

sns.heatmap(
    corr,
    annot=True,
    fmt=".2f",
    cmap="coolwarm",
    vmin=-1,
    vmax=1,
    linewidths=0.8,
    cbar_kws={"label": "Correlação de Pearson"}
)
plt.title("Matriz de Correlação das Métricas Biométricas", pad=15, fontweight="bold")
plt.savefig(output_dir / "05_heatmap_correlacao.png", dpi=300, bbox_inches="tight")
plt.close()

# ---------------------------------------------------------
# 6. Pairplot (Raio-X de Features)
# ---------------------------------------------------------
print("6. Gerando pairplot (visão global)...")
g = sns.pairplot(
    data=penguins.dropna(),
    hue="species",
    corner=True,
    palette="Dark2"
)
g.figure.suptitle("Matriz de Dispersão Geral (Pairplot de Features)", y=1.02, fontweight="bold")
g.savefig(output_dir / "06_pairplot_screening.png", dpi=200, bbox_inches="tight")
plt.close()

print(f"\n✅ Concluído com sucesso! Gráficos gerados e salvos em: {output_dir}")
