# Escopo de Estudo para Selenium e Beautiful Soup (1 Semana)

## Dia 1: Introdução ao Web Scraping e Ambiente de Desenvolvimento
- **Objetivo**: Entender os fundamentos do web scraping e configurar o ambiente de desenvolvimento.
  - **Tópicos**:
    - O que é Web Scraping?
    - Diferenças entre Selenium e Beautiful Soup.
    - Aspectos legais do scraping (robots.txt, limites éticos).
    - Instalação do Python, Selenium, Beautiful Soup e navegadores (Chrome, Firefox).
    - Introdução ao HTML e CSS (tags, classes, ids, DOM básico).
  - **Atividades**:
    - Instalar dependências: `pip install selenium beautifulsoup4`.
    - Instalar o driver de navegador (e.g., ChromeDriver).
    - Escolher um site simples e inspecionar elementos com DevTools.

## Dia 2: Primeiros Passos com Beautiful Soup
- **Objetivo**: Aprender a extrair dados estáticos de páginas HTML.
  - **Tópicos**:
    - Leitura de HTML com Beautiful Soup.
    - Navegação na árvore DOM.
    - Métodos de busca: `find()`, `find_all()`, `select()`.
    - Extração de dados: texto, atributos de elementos (href, src).
  - **Atividades**:
    - Fazer scraping de uma página estática.
    - Praticar a extração de títulos, links e imagens de um site simples.
    - Salvar os dados extraídos em um arquivo CSV.

## Dia 3: Introdução ao Selenium para Automação de Navegadores
- **Objetivo**: Usar Selenium para navegar e interagir com páginas dinâmicas.
  - **Tópicos**:
    - Configurando Selenium com diferentes navegadores.
    - Comandos básicos: abrir uma página, clicar em botões, preencher formulários.
    - Espera implícita e explícita.
    - Lidando com pop-ups e alertas.
  - **Atividades**:
    - Abrir uma página com Selenium e automatizar uma busca simples (ex: pesquisar no Google).
    - Implementar espera para carregar elementos dinâmicos.

## Dia 4: Integração Selenium + Beautiful Soup
- **Objetivo**: Combinar Selenium e Beautiful Soup para scraping de páginas dinâmicas.
  - **Tópicos**:
    - Extração de HTML dinâmico com Selenium.
    - Uso de Beautiful Soup para processar o conteúdo obtido com Selenium.
    - Casos em que ambos são necessários (ex: interagir com páginas antes de scraping).
  - **Atividades**:
    - Navegar em um site dinâmico com Selenium (ex: uma página de resultados paginados).
    - Extrair os dados da página usando Beautiful Soup após interação com Selenium.
    - Salvar os dados extraídos em um arquivo JSON.

## Dia 5: Lidando com Paginação e Conteúdos Dinâmicos
- **Objetivo**: Aprender a navegar por múltiplas páginas e lidar com carregamento dinâmico.
  - **Tópicos**:
    - Navegação por múltiplas páginas (ex: botões "Próxima" ou scroll infinito).
    - Scroll dinâmico com Selenium.
    - Simulação de cliques para carregar novos conteúdos.
  - **Atividades**:
    - Realizar scraping de uma página com paginação.
    - Automatizar o clique em botões de "Próxima" e coletar dados de várias páginas.
    - Tratar diferentes carregamentos dinâmicos (ex: scroll infinito).

## Dia 6: Tratamento de Exceções e Depuração
- **Objetivo**: Lidar com erros e exceções durante o scraping.
  - **Tópicos**:
    - Tratamento de exceções no Selenium (ex: `NoSuchElementException`).
    - Lidando com mudanças na estrutura do HTML.
    - Estratégias de retry para falhas em requests.
    - Uso de logging para depuração.
  - **Atividades**:
    - Adicionar try-except para casos onde elementos não são encontrados.
    - Criar logs para registrar o progresso e erros durante o scraping.
    - Simular e resolver falhas de scraping.

## Dia 7: Projeto Final de Scraping
- **Objetivo**: Aplicar os conceitos aprendidos em um projeto de scraping completo.
  - **Tópicos**:
    - Escolher um site real e projetar uma estratégia de scraping.
    - Combinar Selenium e Beautiful Soup para coletar dados.
    - Salvamento de dados (CSV, JSON ou banco de dados).
  - **Atividades**:
    - Implementar um script que navega em um site de sua escolha, coleta dados relevantes e os salva em um formato estruturado.
    - Melhorar o código com tratamento de exceções e espera adequada.

## Materiais e Ferramentas Sugeridas:
- **Documentação**:
  - Selenium: https://www.selenium.dev/documentation/
  - Beautiful Soup: https://www.crummy.com/software/BeautifulSoup/bs4/doc/
- **Ferramentas**:
  - Python 3.x.
  - Navegador Chrome ou Firefox com DevTools.
  - CSV, JSON para exportação de dados.

## Resultado Esperado:
Ao final da semana, você terá uma boa noção de como automatizar interações com páginas web, extrair dados estáticos e dinâmicos, e armazená-los de forma estruturada.
