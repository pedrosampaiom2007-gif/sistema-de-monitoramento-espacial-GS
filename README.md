# Mission Control AI — Projeto Brazil-space monitoring

Sistema inteligente de monitoramento de sistemas energéticos de uma missão espacial experimental.


---

## Equipe Star Brazil

| Nome | RM |
|---|---|
| Luan de Araujo Carneiro | 573691 |
| Pedro Sampaio Mochnacs Arruda | 573522 |
| Raul Sampaio Mochnacs Arruda | 573523 |

---

## Sobre o projeto

O **Mission Control AI** é uma plataforma de monitoramento inteligente de sistemas energéticos de uma missão espacial experimental chamada **Projeto Brazil-space monitoring**.

O sistema recebe dados simulados de 6 ciclos operacionais, interpreta automaticamente as condições da missão, gera alertas, toma decisões básicas diante de situações críticas e exibe um relatório consolidado ao final. O foco central é o **monitoramento e a gestão eficiente da energia renovável** disponível na missão — principal desafio de sustentabilidade no ambiente espacial.

Os 5 parâmetros monitorados a cada ciclo são:

- Temperatura interna do módulo (°C)
- Qualidade do sinal de comunicação (%)
- Nível de bateria / energia armazenada (%)
- Nível de oxigênio disponível (%)
- Estabilidade geral dos sistemas (%)

---

## Energias renováveis e sustentabilidade (SERS)

### O desafio energético em missões espaciais

Em missões espaciais, a energia é o recurso mais crítico e limitado da operação. Diferente de sistemas terrestres, um módulo orbital não pode recorrer a uma rede elétrica — toda a energia precisa ser gerada, armazenada e gerenciada com extrema eficiência.

A principal fonte de energia renovável em missões espaciais são os **painéis fotovoltaicos (solares)**, que convertem a radiação solar diretamente em eletricidade. Essa energia é armazenada em **baterias de alta densidade**, que alimentam o módulo durante períodos de eclipse ou em momentos de alta demanda operacional.

### Como o sistema monitora a energia renovável

O parâmetro **bateria** representa o estado de carga do banco de baterias que acumula a energia gerada pelos painéis solares. Os três níveis de alerta foram calibrados para refletir cenários reais de gestão energética espacial:

| Nível de bateria | Classificação | Significado energético |
|---|---|---|
| 50% ou mais | NORMAL | Painéis solares em geração ativa — banco de baterias com reserva adequada |
| 20% a 49% | ATENÇÃO | Geração solar insuficiente ou eclipse prolongado — consumo supera a geração |
| Abaixo de 20% | CRÍTICO | Reserva mínima de potência atingida — risco de falha total dos sistemas |

Quando a bateria atinge estado **CRÍTICO**, o sistema emite automaticamente:

> *"Ativar modo de economia e direcionar captação fotovoltaica para suporte à vida"*

Essa decisão reflete um princípio fundamental de **eficiência energética**: em escassez, priorizar oxigênio, temperatura e pressão, desligando experimentos científicos e comunicações secundárias.

### Sustentabilidade aplicada ao contexto espacial

A sustentabilidade no contexto espacial significa manter a operação pelo maior tempo possível com os recursos disponíveis, sem desperdício. O Mission Control AI aplica esse princípio de três formas:

1. **Monitoramento contínuo e preventivo** — ao identificar quedas progressivas no nível de bateria (ciclos 2 a 5 da missão simulada), o sistema emite alertas antes que a situação se torne irreversível, permitindo ajustes de consumo proativos.

2. **Tomada de decisão automatizada e escalonada** — o sistema gera recomendações proporcionais à gravidade. Quando três ou mais sistemas estão críticos simultaneamente, aciona o modo de segurança completo, priorizando suporte à vida e comunicação com a base.

3. **Análise de tendência energética** — ao comparar o risco do primeiro e do último ciclo, o sistema identifica se a missão está em trajetória de melhora ou deterioração, informação essencial para decidir entre continuar ou abortar a operação.

### Conexão com a agenda global de energias renováveis

A dependência de energia solar em missões espaciais é um dos casos mais puros de aplicação de energia renovável: não há combustível fóssil, não há rede elétrica, não há alternativa — o sol é a única fonte. Sistemas inteligentes de monitoramento e gestão dessa energia são diretamente análogos aos desafios de microrredes solares terrestres, veículos elétricos e edificações de energia zero. O Mission Control AI é, em essência, um sistema de gestão de energia renovável aplicado ao ambiente mais extremo possível.

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
| Maior que 35 °C | CRÍTICO |

### Comunicação (%)
| Condição | Classificação |
|---|---|
| Menor que 30% | CRÍTICO |
| De 30% até 59% | ATENÇÃO |
| 60% ou mais | NORMAL |

### Bateria (%)
| Condição | Classificação |
|---|---|
| Menor que 20% | CRÍTICO |
| De 20% até 49% | ATENÇÃO |
| 50% ou mais | NORMAL |

### Oxigênio (%)
| Condição | Classificação |
|---|---|
| Menor que 80% | CRÍTICO |
| De 80% até 89% | ATENÇÃO |
| 90% ou mais | NORMAL |

### Estabilidade (%)
| Condição | Classificação |
|---|---|
| Menor que 40% | CRÍTICO |
| De 40% até 69% | ATENÇÃO |
| 70% ou mais | NORMAL |

---

## Pontuação de risco

| Classificação | Pontos |
|---|---|
| NORMAL | 0 |
| ATENÇÃO | 1 |
| CRÍTICO | 2 |

Pontuação máxima por ciclo: 10 pontos (5 parâmetros × 2 pontos).

---

## Classificação do ciclo

| Pontuação total | Classificação |
|---|---|
| 0 a 2 pontos | MISSÃO ESTÁVEL |
| 3 a 5 pontos | MISSÃO EM ATENÇÃO |
| 6 a 10 pontos | MISSÃO CRÍTICA |

A classificação final da missão é calculada com base na **média de risco arredondada** de todos os ciclos, aplicando a mesma escala acima.

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
| Ciclo 1 | Início da missão — todos os sistemas estáveis |
| Ciclo 2 | Queda de comunicação e bateria — sinais de instabilidade |
| Ciclo 3 | Temperatura começa a subir — oxigênio cai levemente |
| Ciclo 4 | Temperatura crítica — sistemas fragilizados |
| Ciclo 5 | Colapso de comunicação e energia — missão crítica |
| Ciclo 6 | Tentativa de recuperação parcial — sistemas ainda comprometidos |
