

# 🛍️ ProgWeb — E-commerce em Django

Um projeto de e-commerce completo desenvolvido com **Django 5**, focado em boas práticas, arquitetura modular e integração simplificada com ambientes de deploy (ex: **PythonAnywhere**).

---

## 📑 Sumário

- [Visão Geral](#visão-geral)
- [Arquitetura do Projeto](#arquitetura-do-projeto)
- [Principais Recursos](#principais-recursos)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Estrutura de Pastas](#estrutura-de-pastas)
- [Configuração e Execução Local](#configuração-e-execução-local)
- [Deploy no PythonAnywhere](#deploy-no-pythonanywhere)
- [Boas Práticas e Padrões](#boas-práticas-e-padrões)
- [Licença](#licença)

---

## 🧠 Visão Geral

Este projeto implementa uma **loja virtual funcional**, com fluxo completo de cadastro, autenticação, listagem de produtos, carrinho de compras e finalização de pedido.

A aplicação foi estruturada para ser escalável, com separação clara entre as camadas de **negócio, templates, estáticos e rotas**, seguindo os padrões do Django.

---

## 🧩 Arquitetura do Projeto

O projeto é dividido em múltiplos apps independentes:

| App | Função |
|------|--------|
| **core** | Configurações principais e roteamento global |
| **loja** | Lógica e exibição de produtos |
| **carrinho** | Gerenciamento do carrinho de compras via sessão |
| **conta** | Registro, login e gerenciamento de usuários |
| **templates** | Estrutura de HTMLs e partials reutilizáveis |
| **static** | Recursos estáticos (CSS, JS, imagens) |

---

## 🚀 Principais Recursos

- 🔐 **Autenticação de usuários** (login, registro, logout)
- 🛒 **Carrinho de compras persistente** via sessão
- 🧾 **Listagem e detalhamento de produtos**
- 💳 **Checkout e fluxo de compra completo**
- 🖥️ **Interface responsiva com CSS modular**
- ⚙️ **Filtros e paginação com `django-filter`**
- 🧰 **Pronto para deploy em PythonAnywhere**

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.13**
- **Django 5.2.5**
- **SQLite** (para ambiente local)
- **django-filter**
- **HTML5 / CSS3 (modularizado)**
- **Gunicorn + WSGI** (deploy)

---

## 📂 Estrutura de Pastas

```bash
progweb/
├── carrinho/
├── conta/
├── core/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── loja/
├── media/
├── static/
│   └── css/
│       └── styles.css
├── templates/
│   ├── base.html
│   ├── lista_produtos.html
│   ├── produto_detail.html
│   └── ...
├── manage.py
└── requirements.txt
```

---

## ⚙️ Configuração e Execução Local

### 1️⃣ Clonar o repositório
```bash
git clone https://github.com/joaovitormessias/progweb.git
cd progweb
```

### 2️⃣ Criar e ativar o ambiente virtual
```bash
python -m venv venv
source venv/bin/activate  # Linux / Mac
venv\Scripts\activate     # Windows
```

### 3️⃣ Instalar dependências
```bash
pip install -r requirements.txt
```

### 4️⃣ Aplicar migrações e rodar o servidor
```bash
python manage.py migrate
python manage.py runserver
```

Acesse em **http://127.0.0.1:8000/**

---

## ☁️ Deploy no PythonAnywhere

### Estrutura esperada
```
/home/usuario/progweb/
    ├── core/
    ├── loja/
    ├── carrinho/
    ├── conta/
    ├── static/
    ├── templates/
    ├── manage.py
```

### Configurações importantes

#### `core/settings.py`
```python
ALLOWED_HOSTS = ['seuusuario.pythonanywhere.com']

STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
```

#### Coletar arquivos estáticos
```bash
python manage.py collectstatic
```

#### Mapeamento no painel
| URL | Diretório |
|------|------------|
| `/static/` | `/home/usuario/progweb/staticfiles` |
| `/media/` | `/home/usuario/progweb/media` |

---

## 🧭 Boas Práticas e Padrões

- Estrutura modular de apps → facilita manutenção e escalabilidade  
- Padrão **MVC** (Model-View-Template) aplicado corretamente  
- Templates DRY (uso de `{% include %}` e `partials`)  
- Context processors para dados globais (como o carrinho)  
- Configurações de produção separadas por ambiente (via WSGI e variáveis)  
- CSS organizado e carregado via `{% static %}`  

---

## 🪪 Licença

Este projeto é distribuído sob a licença **MIT**.  
Sinta-se livre para usar, modificar e contribuir.  

link do site : [link](https://jvmessias.pythonanywhere.com/)
