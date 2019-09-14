import psycopg2
import psycopg2.extras

from psycopg2 import IntegrityError, OperationalError

connect_str = "dbname='luckakapetanija' user='mauro' host='localhost' password='admin'"

# Table Get - prijavad
def get_prijavad_form1():
    #print("In FormHelper:: get_prijavad_form1")
    conn = psycopg2.connect(connect_str)
    
    cursor = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    #execute query
    cursor.execute(
        "select date_pd, oznaka_pd, duzina_pd, vrstaplovila_pd, kontakt_pd, lukad, ime_pd, prezime_pd, brojclanova_pd, id_pd from prijavad_form1")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()

    return rows

# Table Get - prijavaod
def get_prijavaod_form2():
    #print("In FormHelper:: get_prijavaod_form2")
    conn = psycopg2.connect(connect_str)
    
    cursor = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

    cursor.execute("select date_po, oznaka_po, duzina_po, vrstaplovila_po, kontakt_po, lukao, ime_po, prezime_po, napomena_po, brojclanova_po, id_po from prijavaod_form2;")
    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    return rows

# Table Get - prijavado
def get_prijavado_form3():
    #print("In FormHelper:: get_prijavado_form3")
    conn = psycopg2.connect(connect_str)
    
    cursor = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

    cursor.execute("select serijskibrojd, datum_od, datum_do, nacindolaskad, imeplovilad, vrstaplovilad, oznakad, duljinad, brojclanovad, imed, prezimed, kontaktd, obracund, id_do from prijavado_form3;")
    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    return rows

def countPrijave ():
    #table 3 and table 4 rows count
    conn = psycopg2.connect(connect_str)

    cursor = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

    cursor.execute(
        'SELECT (SELECT COUNT(*) FROM prijavado_form3) AS T1, (SELECT COUNT(*) FROM prijavago_form4) AS T2')
    rows= cursor.fetchall()

    cursor.close()
    conn.close()

    return rows

# Table Get - prijavago
def get_prijavago_form4():
    #print("In FormHelper:: get_prijavago_form4")
    conn = psycopg2.connect(connect_str)
    
    cursor = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

    cursor.execute("select serijskibrojg, datumg_od, datumg_do, nacindolaskag, imeplovilag, vrstaplovilag, oznakag, duljinag, brojclanovag, imeg, prezimeg, kontaktg, obracung, id_go from prijavago_form4;")
    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    return rows

# Table Insert - prijavad
def insert_prijavad_form1(ispostava_pd, date_pd, oznaka_pd, duzina_pd, vrstaplovila_pd, kontakt_pd, lukad, ime_pd, prezime_pd, brojclanova_pd, username_pd):
    #print("In FormHelper:: insert_prijavad_form1")

    conn = psycopg2.connect(connect_str)
    cursor = conn.cursor()

    insertQuery = "INSERT INTO prijavad_form1(ispostava_pd, date_pd, oznaka_pd, duzina_pd, vrstaplovila_pd, kontakt_pd, lukad, ime_pd, prezime_pd, brojclanova_pd, username_pd) VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}');".format(
        ispostava_pd, date_pd, oznaka_pd, duzina_pd, vrstaplovila_pd, kontakt_pd, lukad, ime_pd, prezime_pd, brojclanova_pd, username_pd)

    cursor.execute(insertQuery)
    conn.commit()

    cursor.close()
    conn.close()

    return True

# Table Insert - prijavaod
def insert_prijavaod_form2(ispostava_po, date_po, oznaka_po, duzina_po, vrstaplovila_po, kontakt_po, lukao, ime_po, prezime_po, brojclanova_po, napomena_po, username_pd):
    print("In FormHelper:: insert_prijavaod_form2")

    conn = psycopg2.connect(connect_str)
    cursor = conn.cursor()

    insertQuery = "INSERT INTO prijavaod_form2(ispostava_po, date_po, oznaka_po, duzina_po, vrstaplovila_po, kontakt_po, lukao, ime_po, prezime_po, brojclanova_po, napomena_po, username_pd) VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}');".format(ispostava_po, date_po, oznaka_po, duzina_po, vrstaplovila_po, kontakt_po, lukao, ime_po, prezime_po, brojclanova_po,napomena_po, username_pd)

    cursor.execute(insertQuery)
    conn.commit()

    cursor.close()
    conn.close()

    return True

# Table Insert - prijavado
def insert_prijavado_form3(serijskibrojd, datum_od, datum_do,  nacindolaskad, imeplovilad, vrstaplovilad, oznakad, duljinad, drzava, brojclanovad, imed, prezimed, kontaktd, obracund,  username_pd):
    #print("In FormHelper:: insert_prijavado_form3")

    conn = psycopg2.connect(connect_str)
    cursor = conn.cursor()

    insertQuery = "INSERT INTO prijavado_form3(serijskibrojd, datum_od, datum_do,  nacindolaskad, imeplovilad, vrstaplovilad, oznakad, duljinad, drzava, brojclanovad, imed, prezimed, kontaktd, obracund,  username_pd) VALUES ('{}','{}','{}','{}','{}', '{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(serijskibrojd, datum_od, datum_do,  nacindolaskad, imeplovilad, vrstaplovilad, oznakad, duljinad, drzava, brojclanovad, imed, prezimed, kontaktd, obracund,  username_pd)

    cursor.execute(insertQuery)
    conn.commit()

    cursor.close()
    conn.close()

    return True

# Table Insert - prijavago
def insert_prijavago_form4(serijskibrojg, datumg_od, datumg_do,  nacindolaskag, imeplovilag, vrstaplovilag, oznakag, duljinag, brojclanovag, imeg, prezimeg, kontaktg, obracung,  username_pd):
    #print("In FormHelper:: insert_prijavago_form4")

    conn = psycopg2.connect(connect_str)
    cursor = conn.cursor()

    insertQuery = "INSERT INTO prijavago_form4(serijskibrojg, datumg_od, datumg_do,  nacindolaskag, imeplovilag, vrstaplovilag, oznakag, duljinag, brojclanovag, imeg, prezimeg, kontaktg, obracung,  username_pd) VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}');".format(serijskibrojg, datumg_od, datumg_do,  nacindolaskag, imeplovilag, vrstaplovilag, oznakag, duljinag, brojclanovag, imeg, prezimeg, kontaktg, obracung,  username_pd)
    cursor.execute(insertQuery)
    conn.commit()

    cursor.close()
    conn.close()

    return True

# Table Delete - prijavad
def delete_prijavad_form1(username_pd, id_pd):
    #print("In FormHelper:: delete_prijavad_form1")
    conn = psycopg2.connect(connect_str)
    
    cursor = conn.cursor()
    
    updateQuery = "Delete from prijavad_form1 where id_pd = {} and username_pd = '{}';".format(id_pd, username_pd) 
    cursor.execute(updateQuery)
    conn.commit()
    updated_rows = cursor.rowcount
    cursor.close()
    conn.close()

    return updated_rows > 0 and True or False

# Table Delete - prijavaod
def delete_prijavaod_form2(username_pd, id_po):
    #print("In FormHelper:: delete_prijavaod_form2")
    conn = psycopg2.connect(connect_str)
    
    cursor = conn.cursor()
    
    updateQuery = "Delete from prijavaod_form2 where id_po = {} and username_pd = '{}';".format(id_po, username_pd) 
    cursor.execute(updateQuery)
    conn.commit()
    updated_rows = cursor.rowcount
    cursor.close()
    conn.close()

    return updated_rows > 0 and True or False

# Table Delete - prijavado
def delete_prijavado_form3(username_pd, id_do):
    #print("In FormHelper:: delete_prijavado_form3")
    conn = psycopg2.connect(connect_str)
    
    cursor = conn.cursor()
    
    updateQuery = "Delete from prijavado_form3 where id_do = {} and username_pd = '{}';".format(id_do, username_pd) 
    cursor.execute(updateQuery)
    conn.commit()
    updated_rows = cursor.rowcount
    cursor.close()
    conn.close()

    return updated_rows > 0 and True or False

# Table Delete - prijavago
def delete_prijavago_form4(username_pd, id_go):
    #print("In FormHelper:: delete_prijavago_form4")
    conn = psycopg2.connect(connect_str)
    
    cursor = conn.cursor()
    
    updateQuery = "Delete from prijavago_form4 where id_go = {} and username_pd = '{}';".format(id_go, username_pd) 
    cursor.execute(updateQuery)
    conn.commit()
    updated_rows = cursor.rowcount
    cursor.close()
    conn.close()

    return updated_rows > 0 and True or False

# Table Update - prijavad
def update_prijavad_form1(id_pd ,ispostava_pd, date_pd, oznaka_pd, duzina_pd, vrstaplovila_pd, kontakt_pd, lukad, ime_pd, prezime_pd, brojclanova_pd, username_pd):
    #print("In FormHelper:: Update_prijavad_form1")

    conn = psycopg2.connect(connect_str)
    cursor = conn.cursor()
    
    updateQuery = "UPDATE prijavad_form1 SET ispostava_pd = '{}', date_pd = '{}', oznaka_pd = '{}', duzina_pd = '{}', vrstaplovila_pd = '{}', kontakt_pd = '{}', lukad = '{}', ime_pd = '{}', prezime_pd = '{}', brojclanova_pd = '{}'  where username_pd = '{}' and id_pd = {};".format(ispostava_pd, date_pd, oznaka_pd, duzina_pd, vrstaplovila_pd, kontakt_pd, lukad, ime_pd, prezime_pd, brojclanova_pd, username_pd, id_pd)
    #print(updateQuery)
    
    cursor.execute(updateQuery)
    conn.commit()
    updated_rows = cursor.rowcount

    cursor.close()
    conn.close()
    return updated_rows > 0 and True or False

# Table Update - prijavaod
def update_prijavaod_form2(id_po, ispostava_po, date_po, oznaka_po, duzina_po, vrstaplovila_po, kontakt_po, lukao, ime_po, prezime_po, brojclanova_po, napomena_po, username_pd):
    #print("In FormHelper:: update_prijavaod_form2")

    conn = psycopg2.connect(connect_str)
    cursor = conn.cursor()

    updateQuery = "UPDATE prijavaod_form2 SET ispostava_po = '{}', date_po = '{}', oznaka_po = '{}', duzina_po = '{}', vrstaplovila_po = '{}', kontakt_po = '{}', lukao = '{}', ime_po = '{}', prezime_po = '{}', brojclanova_po = '{}', napomena_po = '{}'  where username_pd = '{}' and id_po = {};".format(ispostava_po, date_po, oznaka_po, duzina_po, vrstaplovila_po, kontakt_po, lukao, ime_po, prezime_po, brojclanova_po, napomena_po, username_pd, id_po)
    
    cursor.execute(updateQuery)
    conn.commit()

    cursor.close()
    conn.close()

    return True

# Table Update - prijavado
def update_prijavado_form3(id_po, serijskibrojd, datum_od, datum_do,  nacindolaskad, imeplovilad, vrstaplovilad, oznakad, duljinad, drzava, brojclanovad, imed, prezimed, kontaktd, obracund, username_pd):
    #print("In FormHelper:: update_prijavado_form3")

    conn = psycopg2.connect(connect_str)
    cursor = conn.cursor()

    updateQuery = "UPDATE prijavado_form3 SET serijskibrojd = '{}', datum_od = '{}', datum_do = '{}', nacindolaskad = '{}', imeplovilad = '{}', vrstaplovilad='{}' , oznakad = '{}', duljinad = '{}', drzava = '{}', brojclanovad = '{}', imed = '{}', prezimed = '{}', kontaktd = '{}', obracund = '{}'  where username_pd = '{}' and id_do = {};".format(serijskibrojd, datum_od, datum_do, nacindolaskad, imeplovilad, vrstaplovilad, oznakad, duljinad, drzava, brojclanovad, imed, prezimed, kontaktd, obracund, username_pd, id_po)
    
    cursor.execute(updateQuery)
    conn.commit()

    cursor.close()
    conn.close()

    return True

# Table Update - prijavago
def update_prijavago_form4(id_go, serijskibrojg, datumg_od, datumg_do,  nacindolaskad, imeplovilag, vrstaplovilag, oznakag, duljinag, brojclanovag, imeg, prezimeg, kontaktg, obracung, username_pd):
    #print("In FormHelper:: prijavago_form4")

    conn = psycopg2.connect(connect_str)
    cursor = conn.cursor()

    updateQuery = "UPDATE prijavago_form4 SET serijskibrojg = '{}', datumg_od = '{}', datumg_do = '{}', nacindolaskad = '{}', imeplovilag = '{}', vrstaplovilag='{}' , oznakag = '{}', duljinag = '{}', brojclanovag = '{}', imeg = '{}', prezimeg = '{}', kontaktg = '{}', obracung = '{}' where username_pd = '{}' and id_go = {};".format(serijskibrojg, datumg_od, datumg_do, nacindolaskad, imeplovilag, vrstaplovilag, oznakag, duljinag, brojclanovag, imeg, prezimeg, kontaktg, obracung, username_pd, id_go)
    
    cursor.execute(updateQuery)
    conn.commit()

    cursor.close()
    conn.close()

    return True

