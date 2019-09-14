import psycopg2

try:
    conn = psycopg2.connect("dbname='luckakapetanija' user='mauro' host='localhost' password='admin'")
    print("Database connected")

    cursor= conn.cursor()
    ######################################################## KORISNICI
    cursor.execute("""
        CREATE TABLE Users(
            userid serial PRIMARY KEY,
            fname varchar (50) NOT NULL,
            sname varchar (50) NOT NULL,
            username varchar (50) UNIQUE,
            email varchar (50) UNIQUE,
            password varchar (50),
            isadmin BOOLEAN NOT NULL DEFAULT FALSE,
            createdon TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            ispostava varchar (50),
            kontakt varchar (15),
            isblocked BOOLEAN NOT NULL DEFAULT FALSE,
            isdeleted BOOLEAN NOT NULL DEFAULT FALSE)
    """
    )
######################################################################## PRIJAVA DOLASKA
    cursor.execute("""
        CREATE TABLE prijavad_form1(
            id_pd serial PRIMARY KEY,
            ispostava_pd varchar (50),
            date_pd varchar (50),
            oznaka_pd varchar (50),
            duzina_pd integer (50),
            vrstaplovila_pd varchar (50),
            kontakt_pd integer (50),
            lukad varchar (50),
            ime_pd varchar (50),
            prezime_pd varchar (50),
            brojclanova_pd integer (50),
            username_pd varchar (50) REFERENCES USERS (username),
            createdon TIMESTAMP DEFAULT CURRENT_TIMESTAMP)
    """
    )
    ############################################################################ PRIJAVA ODLASKA
    cursor.execute("""
        CREATE TABLE prijavaod_form2(
            id_po serial PRIMARY KEY,
            ispostava_po varchar (50),
            date_po varchar (50),
            oznaka_po varchar (50),
            duzina_po integer (50),
            vrstaplovila_po varchar (50),
            kontakt_po integer (50),
            lukao varchar (50),
            ime_po varchar (50),
            prezime_po varchar (50),
            brojclanova_po integer (50),
            napomena_po varchar (100),
            username_pd varchar (50) REFERENCES USERS (username),
            createdon TIMESTAMP DEFAULT CURRENT_TIMESTAMP)
    """
     )
     ######################################################################## PRIJAVA DOMACINA
    cursor.execute("""
        CREATE TABLE prijavado_form3(
            id_do serial PRIMARY KEY,
            serijskibrojd varchar (50),
            datum_od varchar (50),
            datum_do varchar (50),
            nacindolaskad varchar (50),
            imeplovilad varchar (50),
            vrstaplovilad varchar (50),
            oznakad varchar (50),
            duljinad integer (50),
            drzava varchar (50),
            brojclanovad integer (50),
            imed varchar (50),
            prezimed varchar (50),
            kontaktd varchar (50),
            obracund float (50),
            username_pd varchar (50) REFERENCES USERS (username),
            createdon TIMESTAMP DEFAULT CURRENT_TIMESTAMP)
    """
    )
    ######################################################################## PRIJAVA GOSTA
    cursor.execute("""
        CREATE TABLE prijavago_form4(
            id_go serial PRIMARY KEY,
            serijskibrojg varchar (50),
            datumg_od varchar (50),
            datumg_do varchar (50),
            nacindolaskag varchar (50),
            imeplovilag varchar (50),
            vrstaplovilag varchar (50),
            oznakag varchar (50),
            duljinag integer (50),
            drzavag varchar (50),
            brojclanovag integer (50),
            imeg varchar (50),
            prezimeg varchar (50),
            kontaktg varchar (50),
            obracung float (50),
            username_pd varchar (50) REFERENCES USERS (username),
            createdon TIMESTAMP DEFAULT CURRENT_TIMESTAMP)
    """
    )
################################################################# DODAVANJE ADMINA
    cursor.execute(
        """INSERT INTO USERS(fname, sname, username, email, password, kontakt, isadmin, ispostava) VALUES
        ('Mauro', 'Buric', 'mburic', 'mauro.buric@gmail.com', '12345', '0925354352', True, 'LiRovinj')""")

############################################### potvrda promjena u bazi
    conn.commit()
    print("Tablice uspjesno kreirane")
    print("Vrijednosti uspjesno dodane")

except:
        print("Database not connected")
