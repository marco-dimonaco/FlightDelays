from database.DB_connect import DBConnect
from model.airport import Airport
from model.connessione import Connessione


class DAO:
    @staticmethod
    def getAllAirports():
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """SELECT * from airports a order by a.AIRPORT asc"""
        cursor.execute(query)
        for row in cursor:
            result.append(Airport(**row))
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAeroportiMinCompagnie(minimo):
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """
                SELECT tmp.*
                FROM (SELECT a.*
                      FROM airports a , flights f 
                      WHERE a.ID = f.ORIGIN_AIRPORT_ID OR a.ID = f.DESTINATION_AIRPORT_ID 
                      GROUP BY a.ID , a.IATA_CODE , f.AIRLINE_ID
                      ) as tmp
                GROUP BY tmp.ID
                HAVING COUNT(*) >= %s
                """
        cursor.execute(query, (minimo,))
        for row in cursor:
            if row is not None:
                result.append(Airport(**row))
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllConnessioni(idMap):
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """
                SELECT a1.ID as A1, a2.ID as A2, count(*) as Peso
                FROM airports a1, airports a2, flights f 
                WHERE (f.ORIGIN_AIRPORT_ID = a1.ID AND f.DESTINATION_AIRPORT_ID = a2.ID)
                OR (f.ORIGIN_AIRPORT_ID = a2.ID AND f.DESTINATION_AIRPORT_ID = a1.ID)
                GROUP BY a1.ID, a2.ID
                """
        cursor.execute(query)
        for row in cursor:
            if row is not None:
                result.append(Connessione(idMap[row['A1']], idMap[row['A2']], row['Peso']))
        cursor.close()
        conn.close()
        return result
