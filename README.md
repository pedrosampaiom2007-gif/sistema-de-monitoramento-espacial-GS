## README.md

```markdown
# Mission Control AI — Projeto Brazil-space monitoring

Sistema inteligente de monitoramento de missão espacial desenvolvido em Python.
Projeto da Global Solution 2026.1 — Pensamento Computacional e Automação com Python — FIAP.

---

## Equipe Star Brazil

| Nome | RM |
|---|---|
| Luan de Araujo Carneiro | 573691 |
| Pedro Sampaio Mochnacs Arruda | 573522 |
| Raul Sampaio Mochnacs Arruda | 573523 |

---

## Sobre o projeto

O **Mission Control AI** simula o monitoramento inteligente de uma missão espacial experimental chamada **Projeto Brazil-space monitoring**.

O sistema analisa 6 ciclos de monitoramento, cada um contendo 5 parâmetros críticos da missão:

- Temperatura interna do módulo (°C)
- Qualidade do sinal de comunicação (%)
- Nível de bateria (%)
- Nível de oxigênio disponível (%)
- Estabilidade geral dos sistemas (%)

A cada ciclo, o sistema classifica automaticamente o estado de cada parâmetro, calcula o risco total do ciclo, gera recomendações e ao final exibe um relatório completo da missão.

---

## Estrutura do repositório

```
mission-control-ai/
│
├── README.md
└── mission_control.py
```

---

## Como executar

Requisitos: Python 3.x instalado (sem bibliotecas externas).

```bash
python mission_control.py
```

---

## Regras de alerta

### Temperatura (°C)
| Condição | Classificação |
|---|---|
| Menor que 18 °C | ATENÇÃO |
| De 18 °C até 30 °C | NORMAL |
| Maior que 30 °C até 35 °C | ATENÇÃO |
| Maior que 35 °C | CRITICO |

### Comunicação (%)
| Condição | Classificação |
|---|---|
| Menor que 30% | CRITICO |
| De 30% até 59% | ATENÇÃO |
| 60% ou mais | NORMAL |

### Bateria (%)
| Condição | Classificação |
|---|---|
| Menor que 20% | CRITICO |
| De 20% até 49% | ATENÇÃO |
| 50% ou mais | NORMAL |

### Oxigênio (%)
| Condição | Classificação |
|---|---|
| Menor que 80% | CRITICO |
| De 80% até 89% | ATENÇÃO |
| 90% ou mais | NORMAL |

### Estabilidade (%)
| Condição | Classificação |
|---|---|
| Menor que 40% | CRITICO |
| De 40% até 69% | ATENÇÃO |
| 70% ou mais | NORMAL |

---

## Pontuação de risco

| Classificação | Pontos |
|---|---|
| NORMAL | 0 |
| ATENÇÃO | 1 |
| CRITICO | 2 |

Pontuação máxima por ciclo: 10 pontos (5 parâmetros x 2 pontos).

---

## Classificação do ciclo

| Pontuação total | Classificação |
|---|---|
| 0 a 2 pontos | MISSÃO ESTAVEL |
| 3 a 5 pontos | MISSÃO EM ATENÇÃO |
| 6 a 10 pontos | MISSÃO CRITICA |

---

## Funções implementadas

| Função | Descrição |
|---|---|
| `analisar_temperatura()` | Classifica a temperatura e retorna status, descrição e pontos |
| `analisar_comunicacao()` | Classifica a comunicação e retorna status, descrição e pontos |
| `analisar_bateria()` | Classifica a bateria e retorna status, descrição e pontos |
| `analisar_oxigenio()` | Classifica o oxigênio e retorna status, descrição e pontos |
| `analisar_estabilidade()` | Classifica a estabilidade e retorna status, descrição e pontos |
| `classificar_ciclo()` | Classifica o ciclo com base na pontuação total |
| `analisar_tendencia()` | Compara risco do primeiro e último ciclo |
| `identificar_area_mais_afetada()` | Identifica a área com maior risco acumulado |
| `gerar_recomendacao()` | Gera recomendação automática com base nos alertas do ciclo |
| `gerar_relatorio_final()` | Exibe o relatório consolidado da missão |

---

## Narrativa da missão

| Ciclo | Evento |
|---|---|
| Ciclo 1 | Inicio da missão — todos os sistemas estáveis |
| Ciclo 2 | Queda de comunicação e bateria — sinais de instabilidade |
| Ciclo 3 | Temperatura começa a subir — oxigênio cai levemente |
| Ciclo 4 | Temperatura critica — sistemas fragilizados |
| Ciclo 5 | Colapso de comunicação e energia — missão critica |
| Ciclo 6 | Tentativa de recuperação parcial — sistemas ainda comprometidos |
```
