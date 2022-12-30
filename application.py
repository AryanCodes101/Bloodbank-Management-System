import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost" ,
    user = "root" ,
    password = "root" ,
    port = "3306" ,
    database = "blood_bank_management_system"
)
mycursor = mydb.cursor()

def register_blood_donor ():
    name = input ( "Enter your name: " )
    gender = input ( "Enter your gender (M/F): " )
    phone_no = input ( "Enter your phone number: " )
    age = int ( input ( "Enter your age: " ))
    blood_group = input ( "Enter blood group: " )
    city_ = input ( "Enter your city: " )
    diseases = input ( "Enter any disease donor is suffering from, if not just type enter: " )

mycursor.execute( f"SELECT city_id FROM city WHERE city_name = ' { city_ } '" )
city_id = mycursor.fetchall()[ 0 ][ 0 ]

mycursor.execute( f"SELECT MAX(bd_id) FROM blood_donor" )
bd_id = mycursor.fetchall()[ 0 ][ 0 ] + 1

if diseases == '' :
    mycursor.execute( f"INSERT INTO blood_donor VALUES ( { bd_id } , ' { name } ', ' { phone_no } ', ' { gender } ', { age } , ' { blood_group } ', { city_id } , NULL)" )
else :
    mycursor.execute( f"INSERT INTO blood_donor VALUES ( { bd_id } , ' { name } ', ' { phone_no } ', ' { gender } ', { age } , ' { blood_group } ', { city_id } , ' { diseases } ')" )

mydb.commit()

print ( f"Name: { name }\n Donor id: { bd_id }\n " )

def search_for_blood_donors ():
    blood_group_required = input ( "Enter blood group required: " )
    city = input ( "Enter city: " )
    mycursor.execute( f"SELECT city_id FROM city WHERE city_name = ' { city } '" )
    city_id = mycursor.fetchall()[ 0 ][ 0 ]
    mycursor.execute( f"SELECT * FROM blood_donor WHERE bd_Bgroup = ' { blood_group_required } ' AND City_ID = ' { city_id } '" )
    donors = mycursor.fetchall()
    if len (donors) == 0 :
        print ( f" { blood_group_required } is a very rare blood group in { city } . \n Try finding in another city." )
    else :
        print ( "List of donors: \n " )
        for donor in donors:
            print ( "Donor ID:" , donor[ 0 ], " \n Name:" , donor[ 1 ], " \n Contact No:" , donor[ 2 ], " \n " )

def register_patient ():
    name = input ( "Enter name:" )
    age = int ( input ( "Enter age: " ))
    blood_group = input ( "Enter blood group: " )
    phone_number = input ( "Enter phone number: " )
    mycursor.execute( "SELECT MAX(pt_id) FROM patient_details" )
    pt_id = mycursor.fetchall()[ 0 ][ 0 ] + 1
    mycursor.execute( f"INSERT INTO patient_details VALUES ( { pt_id } , ' { name } ', { age } , ' { blood_group } ', ' { phone_number } ')" )
    
    mydb.commit()
    
    print ( " \n\n Record saved successfully! \n Name:" , name, " \n Patient ID:" , pt_id)

def ask_doctor_for_approval ():
    donor_id = int ( input ( "Enter donor id: " ))
    patient_id = int ( input ( "Enter patient id: " ))
    current_status = 2
    mycursor.execute( f"INSERT INTO request_status VALUES ( { donor_id } , { patient_id } , { current_status } )" )

    mydb.commit()

def check_status_of_blood_request ():
    d_id = int ( input ( "Enter donor id: " ))
    p_id = int ( input ( "Enter patient id: " ))
    mycursor.execute( f"SELECT status FROM request_status WHERE donor_id = { d_id } AND patient_id = { p_id } " )
    current_status = mycursor.fetchall()[ 0 ][ 0 ]
    if current_status == 2 :
        print ( "Doctor hasn't approved your request yet." )
    elif current_status == 1 :
        print ( "Doctor has approved your request. \n You can get blood." )
    else :
        print ( "Doctor had not approved your request. Try finding some other donor." )

print ( "blood bank management system" )
current_input = "a"
while current_input != "q" :
    print ( " \n\n For registration of new blood donor, type (a)" )
    print ( "For finding blood donors with required blood group, type (b)" )
    print ( "For registration of patient, type(c)" )
    print ( "For sending a request for blood donation, type(d)" )
    print ( "For checking the status of blood donation request, type(e)" )
    print ( "For quitting, type (q)" )
    current_input = input ()
    if current_input == "a" :
        register_blood_donor()
    elif current_input == "b" :
        search_for_blood_donors()
    elif current_input == "c" :
        register_patient()
    elif current_input == "d" :
        ask_doctor_for_approval()
    elif current_input == "e" :
        check_status_of_blood_request()
    elif current_input == "q" :
        break
    else :
        print ( "Invalid input, try again" )