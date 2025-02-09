from src.PGSQLContext import PGDataHandler

if __name__ == "__main__":
    dh = PGDataHandler()
    print(dh.get_all_employees())
