# ProgWeb — Django Storefront

**Browse products, maintain a session cart, and complete a simulated stock checkout.**

An academic Django storefront with account registration, product pages, filtering, and a server-rendered cart. Checkout updates inventory; it does not charge a payment method or create a durable order ledger.

**Python · Django · SQLite · Server-rendered HTML/CSS**

## Product workflow

1. Browse product listings and details.
2. Register/sign in and add available products to the session cart.
3. Review quantities and totals.
4. Submit checkout: all stock deductions succeed together or roll back.

The existing [hosted link](https://jvmessias.pythonanywhere.com/) has not been checked against the current commit. Use local execution for review.

## Run locally

```bash
git clone https://github.com/joaovitormessias/progweb.git
cd progweb
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Use a Python version compatible with the pinned requirements. Open http://127.0.0.1:8000 and create demo products in `/admin/`. Add images only if you have rights to use them.

## Technical walkthrough

| Area | Code | Decision |
| --- | --- | --- |
| Session cart | [carrinho.py](carrinho/carrinho.py) | Copy nested entries before adding model/Decimal presentation values; stored session data stays JSON serializable |
| Checkout | [views.py](loja/views.py) | Transaction plus conditional stock updates prevents partial checkout and stale-read overselling |
| Mutations | [Cart template](templates/carrinho.html) and views | POST with CSRF protection for add, remove, and checkout |
| Catalogue | [Models](loja/models.py) and [filters](loja/filters.py) | Separate catalogue data and query filtering |

## Verify

Run from the repository root:

```bash
python manage.py check
python manage.py test loja
```

Four regression tests cover rollback when a later item is unavailable, POST-only checkout, JSON-safe cart rendering, and successful stock deduction. They passed on SQLite during review. Concurrent production load and the hosted deployment were not tested.

## Limits and next steps

- Checkout is a simulation: no gateway, order receipt, shipping, refund, or durable purchase record.
- Prices stored in the cart may differ from later catalogue prices; define an explicit pricing policy before real sales.
- Development settings contain a development secret and debug mode. Configure deployment secrets, hosts, HTTPS, backups, and media serving before exposure.
- Add checkout idempotency, persistent orders, and concurrency tests against the intended production database.

[Maintainer](https://github.com/joaovitormessias)
