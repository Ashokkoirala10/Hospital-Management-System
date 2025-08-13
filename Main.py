from Admin import *
from Doctor import *
from Patient import *

def main():
    admin = Admin('admin','123','B1 1AB')
   
    while True:
        if admin.login():
            running = True 
            break
        else:
            print('Incorrect username or password.')

    patients = Patient.load_from_file('patient_data.txt')

    while running:
        print('\nChoose the operation:')
        print(' 1- Register/view/update/delete doctor')
        print(' 2- Add patients')
        print(' 3- View patients')
        print(' 4- Same family patients ')
        print(' 5- Add symptom')
        print(' 6- View symptom')
        print(' 7- Assign doctor to a patient')
        print(' 8- Relocate patient')
        print(' 9- Discharge patient')
        print(' 10- View discharged patient')
        print(' 11- Update admin details')
        print(' 12- View admin details')
        print(' 13- Hospital management report')
        print(' 14- Quit')

        op = input('Please enter your option: ')

        if op == '1':
            admin.doctor_management(doctors,patients)

        elif op == '2':
            admin.add_new_patient(patients)
            
        elif op == '3':
            admin.view_patient(patients)

        elif op == '4':
            admin.same_family()

        elif op == '5':
            admin.add_symptoms_to_patient(patients)
            
        elif op == '6':
            admin.view_symptoms_of_patient(patients)

        elif op == '7':
            admin.assign_doctor_to_patient(patients, doctors)

        elif op == '8':
            admin.relocate_patient(patients, doctors)
             
        elif op == '9':
            admin.discharge(patients, discharged_patients)
        
        elif op == '10':
            admin.view_discharge(discharged_patients)

        elif op == '11':
            admin.update_details()

        elif op == '12':
            admin.view_admin_detail()

        elif op == '13':
            admin.report(patients)

        elif op == '14':
            print("\n----------------------Thankyou!!------------------------------------")
            break

        else:
            print('\nInvalid option. Try again')

if __name__ == '__main__':
    main()
