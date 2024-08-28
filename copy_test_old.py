import psycopg2

def main():
    """psycopg2 2.8.6でCOPYの動作を確認
    """
    schema = "sub_schema"
    table_name = "users"
    with get_connection() as conn:
        with conn.cursor() as cur:
            with open(r"input_file\user_list.csv", mode="r", encoding="utf-8") as f:
                cur.copy_from(f, table=f"{schema}.{table_name}", sep=",", columns=('name', 'email'))
                conn.commit()

def get_connection():
    dsn = {
        "host":"localhost",
        "port":"5432",
        "database":"copy_test",
        "user":"postgres",
        "password":"postgres",
    }
    return psycopg2.connect(**dsn)

if __name__ == "__main__":
    main()