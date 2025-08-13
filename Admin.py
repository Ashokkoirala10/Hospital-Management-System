from Doctor import *
from Patient import *
import datetime

doctors = [
    Doctor("Dendul", "Smith", "Cardiology"),
    Doctor("Emma", "Johnson", "Dermatology"),
    Doctor("Michael", "Brown", "Orthopedics"),
    Doctor("Sarah", "Williams", "Pediatrics"),
    Doctor("David", "Jones", "Neurology"),
]

discharged_patients = []

class Admin:
    def __init__(self, username, password, address =" "):
        self.__username = username
        self.__password = password
        self.__address =  address

    def get_username(self):
        return self.__username
    
    def get_password(self):
        return self.__password

    def view(self,a_list):
        for index, item in enumerate(a_list):
            print(f'{index+1:3}|{item}')

    def login(self) :
        
        print("--------Login--------")

        username = input('Enter the username: ')
        password = input('Enter the password: ')
        
        if username == self.__username and password == self.__password:
            print("You are loggedin.")
            return True
        else:
            return False
        
    def view_admin_detail(self):
        print("\n--------------------Admin Details----------------------------")
        print(f"\nThe username is {self.__username}")
        print(f"The password is {self.__password}")
        print(f"The address is {self.__address}")
        
    def find_index(self,index,doctors):
                  
        if index in range(0,len(doctors)):
            
            return True
        else:
            return False
            
    def get_doctor_details(self) :
        first_name = input('Enter the first name: ')
        surname = input('Enter the surname: ')
        speciality = input('Enter the speciality: ')
        return first_name, surname, speciality 
        
    def doctor_management(self, doctors,patients):
        while True:
            print("\n-----------------------Doctor Management-------------------------")

            print('\nChoose the operation:')
            print(' 1 - Register')
            print(' 2 - View')
            print(' 3 - Update')
            print(' 4 - Delete')
            print(' 5 - back')
            operation = input("\nPlease enter your choice: ")
            if operation =='1':
                print("\n--------------------Register---------------------")
                print("Enter the doctor's details: ")
                first_name = input("Enter the first name of doctor: ")
                surname = input("Enter the surname of doctor: ")
                speciality = input("Enter the speciality of doctor: ")

                for doctor in doctors:
                    if first_name == doctor.get_first_name() and surname == doctor.get_surname():
                        print('Name already exists.')
                        break

                else:   
                    doctor = Doctor(first_name, surname, speciality)
                    doctors.append(doctor)
                    print('Doctor successfully registered.')

            elif operation == '2':
                self.view_doctors_with_patients(doctors,patients)

            elif operation == '3':
                while True:
                    print("\n---------------Update Doctor`s Details----------------")
                    print("\nList of doctors:")
                    print(' ID|          Full name          |  Speciality   ')
                    self.view(doctors)
                    try:
                        index = int(input('Enter the ID of the doctor you want to update: ')) - 1
                    except ValueError:
                        print("Invalid input. Please enter a valid numerical ID.")
                        continue
                    doctor_index=self.find_index(index,doctors)
                    if doctor_index == False:
                        print("Doctor not found")

                    else:
                        if doctor_index == True:
                            print('Choose the field to be updated:')
                            print(' 1. First name')
                            print(' 2. Surname')
                            print(' 3. Speciality')

                            field = input('\nEnter the field you want to update: ')
                            if field == '1':
                                new_first_name = input("Enter the new first name: ")
                                doctors[index].set_first_name(new_first_name)
                                print("\nFirst name successfully changed! ")
                                break
                            elif field == '2':
                                new_surname = input("Enter the new surname: ")
                                doctors[int(index)].set_surname(new_surname)
                                print("\nSurname successfully changed! ")
                                break
                            elif field == '3':
                                new_speciality = input("Enter the new speciality: ")
                                doctors[int(index)].set_speciality(new_speciality)
                                print("\nSpeciallity successfully changed! ")
                                break
                            else:
                                print("Invalid choice")
                        else:
                            print("The ID entered was not found")
                            break

            elif operation == '4': 
                print("\n---------------Delete Doctor-----------------")
                print('\nID |          Full Name          |  Speciality')
                self.view(doctors)

                index = int(input('\nEnter the ID of the doctor you want to delete: '))-1
                if self.find_index(index, doctors):
                    doctors.pop(int(index))
                    print("Doctor deleted successfully")
                else:
                    print('The id entered is incorrect')
                    break
            elif operation == '5':
             break
            else:
                print('Invalid operation choosen!!')
                
    def add_new_patient(self, patients):
        print("\n----------------------- Add Patient------------------------------")
        first_name = input("\nEnter the first name of patient: ")
        surname = input("Enter the surname of patient: ")
        while True:
            try:
                age = int(input("Enter the age of patient: "))
                break  
            except ValueError:
                print("Invalid input. Please enter a numerical age.")

        while True:
            try:
                mobile = int(input("Enter the mobile number of patient: "))
                break  
            except ValueError:
                print("Invalid input. Please enter a numerical number.")
        while True:
            try:
                postcode = int(input("Enter the postcode of patient: "))
                break  
            except ValueError:
                print("Invalid input. Please enter a numerical postcode.")

        address= input("Enter the address of patient: ")

        new_patient = Patient(first_name, surname, age, mobile, postcode,address)
        patients.append(new_patient)
        Patient.save_to_file('patient_data.txt', patients)
        print("New patient has been added.")
        
    def view_patient(self, patients):
        print("\n--------------------------------------------View Patients-------------------------------------------------------------------")
        print('\nID |          Full Name           |     Assigned Doctor`s Full Name      | Age |    Mobile     | Postcode |     Address    ')
        self.view(patients)

    def same_family(self):
        print("\n---------------------------------------------------Patients With Same Family---------------------------------------------------------------")
        patients = Patient.load_from_file('patient_data.txt')
        same_family = {}
        for patient in patients:
            patient_surname = patient.get_surname()
            if patient_surname not in same_family:
                same_family[patient_surname] = [patient]
            else:
                same_family[patient_surname].append(patient)

        for surname, family_members in same_family.items():
            print(f"{surname} family:")
            print('\nS.N |           Full Name            |    Assigned Doctor`s Full Name     | Age |       Mobile         |  Postcode |       Address    ')
            for index, member in enumerate(family_members, 1):
                print(f"{index:^3} | {member.full_name():^30} | {member.get_doctor():^34} | {member.get_age():^3} | {member.get_mobile():^20} | {member.get_postcode():^10}| {member.get_address():^20}\n")

    def add_symptoms_to_patient(self, patients):
        print("\n----------------------------Add Symptoms to Patient-----------------------------")
        print('\nID |          Full Name           |     Assigned Doctor`s Full Name      | Age |    Mobile     | Postcode |     Address    ')
        self.view(patients)

        patient_id = input("\nEnter the ID of the patient you want to add symptom: ")

        try:
            patient_id = int(patient_id) - 1

            if patient_id not in range(len(patients)):
                print("Invalid patient ID.")
                return
            else:
                patient = patients[patient_id]
                symptoms = input("Enter symptoms seperated by coma if more than one: ")
                patient.set_symptoms(symptoms)
                print("\nSymptoms added successfully.")

        except ValueError:
            print("Invalid input. Please enter a valid patient ID.")

    def view_symptoms_of_patient(self, patients):
        print("\n---------------------------------------------View Symptoms of a Patient-----------------------------------------------------")
        print('\nID |          Full Name           |         Doctor`s Full Name           | Age |    Mobile     | Postcode |     Address    ')

        self.view(patients)

        patient_id = input("Enter the ID of the patient you want to see symptom: ")

        try:
            patient_id = int(patient_id) - 1

            if patient_id not in range(len(patients)):
                print("Invalid patient ID.")
                return

            else:
                patient = patients[patient_id]
                symptoms = patient.print_symptoms()
                if symptoms:
                    print(f"\nThe symptoms of {patient_id + 1} -{patient.full_name()} is:")
                    for item in symptoms:
                        print(f"  - {item}")
                else:
                    print(f"No symptoms recorded for {patient_id + 1}-{patient.full_name()}.")

        except ValueError:
            print("Invalid input. Please enter a valid patient ID.")

    def assign_doctor_to_patient(self, patients, doctors):
        
        print("\n----------------------------------------------Assign Patient To Doctor-----------------------------------------------------")
        print('\nID |          Full Name           |     Assigned Doctor`s Full Name      | Age |    Mobile     | Postcode |     Address    ')
        self.view(patients)

        patient_index = input('\nPlease enter the patient ID to be assigned: ')

        try:
            patient_index = int(patient_index)-1

            if patient_index not in range(len(patients)):
                print('\nThe id entered was not found.')
                return 
            else:
                patient = patients[patient_index]
                if patient.get_doctor() != 'None':
                    print(f"\nThe patient {patient.full_name()} is already assigned to a doctor. You need to relocate.")
                    return
                symptoms = patient.print_symptoms()
                if symptoms:
                    print(f"\nThe symptoms of {patient_index + 1} -{patient.full_name()} is:")
                    for item in symptoms:
                        print(f"  - {item}")
                else:
                    print(f"No symptoms recorded for {patient_index + 1}-{patient.full_name()}.")

        except ValueError: 
            print('\nThe id entered is incorrect')
            return 

        print("\n-----------------------Select Doctor-------------------------------")
        print('\nID |          Full Name          |  Speciality   ')
        self.view(doctors)
        doctor_index = input('\nPlease enter the doctor ID: ')

        try:
            doctor_index = int(doctor_index)-1

            if doctor_index not in range(len(doctors)):
                print('\nThe ID entered was not found.')
                return
            else:
                while True:
                    try:
                        appointment_month = input("\nEnter the month for appointment (e.g. january): ")
                        appointment_year = int(input("Enter the year of appointment(e.g.2024): "))
                        break
                    except ValueError:
                        print("please input appointment month and year in a correct format.")

                appointment_date = datetime.datetime(int(appointment_year), datetime.datetime.strptime(appointment_month, "%B").month, 1)
                patients[patient_index].link(doctors[doctor_index].full_name(), appointment_date)

                print("\n-------------------------------------------------Updated list-----------------------------------------------------------------")
                print('\nID |          Full Name           |     Assigned Doctor`s Full Name      | Age |    Mobile     | Postcode |       Address    ')
                self.view(patients)

                doctors[doctor_index].add_patient(patients[patient_index].full_name())
                doctors[doctor_index].add_appointment(appointment_date)
                Patient.save_to_file('patient_data.txt', patients)
                print('\nThe patient is now assigned to the doctor successfully.')
            
        except ValueError: 
            print('\nThe id entered is incorrect')

    def relocate_patient(self, patients, doctors):
        print("---------------------------------------Relocate Patient-------------------------------------------------------------------------")
        print('\nID |          Full Name           |         Doctor`s Full Name           | Age |    Mobile     | Postcode |     Address    ')
        
        assigned_patients = [patient for patient in patients if patient.get_doctor() != 'None']
        
        if not assigned_patients:
            print("No patients available for relocation.")
            return
        
        self.view(assigned_patients)

        patient_index = input('\nPlease enter the ID of the patient you want to relocate: ')
        
        try:
            patient_index = int(patient_index) - 1

            if patient_index not in range(len(assigned_patients)):
                print('The id entered was not found.')
                return 
            patient = patients[patient_index]
            symptoms = patient.print_symptoms()
            if symptoms:
                print(f"\nThe symptoms of {patient_index + 1} -{patient.full_name()} is:")
                for item in symptoms:
                    print(f"  - {item}")
            else:
                print(f"No symptoms recorded for {patient_index + 1}-{patient.full_name()}.")
        except ValueError: 
            print('The id entered is incorrect')
            return

        print("\n--------------------Select Doctors---------------------")
        print('\nID |          Full Name          |  Speciality   ')
        self.view(doctors)
        doctor_index = input('\nPlease enter the doctor ID: ')

        try:
            doctor_index = int(doctor_index) - 1

            if doctor_index not in range(len(doctors)):
                print('The ID entered was not found.')
                return
            
            old_doctor_name = assigned_patients[patient_index].get_doctor()
            
            if old_doctor_name:
                for doctor in doctors:
                    if doctor.full_name() == old_doctor_name:
                        doctor.remove_patient(assigned_patients[patient_index].full_name())
                        break

            while True:
                try:
                    appointment_month = input("\nEnter the new month for appointment (e.g. january): ")
                    appointment_year = int(input("Enter the new year of appointment(e.g.2024): "))
                    break
                except ValueError:
                    print("Please input appointment month and year in a correct format.")
            appointment_date = datetime.datetime(int(appointment_year), datetime.datetime.strptime(appointment_month, "%B").month, 1)

            assigned_patients[patient_index].link(doctors[doctor_index].full_name(), appointment_date)
            print("\n-------------------------------------------------Updated list-----------------------------------------------------------------")
            print('\nID |          Full Name           |     Assigned Doctor`s Full Name      | Age |    Mobile     | Postcode |       Address    ')
            self.view(assigned_patients)
            doctors[doctor_index].add_patient(assigned_patients[patient_index].full_name())
            doctors[doctor_index].add_appointment(appointment_date)
            Patient.save_to_file('patient_data.txt', patients)
            print('\nThe patient is now relocated to the new doctor.')
        except ValueError: 
            print('The id entered is incorrect')

    def discharge(self, patients, discharged_patients):
        print("--------------------------------------------Discharge Patient-------------------------------------------------------------------")
        print('\nID |          Full Name           |         Doctor`s Full Name           | Age |    Mobile     | Postcode |     Address    ')

        assigned_patients = [patient for patient in patients if patient.get_doctor() != 'None']
        self.view(assigned_patients)
        
        if not assigned_patients:
            print("No patients available to discharge.")
            return

        choice = input("\nDo you want to discharge a patient (Y/N): ").lower()
        if choice == "y" or choice == "yes":
            try:
                patient_index = int(input("\nPlease enter the ID of the patient to discharge: ")) - 1
            except ValueError:
                print("Invalid input. Please enter a valid patient ID.")
                return

            if self.find_index(patient_index, assigned_patients):
                discharge_patient = assigned_patients.pop(patient_index)
                discharged_patients.append(discharge_patient)
                patients.remove(discharge_patient)
                print(f"\nPatient {discharge_patient.full_name()} is discharged.")

                with open('patient_data.txt', 'r') as file:
                    lines = file.readlines()
                with open('patient_data.txt', 'w') as file:
                    for line in lines:
                        patient_info = line.strip().split(',')
                        if len(patient_info) >= 2 and discharge_patient.full_name() != f"{patient_info[0]} {patient_info[1]}":
                            file.write(line)
            else:
                print("Invalid patient ID.")

        elif choice == "n" or choice == "no":
            print("Not able to discharge.")

        else:
            print("Incorrect input.")

    def view_discharge(self, discharged_patients):
        print("\n-------------------------------------------------Discharged Patients--------------------------------------------------------")
        print('\nID |          Full Name           |         Doctor`s Full Name           | Age |    Mobile     | Postcode |     Address    ')
        self.view(discharged_patients)

    def view_doctors_with_patients(self, doctors, patients):
        print("\nList of doctors with assigned patients:")
        print("\n ID |          FULL NAME           |   SPECIALITY   | ASSIGNED PATIENTS")
        for index, doctor in enumerate(doctors):
            assigned_patients = [patient.full_name() for patient in patients if patient.get_doctor() == doctor.full_name()]
            print(f"{index + 1:3} | {doctor} | {', '.join(assigned_patients) if assigned_patients else 'None'}")
    
    def update_details(self):
        print('\nChoose the field to be updated:')
        print(' 1. Username')
        print(' 2. Password')
        print(' 3. Address')
        op = input('\nEnter the field you want to update: ')

        try:
            if op == "1":
                username1 = input('\nEnter the new username: ')
                username2 = input('Enter the new username again: ')
                if username1 == username2:
                    self.__username = username2
                    print("\nUsername updated successfully")
                else:
                    print("Both username have to be same.")

            elif op == "2":

                password1 = input('\nEnter the new password: ')
                password2 = input('Enter the new password again: ')
                if password1 == password2:
                    self.__password = password2
                    print("\nPassword updated successfully")
                else:
                    print("Both password have to be same.")
                
            elif op == "3":
                address1 = input('\nEnter the new address: ')
                address2 = input('Enter the new address again: ')
                if address1 == address2:
                    self.__address = address2
                    print("\nAddress updated successfully.")
                else:
                    print("Both address have to be same.")

            else:
                print("\nInvalid choice. Please enter above mentioned one.")
        
        except ValueError as e:
            print(str(e))       

    def admin_details(self):

        print(f"Username : {self.__username}")
        print(f"Password : {self.__password}")
        print(f"Address : {self.__address}")


    def report(self,patients):
        print("\n--------------------------------WELCOME TO REPORT CENTER-----------------------------------------------")
        print("""\nRequest for a management report.
             \n1. Total number of doctors in the system.
2. Total number of patients in the systems.
3. Total number of patients per doctors.
4. Total number of appointments per month per doctor.
5. Total number of patients based on the illness type.
""")
        choice = input ("Enter your request: ")
        while True:
            if choice == "1":
                total_doctors = len(doctors)
                print(f"Total number of doctors: {total_doctors}")  
                break 

            elif choice == "2":
                total_patients = len(patients)
                print(f"Total number of patients: {total_patients}")
                break

            elif choice == "3":
                for doctor in doctors:
                    num_patients = sum(1 for patient in patients if patient.get_doctor() == doctor.full_name())
                    print(f"The number of patients for {doctor.full_name()} is: {num_patients}")
                break
                30
                12.000
            elif choice == "4":
                print("\nTotal number of appointments per month per doctor:")
                for doctor in doctors:
                    print(f"{doctor.full_name()}:")
                    assigned_patients = [patient for patient in patients if patient.get_doctor() == doctor.full_name()]
                    if assigned_patients:
                        appointments = doctor.get_appointments()
                        if not appointments:
                            print("   - 0 appointments")
                        else:
                            for month, count in appointments.items():
                                print(f"   - {month}: {count} appointments")
                    else:
                        print("   - 0 appointments")
                break

            elif choice == "5":
                total_number_of_patients_based_on_illness = {}
                for patient in patients:
                    patient_symptoms = patient.print_symptoms()
                    for symptom in patient_symptoms:
                        if symptom not in total_number_of_patients_based_on_illness:
                            total_number_of_patients_based_on_illness[symptom] = 1
                        else:
                            total_number_of_patients_based_on_illness[symptom] += 1

                print("\nTotal number of patients based on the illness:")
                if not total_number_of_patients_based_on_illness:  
                    print("None")
                else:
                    for symptom, count in total_number_of_patients_based_on_illness.items():
                        print(f"{symptom:<45}: {count:>3} patients")
                break
            else:
                print("Invalid request.")
                break

        

