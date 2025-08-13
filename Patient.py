from person import Person
class Patient(Person):
    def __init__(self, first_name, surname, age, mobile, postcode,address):
        super().__init__(first_name, surname)
        self.__age = age
        self.__mobile = mobile
        self.__postcode = postcode
        self.__address = address
        self.__symptom = [] 
        self.__doctor = 'None'
        self.appointment_date = 'None'
    

    def get_address(self):
        return self.__address
    def get_age(self):
        return self.__age

    def get_mobile(self):
        return self.__mobile

    def get_postcode(self):
        return self.__postcode

    def get_address(self):
        return self.__address

    def get_doctor(self) :
        return self.__doctor

    def link(self, doctor, appointment_date):
        self.__doctor = doctor
        self.appointment_date = appointment_date

    def print_symptoms(self):
        return self.__symptom

    def set_symptoms(self, symptoms):
        self.__symptom.append(symptoms)



    @staticmethod
    def save_to_file(patient_data, patients):
        with open(patient_data, 'w') as file:
            for patient in patients:
                file.write(f"{patient.get_first_name()},{patient.get_surname()},{patient.get_doctor()},{patient.get_age()},{patient.get_mobile()},{patient.get_postcode()},{patient.get_address()}\n")

    @staticmethod
    def load_from_file(patient_data):
        patients = []
        try:
            with open(patient_data, 'r') as file:
                for line in file:
                    data = line.strip().split(',')
                    if len(data) == 7: 
                        first_name, surname, doctor, age, mobile, postcode, address = data
                        patient = Patient(first_name, surname, age, mobile, postcode,address)
                        patient.link(doctor, None) 
                        patients.append(patient)
            return patients
        except FileNotFoundError:
            print("File not found.")
            return []
    

    def __str__(self):
        return f'{self.full_name():^30}|{self.__doctor:^38}|{self.__age:^5}|{self.__mobile:^15}|{self.__postcode:^10}|{self.__address:^20}'
