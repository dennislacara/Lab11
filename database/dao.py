from database.DB_connect import DBConnect
from model.dto.connessione_dto import ConnessioneDTO
from model.dto.rifugio_dto import RifugioDTO


class DAO:
    """
        Implementare tutte le funzioni necessarie a interrogare il database.
        """
    @staticmethod
    def get_all_rifugi():
        try:
            conn = DBConnect.get_connection()
        except Exception as e:
            print(e)

        result = {}
        cursor = conn.cursor(dictionary=True)
        query = """
            SELECT *
            FROM rifugio r
            """
        cursor.execute(query)

        for row in cursor:
            oggetto_rifugio = RifugioDTO(**row)
            result[row['id']] = oggetto_rifugio
            #print(oggetto_rifugio)

        cursor.close()
        conn.close()

        return result

    @staticmethod
    def get_connessioni(anno_limite):

        try:
            conn = DBConnect.get_connection()
        except Exception as e:
            print(e)

        result =[]
        cursor = conn.cursor(dictionary=True)
        query = """
                SELECT *
                FROM connessione c 
                WHERE c.anno <= %s
                """
        cursor.execute(query, (anno_limite,))
        for row in cursor:
            oggetto_connessione = ConnessioneDTO(**row)
            result.append(oggetto_connessione)
            #print(oggetto_connessione)
        cursor.close()
        conn.close()

        return result
    # TODO


