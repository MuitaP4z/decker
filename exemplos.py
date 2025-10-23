from django.db import connection

# Exemplo de Cursor
def executar_sql_personalizado():
    with connection.cursor() as cursor:
        # Exemplo: inserir uma linha diretamente
        cursor.execute("""
            INSERT INTO mtgmanager_deck (nome, formato) 
            VALUES (%s, %s)
        """, ['Deck Raw', 'Commander'])
        
        # Ler resultados de uma consulta
        cursor.execute("SELECT id, nome FROM mtgmanager_deck")
        linhas = cursor.fetchall()
        for row in linhas:
            print(row[0], row[1])

# Exemplo de Stored Procedure utilizando o PostgreSQL
def chamar_meu_stored_procedure(deck_id, carta_id, qty):
    with connection.cursor() as cursor:
        cursor.callproc('adicionar_carta_ao_deck', [deck_id, carta_id, qty])