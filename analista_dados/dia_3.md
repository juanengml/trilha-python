## 🎯 Exercício de BI: Vendas, Receita e Churn

### **Contexto:**

Você trabalha em uma empresa de consultoria de investimentos. A empresa possui dados simulados no banco `cryptodb` com informações sobre clientes, planos vendidos, status de vendas e cancelamentos. O objetivo é analisar a performance de vendas e o comportamento de cancelamento de clientes.

---

## 📌 Parte 1: Crie o Dashboard de **Vendas e Receita**

### **Objetivos:**

* Acompanhar o desempenho mensal de vendas
* Identificar os planos mais vendidos
* Estimar receita mensal recorrente (MRR)
* Calcular o ticket médio por cliente

### **Indicadores e Tarefas:**

1. 📈 **Receita total por mês**

   ```sql
   SELECT 
       DATE_FORMAT(data_venda, '%Y-%m') AS mes,
       SUM(c.valor_mensal) AS receita_total
   FROM vendas v
   JOIN consultorias c ON v.id_consultoria = c.id_consultoria
   WHERE status = 'ativa'
   GROUP BY mes
   ORDER BY mes;
   ```

2. 📊 **Planos mais vendidos**

   ```sql
   SELECT 
       c.nome AS plano,
       COUNT(*) AS vendas
   FROM vendas v
   JOIN consultorias c ON v.id_consultoria = c.id_consultoria
   GROUP BY plano
   ORDER BY vendas DESC;
   ```

3. 💰 **Ticket médio por cliente**

   ```sql
   SELECT 
       v.id_cliente,
       AVG(c.valor_mensal) AS ticket_medio
   FROM vendas v
   JOIN consultorias c ON v.id_consultoria = c.id_consultoria
   GROUP BY v.id_cliente
   ORDER BY ticket_medio DESC;
   ```

4. 📅 **Vendas por trimestre**

   ```sql
   SELECT 
       QUARTER(data_venda) AS trimestre,
       YEAR(data_venda) AS ano,
       COUNT(*) AS qtd_vendas
   FROM vendas
   GROUP BY ano, trimestre
   ORDER BY ano, trimestre;
   ```

---

## 📌 Parte 2: Crie o Dashboard de **Churn e Retenção**

### **Objetivos:**

* Medir o churn mensal
* Acompanhar total de clientes ativos
* Calcular tempo médio de permanência
* Analisar perfis com maior cancelamento

### **Indicadores e Tarefas:**

1. 📉 **Taxa de churn mensal**

   ```sql
   SELECT 
       DATE_FORMAT(data_cancelamento, '%Y-%m') AS mes,
       COUNT(*) AS cancelamentos
   FROM vendas
   WHERE status = 'cancelada'
   GROUP BY mes
   ORDER BY mes;
   ```

2. 👥 **Total de clientes ativos por mês**

   ```sql
   SELECT 
       DATE_FORMAT(data_venda, '%Y-%m') AS mes,
       COUNT(DISTINCT id_cliente) AS clientes_ativos
   FROM vendas
   WHERE status = 'ativa'
   GROUP BY mes
   ORDER BY mes;
   ```

3. ⏳ **Tempo médio de permanência**

   ```sql
   SELECT 
       AVG(DATEDIFF(data_cancelamento, data_venda)) AS dias_medio
   FROM vendas
   WHERE status = 'cancelada';
   ```

4. 🧠 **Churn por plano**

   ```sql
   SELECT 
       c.nome AS plano,
       COUNT(*) AS cancelamentos
   FROM vendas v
   JOIN consultorias c ON v.id_consultoria = c.id_consultoria
   WHERE v.status = 'cancelada'
   GROUP BY c.nome;
   ```

---

## 🛠 Dicas para montar no Metabase:

* Use **gráficos de linha** para métricas temporais (churn, receita)
* Use **gráficos de barras horizontais** para planos ou perfis de cliente
* Crie **filtros de tempo, estado, faixa etária, tipo de plano**
* Adicione uma meta mensal fictícia para comparar com receita real

---

## 🧪 Extra (opcional):

Se quiser, você pode usar também os dados de:

* `interacoes_suporte` → para medir impacto do suporte no churn
* `feedback_cancelamento` → para identificar os principais motivos de saída

---

