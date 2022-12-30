import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost" ,
    user = "root" ,
    password = "root" ,
    port = "3306" ,
    database = "blood_bank_management_system"
)

mycursor = mydb.cursor()

def check_request_for_blood ():
    mycursor.execute( "SELECT * FROM request_status WHERE status = 2" )
    requests = mycursor.fetchall()
    for request in requests:
        d_id = request[ 0 ]
        p_id = request[ 1 ]
        mycursor.execute( f"SELECT * FROM blood_donor WHERE bd_id = { d_id } " )
        donor = mycursor.fetchall()
        mycursor.execute( f"SELECT * FROM patient_details WHERE pt_id = { p_id } " )
        patient = mycursor.fetchall()
        print ( "****************** \n Donor name:" , donor[ 0 ][ 1 ])
        print ( "Gender:" , donor[ 0 ][ 3 ])
        print ( "Blood group:" , donor[ 0 ][ 5 ])
        if (donor[ 0 ][ 7 ]):
            print ( "Disease:" , donor[ 0 ][ 7 ])
        else :
            print ( "Disease: None" )
        print ( "****************** \n Patient Name:" , patient[ 0 ][ 1 ])
        print ( "Age:" , patient[ 0 ][ 2 ])
        print ( "Blood group:" , patient[ 0 ][ 3 ])
        print ( "******************" )
        request_result = int ( input ( "Do you want to approve blood donation request? \n For yes press (1), for no press (0)" ))
        mycursor.execute( f"UPDATE request_status SET status = { request_result } WHERE donor_id = { d_id } AND patient_id = { p_id } " )
        mydb.commit()
        continuation = input ( "Do you want to check further records? Type (Yes/No): " )
        if continuation == "No" :
            break
check_request_for_blood()