# Tutorial de como usar click do python 

## 🎯 Objetivo

Aprender a:

* Criar um CLI com `click`
* Usar comandos, argumentos e opções
* Organizar código com boas práticas

---

## 1. 📦 Instalação

```bash
pip install click
```

---

## 2. 👶 Exemplo básico

```python
# cli.py
import click

@click.command()
@click.option('--nome', prompt='Seu nome', help='Nome da pessoa')
def saudacao(nome):
    click.echo(f'Olá, {nome}!')
```

### ▶️ Rodar

```bash
python cli.py --nome Maria
```

Ou só:

```bash
python cli.py
```

> Vai pedir o nome no prompt.

---

## 3. 🎯 Argumentos vs Opções

### Argumento (posicional)

```python
@click.command()
@click.argument('nome')
def ola(nome):
    click.echo(f'Olá, {nome}!')
```

```bash
python cli.py Maria
```

### Opção (com flag)

```python
@click.command()
@click.option('--idade', default=18, help='Sua idade')
def idade(idade):
    click.echo(f'Idade: {idade}')
```

---

## 4. 🔄 Vários comandos (CLI raiz com subcomandos)

```python
# cli.py
import click

@click.group()
def cli():
    pass

@cli.command()
def oi():
    click.echo("Oi!")

@cli.command()
@click.argument("nome")
def tchau(nome):
    click.echo(f"Tchau, {nome}!")

if __name__ == "__main__":
    cli()
```

```bash
python cli.py oi
python cli.py tchau Ana
```

---

## 5. 🧼 Boas práticas

| Prática                       | Por quê?                                  |
| ----------------------------- | ----------------------------------------- |
| Use `@click.group()`          | Para CLIs com vários comandos             |
| Evite código no nível global  | Use `if __name__ == "__main__":`          |
| Use `prompt=` em opções       | Facilita input interativo                 |
| Use `help=` em argumentos     | Ajuda o usuário com `--help`              |
| Organize comandos em arquivos | Para CLIs maiores e reutilização          |
| Valide input com tipos        | Use `type=int`, `type=click.Choice`, etc. |

---

## 6. 💡 Extras úteis

### Tipagem

```python
@click.option('--idade', type=int)
```

### Valores limitados (como enums)

```python
@click.option('--ambiente', type=click.Choice(['dev', 'prod']))
```

### Confirmação

```python
@click.confirmation_option(prompt='Tem certeza?')
def apagar():
    click.echo('Apagado!')
```

---

## 7. 📁 Estrutura recomendada para projetos maiores

```
meu_cli/
├── cli.py          # ponto de entrada
├── comandos/
│   ├── __init__.py
│   ├── usuarios.py
│   └── tarefas.py
```

**Exemplo (`cli.py`):**

```python
import click
from comandos import usuarios, tarefas

@click.group()
def cli():
    pass

cli.add_command(usuarios.usuarios)
cli.add_command(tarefas.tarefas)

if __name__ == '__main__':
    cli()
```

---

## 8. 📦 Transformar em CLI instalável (opcional)

No `setup.py`:

```python
entry_points={
    'console_scripts': [
        'meucli=cli:cli',
    ],
}
```

Aí pode rodar direto no terminal com:

```bash
meucli oi
```

