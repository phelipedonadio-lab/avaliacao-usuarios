# 📋📞 Pesquisa de Atendimento ao Cliente

![Python](https://skillicons.dev/icons?i=python) ![VS Code](https://skillicons.dev/icons?i=vscode)

![Nível](https://img.shields.io/badge/Nível-Iniciante-yellow?style=for-the-badge)

---

## 📑 Sumário

- [📋📞 Pesquisa de Atendimento ao Cliente](#-pesquisa-de-atendimento-ao-cliente)
  - [📑 Sumário](#-sumário)
  - [Descrição](#descrição)
  - [Objetivo do Projeto](#objetivo-do-projeto)
  - [▶️ Como Executar](#️-como-executar)
  - [Instruções de Uso](#instruções-de-uso)
  - [📋 Tabela de Regras de Classificação](#-tabela-de-regras-de-classificação)
  - [💬 Exemplo de Execução](#-exemplo-de-execução)
  
---

## Descrição

O objetivo é coletar, por meio de uma **pesquisa com 50 entrevistados**, a opinião de cada um sobre o **atendimento ao cliente** recebido (EXCELENTE, BOM ou RUIM), contabilizando e apresentando as respostas no final.

---

## Objetivo do Projeto

Praticar conceitos fundamentais de programação, como:

- 📥📤 Entrada e saída de dados (`input()` / `print()`)
- 🔁 Estrutura de repetição (`for`)
- 🔀 Estrutura de decisão (`match` / `case`)
- ➕ Contadores (variáveis acumuladoras)
- ✂️ Tratamento de strings (`.title()`)
  
---
 
## ▶️ Como Executar
 
```bash
python app.py
```
 
> [!NOTE]
> Requer Python 3.10 ou superior, pois o programa usa a estrutura `match`/`case`.
 
---

## Instruções de Uso

1. Execute o arquivo `app.py`.
2. Para cada um dos 50 entrevistados, informe: nome, idade e a opção correspondente à opinião sobre o atendimento (1, 2 ou 3).

     > [!WARNING]
   > Informe a opinião apenas com o número da opção (ex.: digite `1`, não `EXCELENTE`).

3. Exemplo: `maria`, `29`, `1` → o programa exibe "Maria, sua avaliação foi registrada como Excelente. Muito obrigado!" (o nome é formatado automaticamente com `.title()`).
4. Ao final das 50 entrevistas, o programa exibe o total de notas EXCELENTES, BONS e RUINS.

---

## 📋 Tabela de Regras de Classificação

Complementando o fluxo do programa, uma tabela de regras facilita consultas rápidas — é o mesmo tipo de artefato usado em documentações técnicas para deixar regras de negócio explícitas e fáceis de atualizar quando as opções mudarem.

| Opção digitada | Classificação | Contabilizada em  |
| -------------- | ------------- | ----------------- |
| 1              | EXCELENTE     | `total_excelente` |
| 2              | BOM           | `total_bom`       |
| 3              | RUIM          | `total_ruim`      |
| Outro valor    | Inválida      | Não contabilizada |
 
---
 
## 💬 Exemplo de Execução
 
<details>
<summary>Clique para ver um exemplo de entrada e saída</summary>
<pre>
Digite seu nome: maria
Digite sua idade: 29
Avalie o serviço prestado:
1 - Excelente
2 - Bom
3 - Ruim
Digite o número da opção de avaliação: 1
Maria, sua avaliação foi registrada como Excelente. Muito obrigado!
...
Quantidade de notas EXCELENTES: 1
Quantidade de notas BONS: 0
Quantidade de notas RUINS: 0
</pre>
 
</details>
 
