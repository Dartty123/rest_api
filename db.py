from sqlalchemy import String, create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker, Mapped,mapped_column


engine = create_engine("sqlite:///footbalstadion.db")
Session = sessionmaker(bind=engine)


class Base(DeclarativeBase):
    pass


def create_db():
    Base.metadata.create_all(bind=engine)


class Footballstadion(Base):
    __tablename__ = "footballstadion"

    id: Mapped[int] = mapped_column (primary_key=True)
    author: Mapped[str] = mapped_column(String(100))
    text: Mapped[str] = mapped_column(String())
    price:Mapped[str] = mapped_column(String())