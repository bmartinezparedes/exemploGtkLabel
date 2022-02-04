import sqlite3 as dbapi

'''
print(dbapi.apilevel)     #para ver version de la api
print(dbapi.threadsafety) #nos indica la facilidad de uso de hilos 0 no se sincroniza, 1 compartir modulo pero no
                          #compartir conexiones 2 se comparten modulos y conexiones y 3 permite to-do
print(dbapi.paramstyle)   #Utiliza el ? para evitar el injection sql
'''

"""
Standar Error
    warning
    Error
        Inteface Error
        DataBase Error
            Data Error
            Operational Error
            Integrity Error
            Internal Error
            Programing Error
            Not Supported Error
"""

try:
    bbdd = dbapi.connect("baseDatos.dat")
    cursor = bbdd.cursor()
    # cursor.execute("CREATE TABLE usuarios (dni text,nome text, direccion text)")
    # cursor.execute("INSERT INTO usuarios VALUES('54427746V','Brais Martinez Paredes','Avd Portanet')")
    # bbdd.commit()
    # cursor.execute("INSERT INTO usuarios VALUES('69696969S','Joel Nunes','Matama')")
    # bbdd.commit()
    cursor.execute("SELECT * FROM usuarios")
    for rexistro in cursor.fetchall():
        print("Nombre: " + rexistro[1] + ", DNI: " + rexistro[0] + " Direccion: " + rexistro[2])
    # SQL injection
    # dni= "54427746V' or ''='"
    dni = "54427746V"
    cursor.execute("SELECT * FROM usuarios WHERE dni='" + dni + "'")
    for usuario in cursor.fetchall():
        print(usuario)
    # solucion para SQL injection
    cursor.execute("SELECT * FROM usuarios WHERE dni=?", (dni,))
    for usuario in cursor.fetchall():
        print(usuario)
except dbapi.DatabaseError as e:
    print("Erro na base de datos: " + str(e))
