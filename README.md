# Projeto Integrador - API Educacional (CAEd)

API backend em **FastAPI** para importação, consulta, atualização e consolidação de dados educacionais (CAEd), incluindo:

- carga de planilhas Excel com resultados por estudante;
- manutenção de mapeamento de habilidades por questão;
- geração de arquivo Excel para exportação;
- cálculo de resultados agregados por habilidade;
- gestão e consolidação de questionários por turma.

## Visão Geral

O projeto foi desenvolvido em Python e se conecta a um banco **MySQL**. A aplicação disponibiliza endpoints REST para:

- receber planilhas de resultados e persistir dados em múltiplas tabelas;
- consultar dados detalhados por filtros (ano, matéria, turma, série, bimestre/semestre);
- atualizar códigos de habilidade e respostas de questionário;
- retornar indicadores consolidados para dashboards;
- exportar consultas em formato `.xlsx`.

## Tecnologias

- Python 3.8
- FastAPI
- Uvicorn / Gunicorn
- Pandas
- OpenPyXL / XlsxWriter
- MySQL Connector Python

Dependências completas em `requirements.txt`.

## Estrutura do Repositório

```text
.
|-- main.py
|-- requirements.txt
|-- runtime.txt
|-- Procfile
`-- database/
    |-- educacaodb_consulta_caed.sql
    |-- educacaodb_habilidade_caed.sql
    |-- educacaodb_questionario.sql
    |-- educacaodb_questionario_grupo.sql
    |-- educacaodb_questionario_turma.sql
    |-- educacaodb_questio_turma_op.sql
    `-- educacaodb_opcoes.sql
```

## Configuração de Ambiente

A conexão com banco usa variáveis de ambiente:

- `HRK_DB_USER`
- `HRK_DB_PASS`
- `HRK_DB_HOST`
- `HRK_DB_NAME`

Exemplo (PowerShell):

```powershell
$env:HRK_DB_USER="seu_usuario"
$env:HRK_DB_PASS="sua_senha"
$env:HRK_DB_HOST="localhost"
$env:HRK_DB_NAME="educacaodb"
```

## Instalação e Execução

1. Criar e ativar ambiente virtual.
2. Instalar dependências.
3. Configurar variáveis de ambiente do MySQL.
4. Executar API.

Exemplo local:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn main:app --reload
```

Para deploy (conforme `Procfile`):

```bash
gunicorn -w 4 -k uvicorn.workers.UvicornWorker main:app
```

## CORS

A API está configurada para permitir origens:

- `http://localhost`
- `http://localhost:8080`
- `http://localhost:3000`
- `https://webescolacaed.herokuapp.com`
- `http://webescolacaed.herokuapp.com`

## Modelo de Dados (Banco)

Tabelas principais utilizadas:

- `consulta_caed`: resultados por estudante e habilidade (`h_01` ... `h_30`).
- `habilidade_caed`: mapeamento de questão para código da habilidade.
- `questionario`: perguntas do questionário.
- `questionario_grupo`: agrupadores temáticos das perguntas.
- `opcoes`: opções de resposta por pergunta.
- `questionario_turma`: vínculo de questionário por estudante/turma.
- `questio_turma_op`: respostas selecionadas por pergunta.

Scripts de criação e carga inicial estão na pasta `database/`.

## Endpoints

### 1) Exportação CAEd

- **POST** `/downloadfile/`
- Gera e retorna um arquivo Excel com dados filtrados da `consulta_caed`.
- Query params:
  - `recuperacao` (str)
  - `ano` (int)
  - `materia` (str)
  - `turma` (str)
  - `serie` (int)
  - `bimestre` (int)
  - `vazia` (int, opcional, padrão `0`)

### 2) Consulta detalhada CAEd

- **GET** `/consultacaed/`
- Retorna dados da `consulta_caed` e cabeçalho de habilidades (`table_header`) com rótulos vindos de `habilidade_caed`.
- Query params:
  - `recuperacao`, `ano`, `materia`, `turma`, `serie`, `bimestre`

### 3) Consulta de habilidades

- **GET** `/habilidadecaed/`
- Lista registros de `habilidade_caed` por filtro.
- Query params:
  - `ano`, `materia`, `turma`, `serie`, `bimestre`

### 4) Atualização de código de habilidade

- **PUT** `/habilidadecaed/{id}`
- Atualiza `cod_da_habilidade` de um registro e retorna o objeto atualizado.
- Path param:
  - `id` (int)
- Query param:
  - `cod_da_habilidade` (str)

### 5) Upload de planilha

- **POST** `/uploadfile/`
- Recebe arquivo Excel (`multipart/form-data`) e executa carga/atualização em:
  - `consulta_caed`
  - `habilidade_caed`
  - `questionario_turma`
  - `questio_turma_op`
- Campo esperado no form:
  - `content` (arquivo)
- Retorno: nome do arquivo processado.

### 6) Resultado consolidado CAEd

- **GET** `/resultadocaed/`
- Calcula percentuais agregados por habilidade (`H_01` ... `H_30`), separados por recuperação continuada (`SIM`/`NÃO`), com rótulos da `habilidade_caed`.
- Query params:
  - `ano`, `materia`, `turma`, `serie`, `bimestre`

### 7) Questionários por turma

- **GET** `/questionarioturma/`
- Lista estudantes/questionários da turma com status calculado (`RESPONDIDO` / `PENDENTE`).
- Query params:
  - `ano`, `materia`, `turma`, `serie`, `semestre`

### 8) Itens do questionário do estudante

- **GET** `/questionarioturmaop/`
- Retorna perguntas vinculadas ao `idquestionario_turma`, incluindo lista de opções por pergunta.
- Query params:
  - `idquestionario_turma` (int)

### 9) Atualização de respostas do questionário

- **PUT** `/questionarioturmaop/`
- Atualiza respostas em lote na tabela `questio_turma_op`.
- Body esperado: lista de objetos com:
  - `idquestio_turma_op`
  - `idopcoes`

### 10) Resultado consolidado do questionário

- **GET** `/resultadoquestionario/`
- Consolida percentual de respostas por grupo de questionário (`questionario_grupo`) com base nas opções marcadas.
- Query params:
  - `ano`, `materia`, `turma`, `serie`, `semestre`

## Formato de Planilha para Upload

A carga de `consulta_caed` utiliza colunas do Excel como:

- `RECUPERACAO CONTINUADA`
- `ano`
- `Bimestre`
- `serie`
- `turma`
- `materia`
- `ESTUDANTE`
- `PARTICIPAÇÃO`
- `Nº DE ITENS RESPONDIDOS`
- `% ACERTOS`
- `CATEGORIA DE DESEMPENHO` (opcional)
- `TIPO DE INTERVENÇÃO`
- `ITENS ACERTADOS`
- `H 01` até `H 30`

## Fluxo Funcional Resumido

1. Upload da planilha de resultados.
2. Persistência/atualização dos dados CAEd por estudante.
3. Geração automática de base de habilidades (`h_01`...`h_30`) quando necessário.
4. Geração da base de questionário por estudante/turma e criação dos itens de resposta.
5. Consulta de dados detalhados e indicadores consolidados.
6. Exportação dos dados filtrados para Excel.
