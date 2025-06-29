
## ✅ **Respostas (SQL)**

1.

```sql
SELECT * FROM clientes
WHERE estado = 'SP';
```

2.

```sql
SELECT nome, renda_mensal FROM clientes
WHERE renda_mensal > 15000;
```

3.

```sql
SELECT COUNT(*) FROM clientes
WHERE YEAR(data_entrada) = 2023;
```

4.

```sql
SELECT * FROM contratos
WHERE status = 'ativo';
```

5.

```sql
SELECT * FROM contratos
WHERE status = 'cancelado' AND data_fim > '2024-01-01';
```

6.

```sql
SELECT nome, cargo, salario_mensal FROM funcionarios
WHERE salario_mensal > 12000;
```

7.

```sql
SELECT * FROM faturas
WHERE vencimento < CURDATE() AND status = 'aberta';
```

8.

```sql
SELECT * FROM pagamentos
WHERE metodo = 'pix';
```

9.

```sql
SELECT * FROM chamados
WHERE prioridade = 'critica' AND status != 'fechado';
```

10.

```sql
SELECT * FROM clientes
WHERE nome LIKE '%Consultoria%';
```

11.

```sql
SELECT * FROM contratos
WHERE data_inicio BETWEEN '2023-01-01' AND '2023-12-31'
  AND status = 'ativo';
```

12.

```sql
SELECT * FROM clientes
WHERE estado IN ('RJ', 'SP', 'MG');
```

13.

```sql
SELECT * FROM faturas
WHERE valor_bruto > 500 OR valor_desconto > 0;
```

14.

```sql
SELECT * FROM funcionarios
WHERE cargo IN ('Consultor', 'Especialista');
```

15.

```sql
SELECT * FROM chamados
WHERE titulo LIKE 'Erro%';
```

16.

```sql
SELECT nome, renda_mensal FROM clientes
ORDER BY renda_mensal DESC
LIMIT 10;
```

17.

```sql
SELECT * FROM contratos
ORDER BY data_inicio DESC
LIMIT 5;
```

18.

```sql
SELECT nome, cargo, salario_mensal FROM funcionarios
ORDER BY salario_mensal ASC
LIMIT 10;
```

19.

```sql
SELECT * FROM faturas
ORDER BY valor_bruto DESC
LIMIT 20;
```

20.

```sql
SELECT * FROM pagamentos
ORDER BY data_pagamento DESC
LIMIT 5;
```

