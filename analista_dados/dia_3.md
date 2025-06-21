
## 🧪 **Exercício Prático com Pandas + MySQL**

### 🎯 Objetivo:

Praticar leitura de dados com `pandas`, manipulação de DataFrames e análise de indicadores de vendas e churn usando **dados reais do banco** `cryptodb`.

---

## ✅ Parte 1 – Conexão e Leitura dos Dados

### **Tarefa 1:** Leia as 3 tabelas principais diretamente do banco:

* `clientes`
* `vendas`
* `consultorias`

> Use `pandas.read_sql()` e `mysql.connector`.

```python
import pandas as pd
import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='SUA_SENHA',
    database='cryptodb'
)

clientes = pd.read_sql("SELECT * FROM clientes", conn)
vendas = pd.read_sql("SELECT * FROM vendas", conn)
consultorias = pd.read_sql("SELECT * FROM consultorias", conn)
```

---

## ✅ Parte 2 – Análises de Vendas e Receita

### **Tarefa 2:** Calcule a receita total por mês

* Junte `vendas` e `consultorias`
* Filtre `status = 'ativa'`
* Agrupe por mês de `data_venda`
* Calcule a soma de `valor_mensal`

```python
vendas_ativas = vendas[vendas['status'] == 'ativa']
df = vendas_ativas.merge(consultorias, on='id_consultoria')
df['mes'] = pd.to_datetime(df['data_venda']).dt.to_period('M')
receita_mensal = df.groupby('mes')['valor_mensal'].sum().reset_index()
```

---

### **Tarefa 3:** Descubra o plano mais vendido

```python
mais_vendidos = vendas.groupby('id_consultoria').size().reset_index(name='quantidade')
mais_vendidos = mais_vendidos.merge(consultorias, on='id_consultoria').sort_values(by='quantidade', ascending=False)
```

---

## ✅ Parte 3 – Churn e Retenção

### **Tarefa 4:** Calcule o churn mensal

```python
vendas_canceladas = vendas[vendas['status'] == 'cancelada'].copy()
vendas_canceladas['mes'] = pd.to_datetime(vendas_canceladas['data_cancelamento']).dt.to_period('M')
churn_mensal = vendas_canceladas.groupby('mes').size().reset_index(name='cancelamentos')
```

---

### **Tarefa 5:** Calcule o tempo médio até cancelamento

```python
vendas_canceladas['tempo_dias'] = (
    pd.to_datetime(vendas_canceladas['data_cancelamento']) - pd.to_datetime(vendas_canceladas['data_venda'])
).dt.days

tempo_medio = vendas_canceladas['tempo_dias'].mean()
```

---

### **Tarefa 6:** Qual estado tem mais churn?

```python
cancelados = vendas_canceladas.merge(clientes, on='id_cliente')
churn_por_estado = cancelados.groupby('estado').size().reset_index(name='cancelamentos').sort_values(by='cancelamentos', ascending=False)
```

---

## 📋 Bônus – Visualização com Pandas

Você pode visualizar os dados direto com:

```python
import matplotlib.pyplot as plt

# Receita mensal
receita_mensal.plot(x='mes', y='valor_mensal', kind='line', title='Receita por Mês')
plt.show()

# Churn mensal
churn_mensal.plot(x='mes', y='cancelamentos', kind='bar', title='Churn Mensal')
plt.show()
```

---

### 🧠 O que o exercício treina:

* Conexão com banco MySQL
* Leitura e junção de dados com `pandas`
* Agrupamentos, filtros e transformações
* Análise de churn e vendas
* Visualização simples com `matplotlib`

---
