import pandas as pd;

df = pd.read_csv('vgsales.csv')
linha_0 = df.iloc[0]
frase = f"Rank: {linha_0['Rank']}, Name: {linha_0['Name']}, Platform: {linha_0['Platform']}, Year: {linha_0['Year']}, Genre: {linha_0['Genre']}, Publisher: {linha_0['Publisher']}, NA Sales: {linha_0['NA_Sales']}, EU Sales: {linha_0['EU_Sales']}, JP Sales: {linha_0['JP_Sales']}, Other Sales: {linha_0['Other_Sales']}, Global Sales: {linha_0['Global_Sales']}"
print(frase)

jogos_por_plataforma = df.groupby('Platform')
jogos_wii = jogos_por_plataforma.get_group('Wii')

print(f'jogos da plataforma wii{jogos_wii}')
# Conta quantos jogos existem por plataforma
contagem_plataformas = df['Platform'].value_counts()

# Filtra as plataformas que têm mais de um jogo
plataformas_com_mais_de_um_jogo = contagem_plataformas[contagem_plataformas > 1]

print("Plataformas com mais de um jogo:")
print(plataformas_com_mais_de_um_jogo)

# Para cada plataforma que tem mais de um jogo, exibe os jogos
for plataforma in plataformas_com_mais_de_um_jogo.index:
    jogos_plataforma = jogos_por_plataforma.get_group(plataforma)
    print(f"\nJogos da plataforma {plataforma}:")
    print(jogos_plataforma)
