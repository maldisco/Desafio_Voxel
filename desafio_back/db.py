import requests
from sqlalchemy import String, create_engine
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase, Session

class Base(DeclarativeBase):
    pass

class Products(Base):
    __tablename__ = "products"

    Id: Mapped[int] = mapped_column(primary_key=True)
    Title: Mapped[str] = mapped_column(String(30))
    Category: Mapped[str] = mapped_column()
    Price: Mapped[float] = mapped_column()

    def __repr__(self):
        return f"Products(Id={self.Id}, Title={self.Title}, Category={self.Category}, Price={self.Price})"

if __name__ == '__main__':
    # Coleta de dados
    products = requests.get('https://dummyjson.com/products').json()['products']
    engine = create_engine('sqlite:///products.db', echo=True)

    # Criação da tabela (só executar uma vez)
    Products.metadata.create_all(engine)

        # Inserção de produtos no banco de dados
    with Session(engine) as session:
        for product in products:
            new_product = Products(Id=product['id'], Title=product['title'], Category=product['category'], Price=product['price'])
            session.add(new_product)
            
        session.commit()