import json
from flask import jsonify 

from flask import Flask, request
from flask_cors import CORS, cross_origin
app = Flask(__name__)
cors = CORS(app)
app.config["CORS_HEADERS"] = "Content-Type"

# To generate a unique ID
import uuid 

# Get Functions from UserHelper.py
import UserHelper as userHelper

# Get Functions from FormHelper.py
import FormHelper as formHelper

# API Create to Generate Unique Sequence
@app.route('/GetUUID', methods=['GET'])
def generateUUID():
    return jsonify( {"uuid": uuid.uuid1()})

# Login Service
@app.route('/Login',methods=['POST'])
def login():
    #print("In myServer:: login")
    
    requestObject = request.get_json()
    
    # Checking for Request Object if empty
    if requestObject == 'NoneType' or requestObject == None:
        return jsonify({"error":"Nedovoljno podataka", "status":"Neuspješna prijava"})

    # Checking for Required Parameters
    if 'username' not in  requestObject or 'password' not in requestObject or 'isadmin' not in requestObject:
        return jsonify({"error":"Nedovoljno podataka", "status":"Neuspješna prijava"})
    
    # Login Check
    userObject = userHelper.login(requestObject['username'], requestObject['password'], requestObject['isadmin'])

    if userObject == None:
        return jsonify({"error":"Krivi podaci", "status":"Neuspješna prijava"})

    # Return User Object
    return jsonify({"error":"", "status":"Successfully login", "userObject":userObject})

# Registration Service
@app.route('/Registration', methods=['POST'])
def UserRegistration():
    #print("In myServer:: UserRegistration")
    
    requestObject = request.get_json()
    #print(requestObject)

    if requestObject == 'NoneType' or requestObject == None:
        return jsonify({"error":"Nedovoljno podataka", "status":"Neuspješna registracija"})

    if 'fname' not in  requestObject or 'sname' not in requestObject or 'username' not in requestObject or 'email' not in  requestObject or 'password' not in requestObject or 'isadmin' not in requestObject or 'ispostava' not in requestObject and 'kontakt'  not in requestObject:
        return jsonify({"error":"Nedovoljno podataka", "status":"Neuspješna registracija"})
    
    successful = userHelper.registration(requestObject['fname'], requestObject['sname'], requestObject['username'], requestObject['email'], requestObject['password'], requestObject['isadmin'], requestObject['ispostava'], requestObject['kontakt'])

    if not successful :
        return jsonify({"error":"Insert Error", "status":"Nemoguće kreirati novog korisnika"})

    return jsonify({"error":"", "status":"Uspješno registriran"})

# GetUsers Service
@app.route('/GetUsers', methods=['POST'])
def GetUsers():
    #print("In myServer:: GetUsers")

    requestObject = request.get_json()
    if requestObject == 'NoneType' or requestObject == None:
        return jsonify({"error":"Nedovoljno podataka", "status":"Neuspješna prijava"})

    if 'userid' not in  requestObject:
        return jsonify({"error":"Nedovoljno podataka", "status":"Neuspješna prijava"})

    return jsonify({"error":"", "data":userHelper.getUsers(requestObject['userid'])})

# DeleteUser Service
@app.route('/DeleteUser', methods=['POST'])
def DeleteUser():
    #print("In myServer:: DeleteUser")
    requestObject = request.get_json()
    if requestObject == 'NoneType' or requestObject == None:
        return jsonify({"error": "Nedovoljno podataka", "status": "Neuspješno ažuriranje"})

    if 'userid' not in  requestObject:
        return jsonify({"error":"Nedovoljno podataka", "status":"Neuspješno ažuriranje"})

    if userHelper.deleteUser(requestObject['userid']):
        return jsonify({"error":"", "status":"Uspješno izbrisan korisnik."})
    else:
        return jsonify({"error":"", "status":"Nemoguće izbrisati korisnika."})
    return 0

# UpdateUser Service
@app.route('/UpdateUser', methods=['POST'])
def UpdateUser():
    #print("In myServer:: UpdateUser")
    requestObject = request.get_json()
    if requestObject == 'NoneType' or requestObject == None:
        return jsonify({"error":"Nedovoljno podataka", "status":"Neuspješno ažuriranje"})

    if 'userid' not in  requestObject and 'fname' not in  requestObject or 'sname' not in requestObject or 'password' not in requestObject or 'isadmin' not in requestObject or 'ispostava' not in requestObject or 'kontakt' not in requestObject:
        return jsonify({"error":"Nedovoljno podataka", "status":"Neuspješno ažuriranje"})
    
    successful = userHelper.updateUser(requestObject['userid'], requestObject['fname'], requestObject['sname'], requestObject['password'], requestObject['isadmin'], requestObject['ispostava'], requestObject['kontakt'])

    if not successful :
        return jsonify({"error":"Update Error", "status":"Nemoguće ažurirati korisnika"})

    return jsonify({"error":"", "status":"Uspješno ažuriran korisnik."})

# ToggleBlockingUser Service
@app.route('/ToggleBlockingUser', methods=['POST'])
def ToggleBlockingUser():
    #print("In myServer:: ToggleBlockingUser")

    requestObject = request.get_json()
    if requestObject == 'NoneType' or requestObject == None:
        return jsonify({"error":"Nedostaju podaci", "status":"Neuspješno ažuriranje"})

    if 'userid' not in  requestObject and 'isblocked' not in  requestObject:
        return jsonify({"error": "Nedostaju podaci", "status": "Neuspješno ažuriranje"})

    if userHelper.toggleBlockingUser(requestObject['userid'], requestObject['isblocked']):
        return jsonify({"error":"", "status":"Successfully ToggleBlocking user."})
    else:
        return jsonify({"error":"", "status":"Unable to ToggleBlocking user."})

    return 0


#Interaction with prijavad
@app.route('/PrijavadForm1', methods=['POST'])
def PrijavadForm1():
    #print("In myServer:: PrijavadForm1")
    requestObject = request.get_json()

    if requestObject == None:
        return jsonify({"error":"Nedostaju podaci", "status":""})

    if 'username' not in  requestObject or 'actiontotake' not in  requestObject:
        return jsonify({"error":"Nedostaju podaci", "status":""})

    # Get Data
    if requestObject['actiontotake'] == 'Get':
        try:
            data = formHelper.get_prijavad_form1()
            return jsonify({"actionperformed":"Get", "data":data, "error":""})
        except:
            return jsonify({"actionperformed":"Get", "data":None, "error":"Nemoguće preuzeti podatke"})
    
    # Insert Data
    if requestObject['actiontotake'] == 'Insert':
        if 'ispostava_pd' not in  requestObject or 'date_pd' not in  requestObject or 'oznaka_pd' not in  requestObject or 'duzina_pd' not in  requestObject or 'vrstaplovila_pd' not in  requestObject  or 'kontakt_pd' not in  requestObject or 'lukad' not in  requestObject or 'ime_pd' not in  requestObject or 'prezime_pd' not in  requestObject or 'brojclanova_pd' not in  requestObject or 'username' not in  requestObject:
            return jsonify({"error":"Nedostaju podaci", "status":""})
        try:
            data = formHelper.insert_prijavad_form1(requestObject['ispostava_pd'], requestObject['date_pd'], requestObject['oznaka_pd'], requestObject['duzina_pd'], requestObject['vrstaplovila_pd'], requestObject['kontakt_pd'], requestObject['lukad'], requestObject['ime_pd'], requestObject['prezime_pd'], requestObject['brojclanova_pd'], requestObject['username'])
            return jsonify({"actionperformed":"Insert",  "error":"", "status":"Uspješno dodana"})
        except:
            return jsonify({"actionperformed":"Insert",  "error":"Nemoguće dodati podatke"})
    
    # Update Data
    if requestObject['actiontotake'] == 'Update':
        if 'id_pd' not in requestObject or 'ispostava_pd' not in  requestObject or 'date_pd' not in  requestObject or 'oznaka_pd' not in  requestObject or 'duzina_pd' not in  requestObject or 'vrstaplovila_pd' not in  requestObject or 'kontakt_pd' not in  requestObject or 'lukad' not in  requestObject or 'ime_pd' not in  requestObject or 'prezime_pd' not in  requestObject or 'brojclanova_pd' not in  requestObject or 'username' not in  requestObject:
            return jsonify({"error":"Nedostaju podaci", "status":""})
        try:
            return formHelper.update_prijavad_form1(requestObject['id_pd'], requestObject['ispostava_pd'], requestObject['date_pd'], requestObject['oznaka_pd'], requestObject['duzina_pd'], requestObject['vrstaplovila_pd'], requestObject['kontakt_pd'], requestObject['lukad'], requestObject['ime_pd'], requestObject['prezime_pd'], requestObject['brojclanova_pd'], requestObject['username']) and jsonify({"actionperformed":"Update",  "error":"", "status":"Successfully Updated"}) or jsonify({"actionperformed":"Update", "error":"Nemoguće, dodano od drugog korisnika"})
        except:
            return jsonify({"actionperformed":"Update",  "error":"Nemoguće dodati podatke"})

    # Delete Data
    if requestObject['actiontotake'] == 'Delete':
        if 'id_pd' not in  requestObject or 'username' not in  requestObject:
            return jsonify({"error":"Nedostaju podaci", "status":""})
        try:
            return formHelper.delete_prijavad_form1(requestObject['username'], requestObject['id_pd']) and jsonify({"actionperformed": "Delete",  "error": "", "status": "Successfully Deleted"}) or jsonify({"actionperformed": "Delete",  "error": "Nemoguće, dodano od drugog korisnika", "status": ""})
        except:
            return jsonify({"actionperformed":"Delete",  "error":"Nemoguće izbrisati podatke"})

    return jsonify({"error":"Invalid Request", "status":""})

#Interaction with prijavaod
@app.route('/PrijavaodForm2', methods=['POST'])
def PrijavaodForm2():
    #print("In myServer:: PrijavaodForm2")
    requestObject = request.get_json()
    if requestObject == None:
        return jsonify({"error":"Insufficient Parameters", "status":"Neuspješno ažuriranje"})

    if 'username' not in  requestObject or 'actiontotake' not in  requestObject:
        return jsonify({"error":"Nedostaju podaci", "status":"Neuspješno ažuriranje"})

    # Get Data
    if requestObject['actiontotake'] == 'Get':
        try:
            data = formHelper.get_prijavaod_form2()
            return jsonify({"actionperformed":"Get", "data":data , "error":""})
        except:
            return jsonify({"actionperformed":"Get", "data":None , "error":"Nemoguće preuzeti podatke"})

    # Insert Data
    if requestObject['actiontotake'] == 'Insert':
        if 'ispostava_po' not in  requestObject or 'date_po' not in  requestObject or 'oznaka_po' not in  requestObject or 'duzina_po' not in  requestObject or 'vrstaplovila_po' not in  requestObject  or 'kontakt_po' not in  requestObject or 'lukao' not in  requestObject or 'ime_po' not in  requestObject or 'prezime_po' not in  requestObject or 'brojclanova_po' not in  requestObject or 'napomena_po' not in  requestObject or 'username' not in  requestObject:
            return jsonify({"error":"Nedostaju podaci", "status":""})
        try:
            data = formHelper.insert_prijavaod_form2(requestObject['ispostava_po'], requestObject['date_po'], requestObject['oznaka_po'], requestObject['duzina_po'], requestObject['vrstaplovila_po'], requestObject['kontakt_po'], requestObject['lukao'], requestObject['ime_po'], requestObject['prezime_po'], requestObject['brojclanova_po'], requestObject['napomena_po'], requestObject['username'])
            return jsonify({"actionperformed":"Insert",  "error":"", "status":"Uspješno dodana"})
        except:
            return jsonify({"actionperformed":"Insert",  "error":"Nemoguće dodati podatke"})

    # Delete Data
    if requestObject['actiontotake'] == 'Delete':

        if 'id_po' not in  requestObject or 'username' not in  requestObject:
            return jsonify({"error":"Nedostaju podaci", "status":""})

        try:
            return formHelper.delete_prijavaod_form2(requestObject['username'], requestObject['id_po']) and jsonify({"actionperformed": "Delete",  "error": "", "status": "Successfully Deleted"}) or jsonify({"actionperformed": "Delete",  "error": "Nemoguće, dodano od drugog korisnika", "status": ""})
        except:
            return jsonify({"actionperformed":"Delete",  "error":"Nemoguće izbrisati podatke"})

    # Update Data update_prijavaod_form2
    if requestObject['actiontotake'] == 'Update':
        if 'id_po' not in  requestObject or 'ispostava_po' not in  requestObject or 'date_po' not in  requestObject or 'oznaka_po' not in  requestObject or 'duzina_po' not in  requestObject or 'vrstaplovila_po' not in  requestObject  or 'kontakt_po' not in  requestObject or 'lukao' not in  requestObject or 'ime_po' not in  requestObject or 'prezime_po' not in  requestObject or 'brojclanova_po' not in  requestObject or 'napomena_po' not in  requestObject or 'username' not in  requestObject:
            return jsonify({"error":"Nedostaju podaci", "status":""})
        try:
            return formHelper.update_prijavaod_form2(requestObject['id_po'], requestObject['ispostava_po'], requestObject['date_po'], requestObject['oznaka_po'], requestObject['duzina_po'], requestObject['vrstaplovila_po'], requestObject['kontakt_po'], requestObject['lukao'], requestObject['ime_po'], requestObject['prezime_po'], requestObject['brojclanova_po'], requestObject['napomena_po'], requestObject['username']) and jsonify({"actionperformed": "Update",  "error": "", "status": "Successfully Updated"}) or jsonify({"actionperformed": "Update", "error": "Nemoguće, dodano od drugog korisnika"})
        except:
            return jsonify({"actionperformed":"Update",  "error":"Nemoguće ažurirati podatke"})

    return jsonify({"error":"Invalid Request", "status":""})

#Interaction with prijavado
@app.route('/PrijavadoForm3', methods=['POST'])
def PrijavadoForm3():
    #print("In myServer:: PrijavadoForm3")
    requestObject = request.get_json()
    
    if requestObject == None:
        return jsonify({"error":"Nedostaju podaci", "status":"Neuspješno dodavanje"})

    if 'username' not in  requestObject or 'actiontotake' not in  requestObject:
        return jsonify({"error":"Nedostaju podaci", "status":""})

    # Get Data
    if requestObject['actiontotake'] == 'Get':
        try:
            data = formHelper.get_prijavado_form3()
            return jsonify({"actionperformed":"Get", "data":data, "error":""})
        except:
            return jsonify({"actionperformed":"Get", "data":None, "error":"Nemoguće preuzeti podatke"})

    # Insert Data
    if requestObject['actiontotake'] == 'Insert':
        if 'serijskibrojd' not in  requestObject or 'datum_od' not in  requestObject or 'datum_do' not in  requestObject or 'nacindolaskad' not in  requestObject or 'imeplovilad' not in  requestObject or 'vrstaplovilad' not in  requestObject or 'oznakad' not in  requestObject or 'duljinad' not in  requestObject or 'drzava' not in  requestObject or 'brojclanovad' not in  requestObject or 'imed' not in  requestObject or 'prezimed' not in  requestObject or 'kontaktd' not in  requestObject or 'obracund' not in  requestObject or 'username' not in  requestObject:
            return jsonify({"error":"Nedostaju podaci", "status":""})
        try:
            data = formHelper.insert_prijavado_form3(requestObject['serijskibrojd'], requestObject['datum_od'], requestObject['datum_do'],  requestObject['nacindolaskad'], requestObject['imeplovilad'], requestObject['vrstaplovilad'], requestObject['oznakad'], requestObject['duljinad'], requestObject['drzava'], requestObject['brojclanovad'], requestObject['imed'], requestObject['prezimed'], requestObject['kontaktd'], requestObject['obracund'],  requestObject['username'])
            return jsonify({"actionperformed":"Insert",  "error":"", "status":"Uspješno dodana"})
        except:
            return jsonify({"actionperformed":"Insert",  "error":"Nemoguće dodati podatke"})

    # Delete Data
    if requestObject['actiontotake'] == 'Delete':
        if 'id_do' not in  requestObject or 'username' not in  requestObject:
            return jsonify({"error":"Nedostaju podaci", "status":""})
        try:
            return formHelper.delete_prijavado_form3(requestObject['username'], requestObject['id_do']) and jsonify({"actionperformed": "Delete",  "error": "", "status": "Successfully Deleted"}) or jsonify({"actionperformed": "Delete",  "error": "Nemoguće, dodano od drugog korisnika", "status": ""})
        except:
            return jsonify({"actionperformed":"Delete",  "error":"Nemoguće izbrisati podatke"})

    # Update Data update_prijavado_form3
    if requestObject['actiontotake'] == 'Update':
        if 'id_do' not in  requestObject or 'serijskibrojd' not in  requestObject or 'datum_od' not in  requestObject or 'datum_do' not in  requestObject or 'nacindolaskad' not in  requestObject or 'imeplovilad' not in  requestObject or 'vrstaplovilad' not in  requestObject or 'oznakad' not in  requestObject or 'duljinad' not in  requestObject or 'drzava' not in  requestObject or 'brojclanovad' not in  requestObject or 'imed' not in  requestObject or 'prezimed' not in  requestObject or 'kontaktd' not in  requestObject or 'obracund' not in  requestObject or 'username' not in  requestObject:
            return jsonify({"error":"Nedostaju podaci", "status":""})
        try:
            return formHelper.update_prijavado_form3(requestObject['id_do'], requestObject['id_do'], requestObject['datum_od'], requestObject['datum_do'],  requestObject['nacindolaskad'], requestObject['imeplovilad'], requestObject['vrstaplovilad'], requestObject['oznakad'], requestObject['duljinad'], requestObject['drzava'], requestObject['brojclanovad'], requestObject['imed'], requestObject['prezimed'], requestObject['kontaktd'], requestObject['obracund'],  requestObject['username']) and jsonify({"actionperformed": "Update",  "error": "", "status": "Successfully Updated"}) or jsonify({"actionperformed": "Update", "error": "Nemoguće, dodano od drugog korisnika"})
        except:
            return jsonify({"actionperformed":"Update",  "error":"Nemoguće ažurirati podatke"})

    return jsonify({"error":"Invalid Request", "status":""})


#Interaction with get_prijavago_form4
@app.route('/PrijavagoForm4', methods=['POST'])
def PrijavagoForm4():
    #print("In myServer:: PrijavagoForm4")
    requestObject = request.get_json()
    if requestObject == 'NoneType' or requestObject == None:
        return jsonify({"error":"Nedostaju podaci", "status":"Neuspješno ažuriranje"})

    if 'username' not in  requestObject or 'actiontotake' not in  requestObject:
        return jsonify({"error":"Nedostaju podaci", "status":"Neuspješno ažuriranje"})
    
    # Get Data
    if requestObject['actiontotake'] == 'Get':
        try:
            data = formHelper.get_prijavago_form4()
            return jsonify({"actionperformed":"Get", "data":data, "error":""})
        except:
            return jsonify({"actionperformed":"Get", "data":None, "error":"Nemoguće preuzeti podatke"})

    # Insert Data
    if requestObject['actiontotake'] == 'Insert':
        if 'serijskibrojg' not in  requestObject or 'datumg_od' not in  requestObject or 'datumg_do' not in  requestObject or 'nacindolaskag' not in  requestObject or 'imeplovilag' not in  requestObject or 'vrstaplovilag' not in  requestObject or 'oznakag' not in  requestObject or 'duljinag' not in  requestObject or 'brojclanovag' not in  requestObject or 'imeg' not in  requestObject or 'prezimeg' not in  requestObject or 'kontaktg' not in  requestObject or 'obracung' not in  requestObject or 'username' not in  requestObject:
            return jsonify({"error":"Nedostaju podaci", "status":""})
        try:
            data = formHelper.insert_prijavago_form4(requestObject['serijskibrojg'], requestObject['datumg_od'], requestObject['datumg_do'],  requestObject['nacindolaskag'], requestObject['imeplovilag'], requestObject['vrstaplovilag'], requestObject['oznakag'], requestObject['duljinag'], requestObject['brojclanovag'], requestObject['imeg'], requestObject['prezimeg'], requestObject['kontaktg'], requestObject['obracung'],  requestObject['username'])
            return jsonify({"actionperformed":"Insert",  "error":"", "status":"Uspješno dodana"})
        except:
            return jsonify({"actionperformed":"Insert",  "error":"Nemoguće dodati podatke"})

    # Delete Data
    if requestObject['actiontotake'] == 'Delete':
        if 'id_go' not in  requestObject or 'username' not in  requestObject:
            return jsonify({"error":"Nedostaju podaci", "status":""})
        try:
            return formHelper.delete_prijavago_form4(requestObject['username'], requestObject['id_go']) and jsonify({"actionperformed": "Delete",  "error": "", "status": "Successfully Deleted"}) or jsonify({"actionperformed": "Delete",  "error": "Nemoguće, dodano od drugog korisnika", "status": ""})
        except:
            return jsonify({"actionperformed":"Delete",  "error":"Nemoguće izbrisati podatke"})

    # Update Data update_prijavago_form4
    if requestObject['actiontotake'] == 'Update':
        if 'id_go' not in  requestObject or 'serijskibrojg' not in  requestObject or 'datumg_od' not in  requestObject or 'datumg_do' not in  requestObject or 'nacindolaskad' not in  requestObject or 'imeplovilag' not in  requestObject or 'vrstaplovilag' not in  requestObject or 'oznakag' not in  requestObject or 'duljinag' not in  requestObject or 'brojclanovag' not in  requestObject or 'imeg' not in  requestObject or 'prezimeg' not in  requestObject or 'kontaktg' not in  requestObject or 'obracung' not in  requestObject or 'username' not in  requestObject:
            return jsonify({"error":"Nedostaju podaci", "status":""})
        try:
            return formHelper.update_prijavago_form4(requestObject['id_go'], requestObject['serijskibrojg'], requestObject['datumg_od'], requestObject['datumg_do'],  requestObject['nacindolaskad'], requestObject['imeplovilag'], requestObject['vrstaplovilag'], requestObject['oznakag'], requestObject['duljinag'], requestObject['brojclanovag'], requestObject['imeg'], requestObject['prezimeg'], requestObject['kontaktg'], requestObject['obracung'],  requestObject['username']) and jsonify({"actionperformed": "Update",  "error": "", "status": "Successfully Updated"}) or jsonify({"actionperformed": "Update", "error": "Nemoguće, dodano od drugog korisnika"})
        except:
            return jsonify({"actionperformed":"Update",  "error":"Nemoguće ažuriranje podataka"})

    return jsonify({"error":"Invalid Request", "status":""})


@app.route('/GetCount', methods=['GET'])
def GetCount():
    return jsonify({"actionperformed":"Get", "data":formHelper.countPrijave() , "error":""})

if __name__ == '__main__':
    # run for production
    app.run(host='0.0.0.0',port=8082)

    # run for development and testing
    # app.run(host='0.0.0.0',port=8082,debug=True)
    
