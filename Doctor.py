from person import Person
class Doctor(Person):
    def __init__(self, first_name, surname, speciality):
        super().__init__(first_name, surname)
        self.__speciality = speciality
        self.__patients = []
        self.__appointments = {}

    def get_speciality(self) :
        return self.__speciality

    def set_speciality(self, new_speciality):
        self.__speciality = new_speciality
        return self.__speciality

    def add_patient(self, patient):
        self.__patients.append(patient)

    def add_appointment(self, appointment_date):
        month_year = appointment_date.strftime("%B %Y")
        if month_year not in self.__appointments:
            self.__appointments[month_year] = 1
        else:
            self.__appointments[month_year] += 1


    def get_appointments(self):
        return self.__appointments
    
    def remove_patient(self, patient_name):
        if patient_name in self.__patients:
            self.__patients.remove(patient_name)


    def __str__(self) :
        return f'{self.full_name():^29}|{self.__speciality:^15}'
