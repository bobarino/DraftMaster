#from genetic_algorithm import GeneticAlgorithm
from db_engine import DBEngine
from models.mlb_main import MLB

def main():
    #dk = DraftKings()
    #ga = GeneticAlgorithm(dk)
    mlb = MLB()
    leagues = [mlb]
    db = DBEngine('hi.sqlite', leagues)
    db.create_tables()
    db.fill_tables()
    print("success")

if __name__ == '__main__':
    main()
