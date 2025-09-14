from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Password: Jaan%9009 (encoded)
DATABASE_URL = "mysql+pymysql://root:Jaan9009@localhost:3306/mydatabase"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = declarative_base()

# from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker

# # Use SQLite for development
# DATABASE_URL = "sqlite:///./test.db"

# engine = create_engine(
#     DATABASE_URL, connect_args={"check_same_thread": False}
# )
# SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
# Base = declarative_base()
