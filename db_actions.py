from db import Session, Footballstadion


def add_footbalstadion(author, text, price):
    with Session() as session:
        footbalstadion = Footballstadion(author=author, text=text, price=price)
        session.add(footbalstadion)
        session.commit()
        session.refresh(footbalstadion)
        return footbalstadion.id
    

def get_footbalstadion():
    with Session() as session:
        return session.query(Footballstadion).all()
    

def get_footbalstadion():
    with Session() as session:
        return session.query(Footballstadion).where(Footballstadion.id == id).first()


def update_footbalstadion(id, author, text):
    with Session() as session:
        footbalstadion = session.query(Footballstadion).filter_by(id=id).first()
        footbalstadion.author = author
        footbalstadion.text = text
        session.commit()
        return "Дані про стадіон  оновлено"
    
def delete_footbalstadion(id):
    with Session() as session:
        footbalstadion = footbalstadion = session.query(Footballstadion).filter_by(id=id).first()
        session.delete(footbalstadion)
        return  "Cтадіон видалено"