import psycopg2

def main():
    """psycopg2 2.8.6でCOPYの動作を確認
    """
    schema = ""
    table_name = ""
    import_file = "test.csv"
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.copy_from(file=import_file, table=f"{schema}.{table_name}", sep=",")

def get_connection():
    dsn = {
        "host":"localhost",
        "port":"5432",
        "database":"test_db",
        "user":"postgres",
        "password":"postgres",
    }
    return psycopg2.connect(**dsn)

if __name__ == "__main__":
    main()
