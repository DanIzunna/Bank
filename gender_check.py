import time

def gender_check():
    #To ensure that gender is male or female
    gender_ = input('Please Select your Gender \n\tMale (M)\n\tFemale (F)\n ').upper()
    if gender_ not in ['M', 'F', 'MALE', 'FEMALE']:
        time.sleep(0.5)
        print('INVALID GENDER\n MUST BE EITHER MALE OR FEMALE')
        return gender_check()
    elif gender_ == 'MALE':
            gender_ = 'M'
    elif gender_ == 'FEMALE':
        gender_ = 'F'
    return gender_