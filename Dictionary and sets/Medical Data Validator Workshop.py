import re  # Regular Expression (Regex) ব্যবহার করার জন্য re module import করা হয়েছে

medical_records = [  # সব রোগীর তথ্য রাখার জন্য একটি list
    {
        'patient_id': 'P1001',  # রোগীর আইডি
        'age': 34,  # বয়স
        'gender': 'Female',  # লিঙ্গ
        'diagnosis': 'Hypertension',  # রোগের নাম
        'medications': ['Lisinopril'],  # ওষুধের তালিকা
        'last_visit_id': 'V2301',  # সর্বশেষ ভিজিট আইডি
    },
    {
        'patient_id': 'p1002',
        'age': 47,
        'gender': 'male',
        'diagnosis': 'Type 2 Diabetes',
        'medications': ['Metformin', 'Insulin'],
        'last_visit_id': 'v2302',
    },
    {
        'patient_id': 'P1003',
        'age': 29,
        'gender': 'female',
        'diagnosis': 'Asthma',
        'medications': ['Albuterol'],
        'last_visit_id': 'v2303',
    },
    {
        'patient_id': 'p1004',
        'age': 56,
        'gender': 'Male',
        'diagnosis': 'Chronic Back Pain',
        'medications': ['Ibuprofen', 'Physical Therapy'],
        'last_visit_id': 'V2304',
    }
]

# একটি রোগীর তথ্য সঠিক কিনা যাচাই করার function
def find_invalid_records(
    patient_id, age, gender, diagnosis, medications, last_visit_id
):

    constraints = {  # প্রতিটি field-এর validation rule রাখা হয়েছে

        'patient_id': isinstance(patient_id, str)  # patient_id string কিনা
        and re.fullmatch('p\d+', patient_id, re.IGNORECASE),  # P এর পরে শুধু সংখ্যা আছে কিনা

        'age': isinstance(age, int) and age >= 18,  # বয়স integer এবং কমপক্ষে ১৮ কিনা

        'gender': isinstance(gender, str) and gender.lower() in ('male', 'female'),  # gender male/female কিনা

        'diagnosis': isinstance(diagnosis, str) or diagnosis is None,  # diagnosis string অথবা None কিনা

        'medications': isinstance(medications, list)  # medications list কিনা
        and all([isinstance(i, str) for i in medications]),  # list-এর প্রতিটি item string কিনা

        'last_visit_id': isinstance(last_visit_id, str)  # visit id string কিনা
        and re.fullmatch('v\d+', last_visit_id, re.IGNORECASE)  # V এর পরে সংখ্যা আছে কিনা
    }

    return [key for key, value in constraints.items() if not value]  # যেসব field invalid তাদের নাম list আকারে return


# পুরো medical_records validate করার function
def validate(data):

    is_sequence = isinstance(data, (list, tuple))  # data list অথবা tuple কিনা

    if not is_sequence:  # list/tuple না হলে
        print('Invalid format: expected a list or tuple.')
        return False

    is_invalid = False  # শুরুতে ধরা হচ্ছে কোনো error নেই

    key_set = set(  # প্রত্যেক dictionary-তে যে key গুলো থাকা বাধ্যতামূলক
        ['patient_id', 'age', 'gender', 'diagnosis', 'medications', 'last_visit_id']
    )

    for index, dictionary in enumerate(data):  # প্রতিটি record একে একে নেওয়া হচ্ছে

        if not isinstance(dictionary, dict):  # record dictionary কিনা
            print(f'Invalid format: expected a dictionary at position {index}.')
            is_invalid = True
            continue  # পরের record-এ চলে যাবে

        if set(dictionary.keys()) != key_set:  # key গুলো ঠিক আছে কিনা
            print(
                f'Invalid format: {dictionary} at position {index} has missing and/or invalid keys.'
            )
            is_invalid = True
            continue

        invalid_records = find_invalid_records(**dictionary)  # dictionary unpack করে validation function-এ পাঠানো

        for record in invalid_records:  # যতগুলো invalid field পাওয়া গেছে তাদের উপর loop
            print(f"Unexpected format '{record}: {dictionary[record]}' at position {index}.")  # error message দেখানো
            is_invalid = True

    if is_invalid:  # যদি কোনো error থাকে
        return False

    print('Valid format.')  # সব ঠিক থাকলে
    return True


validate(medical_records)  # function call করে সব data validate করা