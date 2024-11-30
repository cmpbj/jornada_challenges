# Supplier and Product Management with SQLAlchemy

This project is part of the **Jornada de Dados** course by Luciano Galvão and demonstrates the use of **SQLAlchemy**, a powerful SQL toolkit and Object-Relational Mapping (ORM) library for Python. The project is divided into two main parts:

1. **Creating and populating tables for suppliers and products.**
2. **Performing a SQL query to calculate and display the total price of products supplied by each supplier.**

## Project Structure

### `create_tables_and_insert_data.py`
This script:
- Creates an SQLite database named `first_challenge.db`.
- Defines two tables:
  - **suppliers**: Stores supplier details (nome, telefone, e-mail e endereço).
  - **products**: Stores product details (nome, descrição, preço and a foreing key related to the supplier).
- Inserts sample data into both tables.

### `query_data.py`
This script:
- Connects to the `first_challenge.db` database.
- Executes a SQL query to join the `products` and `suppliers` tables, grouping data by supplier and calculating the total price of products.
- Outputs the results in a user-friendly format.

---

## How to Run the Project

### Prerequisites
- **Python 3.10 or later** installed.
- **Poetry** for dependency management. Install Poetry via:
  ```bash
  pip install poetry

```markdown
## Installation

### Clone the Repository:
```bash
git clone <repository_url>
cd <repository_folder>
```

### Install Dependencies Using Poetry:
```bash
poetry install
```

---

## Steps to Run

### Activate the Poetry Shell:
```bash
poetry shell
```

### Run the `first_challenge.py` Script to Set Up the Database:
```bash
poetry run python first_challenge.py
```

### Run the `query_challenge.py` Script to Perform the SQL Query and View Results:
```bash
python query_challenge.py
```

---

## Project Details

### Database Design

#### **suppliers** Table:
- **id**: Integer, Primary Key.
- **nome**: Supplier name.
- **telefone**: Supplier phone.
- **email**: Supplier email.
- **endereco**: Supplier address.

#### **products** Table:
- **id**: Integer, Primary Key.
- **nome**: Product name.
- **descricao**: Product description.
- **preco**: Product price.
- **fornecedor_id**: Foreign key referencing the suppliers table.

### Relationships
The **products** table references the **suppliers** table using the `fornecedor_id` foreign key, creating a one-to-many relationship between suppliers and products.

---

## SQL Query Explained

The SQL query in `query_data.py`:
```sql
SELECT 
    suppliers.nome AS fornecedor,
    SUM(products.preco) AS total_preco
FROM products
INNER JOIN suppliers ON products.fornecedor_id = suppliers.id
GROUP BY suppliers.nome;
```
- Joins the **products** table with **suppliers** on their foreign key relationship.
- Groups products by supplier.
- Calculates the total price of all products for each supplier.

### Example Output:
```text
Fornecedor: Fornecedor A, Total Preço: 100.5
Fornecedor: Fornecedor B, Total Preço: 200.2
```

---

## About the Course

This project is a hands-on exercise in the **Jornada de Dados**, a course designed by Luciano Galvão to teach fundamental and advanced data concepts. The activities focus on applying database concepts, Python programming, and SQL queries in practical scenarios.
```