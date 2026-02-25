# JDC — Judge Code

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue.svg"/>
  <img src="https://img.shields.io/badge/Architecture-Clean%20Architecture-success"/>
  <img src="https://img.shields.io/badge/UI-Terminal%20UI-purple"/>
  <img src="https://img.shields.io/badge/Database-SQLite-lightgrey"/>
  <img src="https://img.shields.io/github/last-commit/Joao-Vitor-Rd/JDC"/>
</p>

> Um juiz de programação local em **Terminal User Interface (TUI)** desenvolvido em Python com Textual, projetado para praticar problemas algorítmicos diretamente no terminal.

---

## Sumário

* [Visão Geral](#visão-geral)
* [Motivação do Projeto](#motivação-do-projeto)
* [Principais Funcionalidades](#principais-funcionalidades)
* [Preview](#preview)
* [Requisitos](#requisitos)
* [Instalação e Execução](#instalação-e-execução)
* [Arquitetura](#arquitetura)
* [Decisões Arquiteturais](#decisões-arquiteturais)
* [Banco de Dados](#banco-de-dados)
* [Estrutura do Projeto](#estrutura-do-projeto)
* [Melhorias Futuras](#melhorias-futuras)
* [Contribuição](#contribuição)

---

## Visão Geral

O **JDC (Judge Code)** é um judge de programação executado localmente no terminal, projetado para auxiliar no estudo e prática de algoritmos e estruturas de dados.

A aplicação permite navegar por categorias de problemas, visualizar enunciados, implementar soluções em Python e submetê-las para avaliação automática baseada em casos de teste — sem depender de plataformas externas.

O projeto foi desenvolvido com foco em:

* organização arquitetural
* separação de responsabilidades
* experiência fluida em ambiente terminal
* prática local de programação

---

## Motivação do Projeto

O **JDC** foi criado com o objetivo de oferecer uma ferramenta **simples, eficiente e acessível** para o início do aprendizado em programação.

A proposta surgiu da necessidade de um ambiente local que permitisse aos estudantes praticar exercícios sem configurações complexas ou dependência de conexão com plataformas online. Além disso, o sistema foi projetado para ser **facilmente personalizável**, permitindo adaptação para diferentes turmas e níveis de ensino.

Por ser **open source**, o JDC facilita a criação e modificação de conjuntos de problemas e casos de teste, possibilitando a construção rápida de listas personalizadas para diversos contextos educacionais.

O projeto busca unir **simplicidade**, **flexibilidade pedagógica** e **boas práticas arquiteturais**.

---

## Principais Funcionalidades

* Navegação por seções de problemas
* Visualização completa de enunciados
* Edição automática da solução no VS Code
* Avaliação automática baseada em casos de teste
* Persistência local com SQLite
* Interface TUI moderna baseada em teclado

---

## Preview

| Seções                 | Problema              | Submissão            |
| ---------------------- | --------------------- | -------------------- |
| ![](docs/sections.png) | ![](docs/problem.png) | ![](docs/result.png) |

---

## Requisitos

* Python **3.10+**
* Textual
* Visual Studio Code disponível no PATH
* Linux / macOS / Windows (terminal compatível)

---

## Instalação e Execução

### Clone o repositório

```bash
git clone https://github.com/Joao-Vitor-Rd/JDC.git
cd JDC
```

### Crie um ambiente virtual

```bash
python -m venv venv

# Linux/macOS
source venv/bin/activate

# Windows
venv\Scripts\activate
```

### Instale as dependências

```bash
pip install -r requirements.txt
```

### Execute

```bash
python run.py
```

---

## Arquitetura

O projeto segue os princípios da **Clean Architecture**, garantindo baixo acoplamento entre camadas.

```
Presentation  →  Application  →  Domain  ←  Infrastructure
```

### Responsabilidades

| Camada         | Responsabilidade                    |
| -------------- | ----------------------------------- |
| Domain         | Entidades e regras de negócio       |
| Application    | Casos de uso                        |
| Infrastructure | Banco de dados e execução de código |
| Presentation   | Controllers                         |
| UI             | Telas Textual                       |
| Container      | Injeção de dependência              |
| Shared         | Utilitários reutilizáveis           |

---

## Decisões Arquiteturais

### Clean Architecture

Permite o isolamento da lógica de negócio, facilitando manutenção, testes e evolução do sistema.

### Interface Terminal (TUI)

A escolha por uma TUI foi motivada por:

* rapidez de uso
* baixo consumo de recursos
* foco em produtividade via teclado

### Execução Local

A execução totalmente local:

* elimina dependência de internet
* facilita uso em ambientes educacionais
* permite total personalização dos datasets

### SQLite

Selecionado por ser:

* leve
* portátil
* sem necessidade de configuração
* adequado para ambientes acadêmicos e projetos locais

---

## Banco de Dados

O sistema utiliza **SQLite** como persistência local.

| Tabela     | Descrição                           |
| ---------- | ----------------------------------- |
| sections   | Categorias de problemas             |
| problems   | Informações e status das submissões |
| test_cases | Entradas e saídas esperadas         |

As soluções são armazenadas em:

```
~/jdc_data/q{id}.py
```

---

## Estrutura do Projeto

```
JDC/
├── run.py                    # Ponto de entrada
├── requirements.txt
├── sample_data_set_db.sql
└── app/
    ├── app.py                # Aplicação principal Textual
    ├── container/            # Injeção de dependências
    ├── shared/               # Utilitários comuns
    │   ├── database/
    │   └── utils/
    ├── ui/                   # Interface TUI
    │   └── screens/
    └── modules/
        └── evaluation/
            ├── domain/       # Entidades e interfaces
            ├── application/  # Casos de uso
            ├── infrastructure/# SQLite e executor de código
            └── presentation/ # Controllers
```

A organização separa claramente regras de negócio, infraestrutura e interface, facilitando manutenção e extensibilidade.

---

## Melhorias Futuras

* [ ] Suporte a múltiplas linguagens (C++, Java)
* [ ] Sistema de progresso do usuário
* [ ] Importação automática de datasets
* [ ] Relatórios de desempenho

---

## Contribuição

Contribuições são bem-vindas:

1. Abra uma issue
2. Crie uma branch
3. Envie um pull request

