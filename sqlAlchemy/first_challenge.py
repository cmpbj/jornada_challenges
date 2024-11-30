# This script aims to create two tables in the database
# The first table is called "suppliers" and has the following columns: id, nome, telefone, email and endereco
# The second table is called "products" and has the following columns: id, nome, descricao, preco, fornecedor_id

# the first step is to import the necessary libraries
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.exc import SQLAlchemyError 

Base = declarative_base()

class Supplier(Base):
    __tablename__ = 'suppliers'
    id = Column(Integer, primary_key=True)
    nome = Column(String(50), nullable=False)
    telefone = Column(String(20))
    email = Column(String(50))
    endereco = Column(String(100))

class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    nome = Column(String(50), nullable=False)
    descricao = Column(String(200))
    preco = Column(Float)
    fornecedor_id = Column(Integer, ForeignKey('suppliers.id'))
    fornecedor = relationship("Supplier")

engine = create_engine('sqlite:///first_challenge.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)


try:
    with Session() as session:
        suppliers = [
            Supplier(nome="Fornecedor A", telefone="12345678", email="contato@a.com", endereco="Endereço A"),
            Supplier(nome="Fornecedor B", telefone="87654321", email="contato@b.com", endereco="Endereço B"),
            Supplier(nome="Fornecedor C", telefone="12348765", email="contato@c.com", endereco="Endereço C"),
            Supplier(nome="Fornecedor D", telefone="56781234", email="contato@d.com", endereco="Endereço D"),
            Supplier(nome="Fornecedor E", telefone="43217865", email="contato@e.com", endereco="Endereço E")
        ]
        session.add_all(suppliers)
        session.commit()
except SQLAlchemyError as e:
    print(f"Error when inserting suppliers: {e}")


try:
    with Session() as session:
        products = [
            Product(nome="Produto 1", descricao="Descrição do Produto 1", preco=100.5, fornecedor_id=1),
            Product(nome="Produto 2", descricao="Descrição do Produto 2", preco=200.20, fornecedor_id=2),
            Product(nome="Produto 3", descricao="Descrição do Produto 3", preco=300.35, fornecedor_id=3),
            Product(nome="Produto 4", descricao="Descrição do Produto 4", preco=415.10, fornecedor_id=4),
            Product(nome="Produto 5", descricao="Descrição do Produto 5", preco=500, fornecedor_id=5)
        ]
        session.add_all(products)
        session.commit()
except SQLAlchemyError as e:
    print(f"Error when inserting products: {e}")
