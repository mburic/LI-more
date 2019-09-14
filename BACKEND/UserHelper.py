import psycopg2
import psycopg2.extras

from psycopg2 import IntegrityError, OperationalError

# Creation of Database Connectivity
connect_str = "dbname='luckakapetanija' user='mauro' host='localhost' password='admin'"


# Used for Login
def login(username, password, isAdmin):
    print("In UserHelper:: login")
    conn = psycopg2.connect(connect_str)
    cursor = conn.cursor(cursor_factory = psycopg2.extras.RealDictCursor)

    # Get Login Details
    GetUserQuery = "Select userid, fname, sname, username, email, isadmin, ispostava from users \
    where isdeleted = FALSE and isblocked = FALSE and \
    username = '" + username + "' and  password = '" + password + "' and isadmin = " + (isAdmin and "TRUE" or "FALSE") + ";"

    cursor.execute(GetUserQuery)
    singleUser = cursor.fetchone()

    cursor.close()
    conn.close()

    return singleUser

# Used for Registration
def registration(fname, sname, username, email, password, isadmin, ispostava, kontakt):
    #print("In UserHelper:: registration")
 
    conn = psycopg2.connect(connect_str)
    cursor = conn.cursor()

    # Insert User Details
    InsertUserQuery = "INSERT INTO USERS (fname,sname,username,email,kontakt,password,isadmin,ispostava) VALUES \
    ('"+fname+"','"+sname+"','"+username+"','"+email+"', '"+kontakt+"','"+password+"',"+(isadmin and "TRUE" or "FALSE")+",'"+ispostava +"');"

    cursor.execute(InsertUserQuery)
    conn.commit()

    cursor.close()
    conn.close()

    return True

# Used for Registration
def updateUser(userid, fname, sname, password, isadmin, ispostava, kontakt):
    #print("In UserHelper:: updateUser")
    try: 
        conn = psycopg2.connect(connect_str)
        cursor = conn.cursor()

        # Update User Details
        updateUserQuery = ""
        
        if password != "":
            updateUserQuery = "UPDATE USERS SET fname = '{}', sname = '{}', password = '{}', isadmin = '{}', ispostava = '{}', kontakt = '{}' where userid = '{}';".format(fname, sname, password, isadmin, ispostava, kontakt, userid)
        else:
            updateUserQuery = "UPDATE USERS SET fname = '{}', sname = '{}', isadmin = '{}', ispostava = '{}', kontakt = '{}' where userid = '{}';".format(fname, sname, isadmin, ispostava, kontakt, userid)
        #print(updateUserQuery)
        
        cursor.execute(updateUserQuery)
        conn.commit()
        updated_rows = cursor.rowcount

        cursor.close()
        conn.close()
        
    except OperationalError:
        print("In UserHelper:: updateUser :: OperationalError :: While inserting user details values in DB")
        return False

    except IntegrityError:
        print("In UserHelper:: updateUser :: IntegrityError :: While inserting user details values in DB")
        return False
    except:
        return False

    return True

# Used for Blocking USER in a table
def toggleBlockingUser(userid, isblocked):
    #print("In myHelper:: toggleBlockingUser")
    
    conn = psycopg2.connect(connect_str)
    
    cursor = conn.cursor()
    
    cursor.execute("UPDATE USERS SET isblocked = {} WHERE isdeleted = FALSE and userid = {}".format(isblocked, userid) )
    conn.commit()

    updated_rows = cursor.rowcount

    cursor.close()
    conn.close()

    return updated_rows > 0 and True or False

# Used for detete in a table
def deleteUser(userid):
    #print("In myHelper:: deleteUser")
    conn = psycopg2.connect(connect_str)
    
    cursor = conn.cursor()
    
    #updateUserQuery = "UPDATE USERS SET isdeleted = TRUE WHERE isdeleted = FALSE and userid = {}".format(userid) 
    updateUserQuery = "Delete from USERS WHERE userid = {}".format(userid) 
    cursor.execute(updateUserQuery)
    conn.commit()
    updated_rows = cursor.rowcount
    cursor.close()
    conn.close()

    return updated_rows > 0 and True or False

# Used for Get from a table
def getUsers(userid):
    #print("In UserHelper:: getUsers")
    conn = psycopg2.connect(connect_str)

    cursor = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    
    cursor.execute("SELECT userid, fname, sname, username, email, isadmin, ispostava, kontakt FROM USERS WHERE isdeleted = FALSE and userid != (select userid from USERS where userid = {} and isadmin = TRUE);".format(userid))
   
    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    return rows


#def setUpDatabase() :
    #print("In myHelper:: setUpDatabase")
   # try:
        # use our connection values to establish a connection
      #  conn = psycopg2.connect(connect_str)
        # create a psycopg2 cursor that can execute queries
      #  cursor = conn.cursor()
        #create a new table with a single column called "name"
       # cursor.execute("CREATE TABLE IF NOT EXISTS tutorial ( tutorial_id serial PRIMARY KEY, name varchar (50) NOT NULL );")
        # run a SELECT statement - no data in there, but we can try it
        # cursor.execute("""SELECT * from tutorials""")
        #conn.commit() # <--- makes sure the change is shown in the database
        # rows = cursor.fetchall()
        # print(rows)
        # print(len(rows))
        # print(type(rows))
        # for row in rows:
        #     print(row)
        #     print(type(row))

      #  cursor.close()
       # conn.close()
       # return True
    #except Exception as e:
        #print("Uh oh, can't connect. Invalid dbname, user or password?")
       # print(e)
      #  return False
