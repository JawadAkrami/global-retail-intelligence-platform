

from sqlalchemy import create_engine

from src.config.settings import DB_CONFIG

connection_string = (
    f"mysql+pymysql://"
    f"{DB_CONFIG['user']}:"
    f"{DB_CONFIG['password']}@"
    f"{DB_CONFIG['host']}:"
    f"{DB_CONFIG['port']}/"
    f"{DB_CONFIG['database']}"
)

engine = create_engine(connection_string)