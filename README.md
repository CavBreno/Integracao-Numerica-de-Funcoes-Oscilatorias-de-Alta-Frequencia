# Integração Numérica de Funções Oscilatórias de Alta Frequência

Projeto do **PAVI (Programa de Vivência Interdisciplinar)** — Universidade Federal do Agreste de Pernambuco (UFAPE), Bacharelado em Ciência da Computação.

O projeto investiga o desempenho dos métodos dos **Trapézios** e de **Simpson (1/3)** na integração numérica de funções senoidais de diferentes frequências, avaliando até que ponto a superioridade teórica da Regra de Simpson se mantém quando a oscilação da função aumenta.

## Problema de pesquisa

> A superioridade do método de Simpson sobre o método dos Trapézios, amplamente conhecida para funções suaves, permanece válida quando a frequência de oscilação da função aumenta significativamente? Existe uma relação entre frequência e refinamento da malha capaz de comprometer a precisão das aproximações numéricas?

## Objetivo geral

Investigar experimentalmente o desempenho dos métodos dos Trapézios e de Simpson (1/3) na integração numérica de funções da forma `f(x) = sin(kx)`, analisando a influência da frequência `k` sobre a precisão, a convergência, a eficiência computacional e a qualidade das aproximações numéricas.

### Objetivos específicos

- Revisar os fundamentos matemáticos da integração numérica (Riemann, Trapézios, Simpson)
- Implementar os métodos em Python e validar suas ordens teóricas de convergência para funções de baixa frequência
- Investigar o comportamento dos métodos para `f(x) = sin(kx)` variando `k`
- Analisar os efeitos do refinamento da malha sobre a precisão das aproximações
- Estudar o critério de Nyquist, subamostragem e o fenômeno de *aliasing* no contexto da integração numérica
- Determinar a quantidade mínima de subdivisões necessária para representar cada frequência
- Comparar a eficiência computacional entre os dois métodos
- Produzir gráficos, tabelas e materiais de divulgação científica com os resultados

## Metodologia

A investigação segue uma **análise determinística**, usando funções `f(x) = sin(kx)` com integrais analíticas conhecidas como referência de erro.

- **Frequências analisadas:** `k ∈ {1, 5, 10, 20, 50, 100, 200}` (agrupadas em baixa, média e alta frequência)
- **Refinamentos de malha:** `N ∈ {50, 100, 200, 500, 1000}`
- **Métrica de erro:** erro absoluto `E = |I − Iₕ|`, onde `I` é o valor exato e `Iₕ` a aproximação numérica

Os resultados são organizados em tabelas (`k`, `N`, método, valor aproximado, valor exato, erro) e em gráficos log-log de convergência, erro versus frequência e comparação direta entre os métodos (`R(N) = E_Trap(N) / E_Simp(N)`).

## Estrutura do repositório

O código é organizado por semana de desenvolvimento, seguindo a evolução do estudo dos métodos:

```
├── teoremaFundamentalDoCalculo.py         # Template base: cálculo de integral via primitiva (TFC)
├── Semana 1/
│   ├── Semana1_ProblemaA.py               # TFC aplicado a f(x) = x² em [0, 1]
│   ├── Semana1_ProblemaB.py               # TFC aplicado a f(x) = sin(x) em [0, π]
│   └── Semana1_ProblemaC.py               # TFC aplicado a f(x) = eˣ em [0, 1]
├── Semana 2/
│   └── Semana2_SomadeRiemman.py           # Soma de Riemann para f(x) = eˣ, com teste de convergência (n = 10, 100, 1000)
├── Semana 3/
│   └── Semana3_RegraDosTrapézios.py       # Regra dos Trapézios composta para f(x) = sin(x) em [0, π]
└── Semana 4/
    └── Semana4_RegraDeSimpson.py          # Regra de Simpson 1/3 composta para f(x) = x³ em [0, 1]
```

Cada script imprime uma tabela comparando o número de subdivisões, o valor aproximado, o valor exato da integral e o erro absoluto obtido.

## Requisitos

- Python 3.x
- Nenhuma dependência externa — os scripts usam apenas a biblioteca padrão (`math`)

## Como executar

Cada arquivo é independente e pode ser executado diretamente:

```bash
python3 "Semana 1/Semana1_ProblemaA.py"
python3 "Semana 2/Semana2_SomadeRiemman.py"
python3 "Semana 3/Semana3_RegraDosTrapézios.py"
python3 "Semana 4/Semana4_RegraDeSimpson.py"
```

## Cronograma (resumo)

| Semanas | Tema |
|---|---|
| 1–2 | Fundamentação matemática (integrais, TFC, integração numérica, erro e convergência) |
| 3 | Regra dos Trapézios |
| 4 | Regra de Simpson |
| 5–6 | Funções oscilatórias, critério de Nyquist e aliasing |
| 7–8 | Implementação computacional e planejamento experimental |
| 9–11 | Experimentos com baixa, média e alta frequência |
| 12–13 | Análise dos resultados e discussão científica |
| 14–15 | Redação do artigo, pôster e encerramento |

## Possíveis trabalhos futuros

- Funções oscilatórias compostas (`sin(kx) + sin(rx)`) e interação entre frequências
- Funções oscilatórias amortecidas (`e^(−ax) sin(kx)`)
- Integração adaptativa e quadratura de Gauss para altas frequências
- Efeitos de ruído experimental em funções oscilatórias

## Referências

- STEWART, James. *Cálculo*, v. 1. São Paulo: Cengage Learning.
- BARROSO, Leonidas Conceição et al. *Cálculo Numérico com Aplicações*. 2. ed. São Paulo: Harbra.
- BURDEN, Richard L.; FAIRES, J. Douglas. *Numerical Analysis*. 10. ed. Boston: Cengage Learning.
- CHAPRA, S. C.; CANALE, R. P. *Métodos Numéricos para Engenharia*. 7. ed. Porto Alegre: AMGH, 2016.

## Instituição

Universidade Federal do Agreste de Pernambuco (UFAPE) — Bacharelado em Ciência da Computação
Programa de Vivência Interdisciplinar (PAVI)
