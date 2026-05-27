# =============================================================
# MISSION CONTROL AI
# Sistema Inteligente de Monitoramento de Missão Espacial
# GS2026.1 - Pensamento Computacional e Automação com Python
# =============================================================

nome_missao = "Projeto Brazil-space monitoring"
nome_equipe  = "Equipe Star Brazil"

areas_monitoradas = [
    "Temperatura interna",
    "Comunicação com a base",
    "Sistema de energia",
    "Suporte de oxigênio",
    "Estabilidade operacional"
]

# Cada linha: [temperatura, comunicacao, bateria, oxigenio, estabilidade]
# Narrativa:
# Ciclo 1 - início estável, todos sistemas normais
# Ciclo 2 - queda de comunicação e bateria, sinais de instabilidade
# Ciclo 3 - temperatura começa a subir, oxigênio cai levemente
# Ciclo 4 - temperatura crítica, bateria em atenção
# Ciclo 5 - colapso de comunicação e energia
# Ciclo 6 - tentativa de recuperação parcial, mas sistemas ainda comprometidos
dados_missao = [
    [23, 91, 85, 97, 93],   # Ciclo 1 - início da missão, tudo estável
    [27, 52, 44, 94, 76],   # Ciclo 2 - queda de comunicação e bateria
    [33, 61, 41, 86, 66],   # Ciclo 3 - temperatura sobe, oxigênio cai
    [37, 45, 36, 82, 54],   # Ciclo 4 - temperatura crítica, sistemas fragilizados
    [41, 26, 18, 75, 38],   # Ciclo 5 - comunicação crítica, bateria crítica
    [35, 49, 31, 84, 57]    # Ciclo 6 - tentativa de recuperação parcial
]


# -------------------------------------------------------------
# FUNÇÕES DE ANÁLISE POR ÁREA
# -------------------------------------------------------------

def analisar_temperatura(valor):
    """Classifica a temperatura e retorna (status, descricao, pontos)."""
    if valor < 18:
        return "ATENÇÃO", "Temperatura abaixo do ideal", 1
    elif valor <= 30:
        return "NORMAL", "Temperatura estável", 0
    elif valor <= 35:
        return "ATENÇÃO", "Temperatura elevada", 1
    else:
        return "CRÍTICO", "Risco de superaquecimento", 2


def analisar_comunicacao(valor):
    """Classifica a comunicação e retorna (status, descricao, pontos)."""
    if valor < 30:
        return "CRÍTICO", "Comunicação com a base em nível crítico", 2
    elif valor < 60:
        return "ATENÇÃO", "Comunicação instável", 1
    else:
        return "NORMAL", "Comunicação estável", 0


def analisar_bateria(valor):
    """Classifica a bateria e retorna (status, descricao, pontos)."""
    if valor < 20:
        return "CRÍTICO", "Bateria em nível crítico", 2
    elif valor < 50:
        return "ATENÇÃO", "Bateria abaixo do recomendado", 1
    else:
        return "NORMAL", "Energia estável", 0


def analisar_oxigenio(valor):
    """Classifica o oxigênio e retorna (status, descricao, pontos)."""
    if valor < 80:
        return "CRÍTICO", "Oxigênio em nível crítico", 2
    elif valor < 90:
        return "ATENÇÃO", "Oxigênio abaixo do ideal", 1
    else:
        return "NORMAL", "Oxigênio adequado", 0


def analisar_estabilidade(valor):
    """Classifica a estabilidade e retorna (status, descricao, pontos)."""
    if valor < 40:
        return "CRÍTICO", "Estabilidade operacional crítica", 2
    elif valor < 70:
        return "ATENÇÃO", "Estabilidade operacional reduzida", 1
    else:
        return "NORMAL", "Estabilidade operacional adequada", 0


# -------------------------------------------------------------
# CLASSIFICAÇÃO DO CICLO
# -------------------------------------------------------------

def classificar_ciclo(pontuacao):
    """Retorna a classificação textual do ciclo com base na pontuação."""
    if pontuacao <= 2:
        return "MISSÃO ESTÁVEL"
    elif pontuacao <= 5:
        return "MISSÃO EM ATENÇÃO"
    else:
        return "MISSÃO CRÍTICA"


# -------------------------------------------------------------
# ANÁLISE DE TENDÊNCIA
# -------------------------------------------------------------

def analisar_tendencia(risco_primeiro, risco_ultimo):
    """Compara o risco do primeiro e do último ciclo e retorna a tendência."""
    if risco_ultimo > risco_primeiro:
        return "A missão apresentou tendência de piora."
    elif risco_ultimo < risco_primeiro:
        return "A missão apresentou tendência de melhora."
    else:
        return "A missão permaneceu estável em relação ao início."


# -------------------------------------------------------------
# IDENTIFICAÇÃO DA ÁREA MAIS AFETADA
# -------------------------------------------------------------

def identificar_area_mais_afetada(pontos_por_area):
    """Retorna o nome da área com maior pontuação acumulada de risco."""
    maior_pontuacao = -1
    area_mais_afetada = ""
    for i in range(len(pontos_por_area)):
        if pontos_por_area[i] > maior_pontuacao:
            maior_pontuacao = pontos_por_area[i]
            area_mais_afetada = areas_monitoradas[i]
    return area_mais_afetada


# -------------------------------------------------------------
# RECOMENDAÇÃO AUTOMÁTICA
# -------------------------------------------------------------

def gerar_recomendacao(status_temp, status_com, status_bat, status_ox, status_est):
    """Gera uma recomendação com base nos status críticos do ciclo."""
    recomendacoes = []

    if status_temp == "CRÍTICO":
        recomendacoes.append("verificar controle térmico da missão")
    if status_com == "CRÍTICO":
        recomendacoes.append("tentar restabelecer contato com a base")
    if status_bat == "CRÍTICO":
        recomendacoes.append("ativar modo de economia de energia")
    if status_ox == "CRÍTICO":
        recomendacoes.append("acionar protocolo de suporte à vida")
    if status_est == "CRÍTICO":
        recomendacoes.append("reduzir operações não essenciais")

    if not recomendacoes:
        atencoes = [s for s in [status_temp, status_com, status_bat, status_ox, status_est] if s == "ATENÇÃO"]
        if atencoes:
            return "Monitorar sistemas em atenção e preparar plano de contingência."
        else:
            return "Manter operação normal e continuar monitoramento."

    if len(recomendacoes) >= 3:
        return "Ativar modo de segurança e priorizar suporte à vida, energia e comunicação."

    return "Recomenda-se: " + "; ".join(recomendacoes) + "."


# -------------------------------------------------------------
# RELATÓRIO FINAL
# -------------------------------------------------------------

def gerar_relatorio_final(riscos_por_ciclo, pontos_por_area, tendencia, classificacao_final):
    """Exibe o relatório consolidado da missão."""
    num_ciclos = len(dados_missao)

    soma_temp = soma_com = soma_bat = soma_ox = soma_est = 0
    for ciclo in dados_missao:
        soma_temp += ciclo[0]
        soma_com  += ciclo[1]
        soma_bat  += ciclo[2]
        soma_ox   += ciclo[3]
        soma_est  += ciclo[4]

    media_temp = soma_temp / num_ciclos
    media_com  = soma_com  / num_ciclos
    media_bat  = soma_bat  / num_ciclos
    media_ox   = soma_ox   / num_ciclos
    media_est  = soma_est  / num_ciclos

    maior_risco   = max(riscos_por_ciclo)
    ciclo_critico = riscos_por_ciclo.index(maior_risco) + 1
    risco_medio   = sum(riscos_por_ciclo) / num_ciclos
    qtd_criticos  = sum(1 for r in riscos_por_ciclo if r >= 6)
    area_afetada  = identificar_area_mais_afetada(pontos_por_area)

    if classificacao_final == "MISSÃO CRÍTICA":
        conclusao = ("A missão entrou em colapso operacional nos ciclos finais. "
                     "Intervenção imediata é necessária para preservar a integridade da tripulação e dos sistemas.")
    elif classificacao_final == "MISSÃO EM ATENÇÃO":
        conclusao = ("A missão apresentou instabilidade relevante durante a operação. "
                     "Os sistemas mais críticos precisam de atenção contínua e o plano de contingência "
                     "deve permanecer ativo.")
    else:
        conclusao = ("A missão transcorreu de forma estável. "
                     "Todos os sistemas operaram dentro dos parâmetros normais.")

    print("=" * 60)
    print("RELATÓRIO FINAL DA MISSÃO")
    print("=" * 60)
    print(f"Missão: {nome_missao}")
    print(f"Equipe: {nome_equipe}")
    print()
    print(f"Quantidade de ciclos analisados: {num_ciclos}")
    print()
    print(f"Média de temperatura:   {media_temp:.2f} °C")
    print(f"Média de comunicação:   {media_com:.2f}%")
    print(f"Média de bateria:       {media_bat:.2f}%")
    print(f"Média de oxigênio:      {media_ox:.2f}%")
    print(f"Média de estabilidade:  {media_est:.2f}%")
    print()
    print(f"Ciclo mais crítico:            Ciclo {ciclo_critico}")
    print(f"Maior pontuação de risco:      {maior_risco}")
    print(f"Risco médio da missão:         {risco_medio:.2f}")
    print(f"Quantidade de ciclos críticos: {qtd_criticos}")
    print()
    print("Tendência da missão:")
    print(tendencia)
    print()
    print("Pontuação acumulada por área:")
    for i in range(len(areas_monitoradas)):
        print(f"  {areas_monitoradas[i]}: {pontos_por_area[i]} pontos")
    print()
    print("Área mais afetada:")
    print(f"  {area_afetada}")
    print()
    print("Classificação final da missão:")
    print(f"  {classificacao_final}")
    print()
    print("Conclusão:")
    print(conclusao)


# -------------------------------------------------------------
# PROGRAMA PRINCIPAL
# -------------------------------------------------------------

print("=" * 60)
print("MISSION CONTROL AI")
print("=" * 60)
print(f"Missão: {nome_missao}")
print(f"Equipe: {nome_equipe}")
print(f"Quantidade de ciclos analisados: {len(dados_missao)}")
print("=" * 60)

riscos_por_ciclo = []
pontos_por_area  = [0, 0, 0, 0, 0]

for i in range(len(dados_missao)):
    ciclo = dados_missao[i]
    numero_ciclo = i + 1

    temperatura  = ciclo[0]
    comunicacao  = ciclo[1]
    bateria      = ciclo[2]
    oxigenio     = ciclo[3]
    estabilidade = ciclo[4]

    st_temp, desc_temp, pts_temp = analisar_temperatura(temperatura)
    st_com,  desc_com,  pts_com  = analisar_comunicacao(comunicacao)
    st_bat,  desc_bat,  pts_bat  = analisar_bateria(bateria)
    st_ox,   desc_ox,   pts_ox   = analisar_oxigenio(oxigenio)
    st_est,  desc_est,  pts_est  = analisar_estabilidade(estabilidade)

    pontuacao_ciclo = pts_temp + pts_com + pts_bat + pts_ox + pts_est
    classificacao   = classificar_ciclo(pontuacao_ciclo)
    recomendacao    = gerar_recomendacao(st_temp, st_com, st_bat, st_ox, st_est)

    riscos_por_ciclo.append(pontuacao_ciclo)
    pontos_por_area[0] += pts_temp
    pontos_por_area[1] += pts_com
    pontos_por_area[2] += pts_bat
    pontos_por_area[3] += pts_ox
    pontos_por_area[4] += pts_est

    print(f"\nCICLO {numero_ciclo}")
    print("-" * 60)
    print(f"Temperatura:  {temperatura} °C | {st_temp} | {desc_temp}")
    print(f"Comunicação:  {comunicacao}%   | {st_com} | {desc_com}")
    print(f"Bateria:      {bateria}%       | {st_bat} | {desc_bat}")
    print(f"Oxigênio:     {oxigenio}%      | {st_ox} | {desc_ox}")
    print(f"Estabilidade: {estabilidade}%  | {st_est} | {desc_est}")
    print()
    print(f"Pontuação de risco do ciclo: {pontuacao_ciclo}")
    print(f"Classificação do ciclo: {classificacao}")
    print(f"Recomendação: {recomendacao}")

print()

tendencia = analisar_tendencia(riscos_por_ciclo[0], riscos_por_ciclo[-1])

risco_medio_final   = sum(riscos_por_ciclo) / len(riscos_por_ciclo)
classificacao_final = classificar_ciclo(round(risco_medio_final))

print()
gerar_relatorio_final(riscos_por_ciclo, pontos_por_area, tendencia, classificacao_final)
