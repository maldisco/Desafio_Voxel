import requests, random
from sqlalchemy import create_engine, select, func
from sqlalchemy.orm import Session
from sqlalchemy.exc import OperationalError
from db import Products

if __name__ == '__main__':
    # Acesso ao banco de dados 
    engine = create_engine('sqlite:///products.db', echo=False)

    # Calcular preço médio dos smartphones a partir do banco
    with Session(engine) as session:
        query = select(func.avg(Products.Price)).where(Products.Category == 'smartphones')
        try:
            average_price = session.execute(query).scalar()
        except OperationalError:
            print('\033[91mBanco de dados não encontrado. Execute o arquivo db.py para criar.\033[0m')
            exit()
        print('## Resultado da coleta de dados ##')
        print(f'Preço médio dos smartphones: $ {average_price}.')

    # Passo mais importante da solução
    author = ['Stephen Hawking', 'Socrates', 'Machado de Assis', 'Anitta', 'Chuck Norris', 'Schopenhauer']
    citation = requests.get('https://api.chucknorris.io/jokes/random').json()
    print(f'"{citation["value"]}" -{random.choice(author)}')