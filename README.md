#Sistema de Times de Futebol com Django

## Descrição

Este projeto foi desenvolvido utilizando o framework Django com o objetivo de criar uma aplicação web simples para cadastro e visualização de times de futebol.

A aplicação permite cadastrar os times pelo painel administrativo e visualizar os dados em uma página web.

---

## Objetivo

Aplicar conceitos fundamentais do Django:

* Models
* Views
* URLs
* Templates
* Admin

---

## Tecnologias utilizadas

* Python
* Django
* SQLite
* HTML

---

## Funcionalidades

* Cadastro de times pelo admin
* Armazenamento em banco de dados
* Exibição dos times na página inicial

---

## 📸 Imagens do Sistema

### Página Principal

<img width="1432" height="843" alt="image" src="https://github.com/user-attachments/assets/a9313f4f-9863-47ec-adac-67892ce560a4" />


---

### Painel Administrativo

<img width="1917" height="1012" alt="image" src="https://github.com/user-attachments/assets/fe8ce747-c4f8-40b9-8854-fa50eae12c9f" />


---

## Como executar o projeto

### 1. Criar ambiente virtual

```
python -m venv venv
```

### 2. Ativar o ambiente

```
venv\Scripts\activate
```
Se der erro no VSCode, troque o terminal para Command Prompt.

### 3. Instalar dependências

```
pip install -r requirements.txt
```

### 4. Rodar migrações

```
python manage.py migrate
```

### 5. Criar superusuário

```
python manage.py createsuperuser
```

### 6. Executar o servidor

```
python manage.py runserver
```

---

## Acessos

* Página principal:
  http://127.0.0.1:8000/

* Admin:
  http://127.0.0.1:8000/admin

---

## Como usar

1. Acesse o admin
2. Cadastre os times
3. Visualize na página inicial

---

## Conclusão

O projeto demonstra a criação de uma aplicação web básica com Django, integrando banco de dados, painel administrativo e interface web.
