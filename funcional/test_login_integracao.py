from testcontainers.postgres import PostgresContainer
import psycopg2

def test_postgres_integration():
    with PostgresContainer("postgres:13") as postgres:
        # Pegue as credenciais geradas pelo container
        conn = psycopg2.connect(
            host=postgres.get_container_host_ip(),
            port=postgres.get_exposed_port(5432),
            user=postgres.USERNAME,
            password=postgres.PASSWORD,
            dbname=postgres.DATABASE,
        )
        
        # Criar um cursor para executar comandos SQL
        cursor = conn.cursor()

        # Executar uma query de teste
        cursor.execute("CREATE TABLE teste (id SERIAL PRIMARY KEY, nome VARCHAR(50));")
        cursor.execute("INSERT INTO teste (nome) VALUES ('Test User');")
        cursor.execute("SELECT * FROM teste;")

        # Verificar os resultados
        result = cursor.fetchone()
        assert result[1] == 'Test User'

        # Fechar a conexão
        cursor.close()
        conn.close()

if __name__ == "__main__":
    test_postgres_integration()
