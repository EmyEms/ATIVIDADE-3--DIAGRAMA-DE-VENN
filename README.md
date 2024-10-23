---

# Análise Lógica: Situação da Festa de Ana e Bruno

Este repositório contém uma implementação em Python que analisa uma situação lógica envolvendo dois amigos, Ana e Bruno, com base em proposições lógicas. O objetivo é gerar uma tabela verdade que considera diferentes cenários e avalia se a festa será animada.

## Objetivo

A situação descrita é a seguinte:
1. Se Ana vai à festa (\(P\)), então Bruno também vai (\(Q\)).
2. Se pelo menos um deles for à festa, a festa será animada (\(R\)).
3. Se Ana não for, a festa só será animada se Bruno trouxer música (\(M\)).

Com base nessas proposições, o programa gera uma **tabela verdade** para avaliar os cenários possíveis.

## Proposições Lógicas

1. **P**: Ana vai à festa.
2. **Q**: Bruno vai à festa.
3. **M**: Bruno traz música.
4. **R**: A festa é animada.

### Expressões Lógicas

- **P → Q**: Se Ana vai à festa, então Bruno também vai.
- **P ∨ Q → R**: Se pelo menos um deles vai à festa, a festa será animada.
- **¬P → (M → R)**: Se Ana não vai, a festa só será animada se Bruno trouxer música.

### Lógica do Algoritmo

1. **Definição das Implicações**: O código usa uma função `implica(p, q)` para avaliar \(P \to Q\) e \(M \to R\).
2. **Combinações de Proposições**: Para cada combinação de \(P\), \(Q\), e \(M\) (verdadeiro ou falso), o código avalia as proposições lógicas.
3. **Avaliação de \(R\)**: 
   - Se Ana vai à festa (\(P\)), então \(R\) será verdadeiro se \(P \vee Q\) for verdadeiro.
   - Se Ana não vai à festa (\(¬P\)), então a festa só será animada (\(R\)) se Bruno trouxer música (\(M\)).



## Tabela Verdade

Ao executar o código Python, obtemos a seguinte tabela verdade, que cobre todas as combinações de \(P\), \(Q\), e \(M\):

```
P    Q    M    P → Q     P ∨ Q → R      ¬P → (M → R)    R
True  True  True  True      True           True           True
True  True  False True      True           True           True
True  False True  False     True           True           True
True  False False False     True           True           True
False True  True  True      True           True           True
False True  False True      True           True           True
False False True  True      False          True           True
False False False True      False          False          False
```

## Testes

### Teste 1:
Entrada: \( P = True \), \( Q = True \), \( M = True \)

Saída:
```
P    Q    M    P → Q     P ∨ Q → R      ¬P → (M → R)    R
True  True  True  True      True           True           True
```
Explicação: Ambos vão à festa, e a festa será animada.

### Teste 2:
Entrada: \( P = False \), \( Q = False \), \( M = True \)

Saída:
```
P    Q    M    P → Q     P ∨ Q → R      ¬P → (M → R)    R
False False True  True      False          True           True
```
Explicação: Ana não vai à festa, mas como Bruno traz música, a festa será animada.

## Esboço no GeoGebra

O diagrama de Venn a seguir ilustra as condições lógicas da situação da festa. As proposições \(P\), \(Q\), \(M\) e \(R\) estão representadas pelas interseções dos conjuntos.

![Diagrama de Venn](https://raw.githubusercontent.com/EmyEms/ATIVIDADE-3--DIAGRAMA-DE-VENN/refs/heads/main/DIAGRAMA.jpeg)

Você também pode visualizar o diagrama completo no **GeoGebra** através do seguinte link:

[Link para o GeoGebra](https://www.geogebra.org/calculator/gvveazh5)

