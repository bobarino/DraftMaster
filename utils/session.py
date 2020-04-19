from sqlalchemy.orm import sessionmaker

def load_session(engine):
    Session = sessionmaker(bind=engine)
    session = Session()
    return session
