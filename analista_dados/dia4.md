### 1. **Churn**

O **Churn** mede a taxa de perda de clientes ao longo do tempo. Podemos calcular o churn com base no número de clientes que cancelaram suas vendas ou consultorias, em relação ao número total de clientes.

#### Como calcular:

* **Churn Rate** = (Clientes cancelados no período) / (Clientes totais no início do período)

**Consulta SQL:**

```sql
SELECT 
    COUNT(DISTINCT v.id_cliente) AS clientes_cancelados,
    COUNT(DISTINCT c.id_cliente) AS clientes_totais,
    (COUNT(DISTINCT v.id_cliente) / COUNT(DISTINCT c.id_cliente)) * 100 AS churn_rate
FROM vendas v
JOIN clientes c ON v.id_cliente = c.id_cliente
WHERE v.status = 'cancelada'
AND v.data_cancelamento BETWEEN '2025-01-01' AND '2025-06-30';  -- Exemplo de período
```

Aqui, estamos calculando a taxa de churn para um período específico (de 1º de janeiro a 30 de junho de 2025, por exemplo).

### 2. **CAC (Custo de Aquisição de Clientes)**

O **CAC** mede o custo médio de adquirir um novo cliente. Para calcular isso, precisamos somar os custos de marketing e vendas durante um período e dividir pelo número de novos clientes adquiridos nesse período.

#### Como calcular:

* **CAC** = (Total de custos de marketing e vendas no período) / (Número de clientes adquiridos no período)

Se a tabela de **vendas** ou outra tabela de custo de marketing não estiver presente, você precisará criar um campo ou registrar o custo médio de aquisição de clientes.

**Consulta SQL (sem considerar custos diretos, apenas quantidade de novos clientes):**

```sql
SELECT 
    COUNT(DISTINCT v.id_cliente) AS clientes_adquiridos,
    SUM(c.renda_mensal) AS custo_medio,  -- Supondo um custo médio de aquisição por cliente
    (SUM(c.renda_mensal) / COUNT(DISTINCT v.id_cliente)) AS cac
FROM vendas v
JOIN clientes c ON v.id_cliente = c.id_cliente
WHERE v.status = 'ativa'
AND v.data_venda BETWEEN '2025-01-01' AND '2025-06-30';  -- Exemplo de período
```

Aqui, estamos usando um custo médio baseado na `renda_mensal` dos clientes como uma aproximação do custo de aquisição.

### 3. **LTV (Lifetime Value)**

O **LTV** calcula o valor total que um cliente gera para a empresa durante o tempo em que permanece ativo. A fórmula básica do LTV é:

* **LTV** = (Valor médio de venda) \* (Tempo médio de retenção do cliente)

#### Como calcular:

Você pode calcular o **LTV** com base na receita média mensal e no tempo médio de retenção (baseado no churn).

**Consulta SQL (exemplo simplificado):**

```sql
SELECT 
    AVG(v.valor_mensal) AS receita_media,
    AVG(DATEDIFF(CURDATE(), v.data_venda)) AS tempo_medio_ativacao,  -- Tempo em dias
    (AVG(v.valor_mensal) * (AVG(DATEDIFF(CURDATE(), v.data_venda)) / 30)) AS ltv  -- LTV em termos mensais
FROM vendas v
WHERE v.status = 'ativa'
AND v.data_venda <= '2025-06-30';  -- Exemplo de período
```

Este exemplo considera o valor mensal das vendas e o tempo médio de permanência dos clientes. É possível ajustar para outras variáveis dependendo dos dados disponíveis.

---

### **Views para Análises**

Para facilitar a análise, você pode criar **views** que agreguem e simplifiquem o acesso a essas informações. Aqui estão algumas sugestões de **views** que você poderia criar:

1. **vw\_receita\_diaria** – Para calcular a receita diária gerada pelas vendas.

```sql
CREATE VIEW vw_receita_diaria AS
SELECT 
    v.data_venda,
    SUM(v.valor_mensal) AS receita_diaria
FROM vendas v
WHERE v.status = 'ativa'
GROUP BY v.data_venda;
```

2. **vw\_churn\_diario** – Para calcular o churn diário, baseado nos cancelamentos diários.

```sql
CREATE VIEW vw_churn_diario AS
SELECT 
    v.data_cancelamento,
    COUNT(DISTINCT v.id_cliente) AS churn_diario
FROM vendas v
WHERE v.status = 'cancelada'
GROUP BY v.data_cancelamento;
```

Essas **views** podem ajudar a simplificar a consulta e acelerar o processo de análise de dados.

---
