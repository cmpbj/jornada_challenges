from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from sqlalchemy import func
from first_challenge import Supplier, Product

engine = create_engine('sqlite:///first_challenge.db')
Session = sessionmaker(bind=engine)
session = Session()

# Another way tho query the database
# with engine.connect() as connection:
#     results = connection.execute(text('''
#         SELECT 
#             suppliers.nome AS fornecedor,
#             SUM(products.preco) AS total_preco
#         FROM products
#         INNER JOIN suppliers ON products.fornecedor_id = suppliers.id
#         GROUP BY suppliers.nome
#     '''))

results = session.query(
    Supplier.nome.label('fornecedor'),
    func.sum(Product.preco).label('total_preco')
).join(
    Product, Product.fornecedor_id == Supplier.id
).group_by(Supplier.nome).all()

for row in results:
    print(f"Fornecedor: {row.fornecedor}, Total Preço: {row.total_preco}")
