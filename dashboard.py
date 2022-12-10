import requests

############# Class Student To store details inside it ###########
class Student:
    def __init__(self, id, full_name, age, level, mobile_number):
        self.id = id
        self.full_name = full_name
        self.age = age
        self.level = level
        self.mobile_number = mobile_number


######### Student List #############
students = []

# isinstance function Return whether an object is an instance of a class or of a subclass thereof.

######## Regester Student Function #########
def regester_student():
    full_name = None
    age = ""
    level = ""
    mobile_number = None
    while not isinstance(full_name, str) or full_name == "":
        full_name = input("Enter Student Full Name: ")

    while (f"{level}").upper() not in ["A", "B", "C"]:
        level = input("Enter Student Level (A, B, C): ")

    while not isinstance(age, int):
        try:
            age = int(input("Enter Student age: "))
        except:
            print("error input \n Enter number value !")

    while not isinstance(mobile_number, str) or mobile_number == "":
        mobile_number = input("Enter Student Mobile number: ")
    data = {
            "full_name": full_name,
            "age": age,
            "level": level,
            "mobile_number": mobile_number
        }
    url = "http://staging.bldt.ca/api/method/build_it.test.register_student"
    result = requests.post(url, json=data)
    result_json = result.json()
    if result_json.get("status", False):
            print(result_json.get("message", "Student Registerd!"))
            data = result_json.get("data")
            if data:
                data.update({
                    "level": level
                })
                student_obj = Student(**data)
                return student_obj
            else:
                print("There is an problem")
    else:
            print(result_json.get("message", "Faield to Register"))
    

  ####### delete student by id ##########


def delete_student_from_list(id):
    new_list = []
    for student in students:
        if student.id != id:
            new_list.append(student)
    student = new_list

####### check student by id ##########


def check_student_by_id(id):
    for student in students:
        if student.id == id:
            return student
    return None

#############  Edit Student Function  #############


def edit_student():
    id = None
    id = input("Enter Student id to edit: ")
    student = check_student_by_id(id)
    if not student:
        print("Student not found!")
        return
    data = {
        "id": id,
        "full_name": student.full_name,
        "age": student.age,
        "level": student.level,
        "mobile_number": student.mobile_number
    }
        # enter and check full name
    full_name = input("Enter Student Full Name: ")
    if isinstance(full_name, str) and full_name != "":
        data.update({
            "full_name": full_name
        })
            # enter and check student level

    level = input("Enter Student Level [A, B, C]: ")
    if f"{level}".upper() in ["A", "B", "C"]:
        data.update({
            "level": f"{level}".upper()
        })
            # enter and check age
        age = int(input("Enter Student age: "))
        if age > 0:
            data.update({
                "age": age
            })
    
    # enter and check mobile number
    mobile_number = input("Enter Student Mobile no.: ")
    if isinstance(mobile_number, str) and mobile_number != "":
        data.update({
            "mobile_number": mobile_number
        })

        print(data)
        url = "http://staging.bldt.ca/api/method/build_it.test.edit_student"
        result = requests.put(url, json=data)
        result_json = result.json()
        if result_json.get("status", False):
            print(result_json.get("message", "Edit Done!"))
            data = result_json.get("data")
            if data:
                data.update({
                    "level": level
                })
                    # store student data
                student.full_name = data.get("full_name")
                student.age = data.get("age")
                student.level = data.get("full_name")
                student.mobile_number = data.get("mobile_number")
                return student
            else:
                print("Something went wrong!")
        else:
            print(result_json.get("message", "Faield to Edit"))


#############  Delete Student Function  #############
def delete_student():
    id = None
    id = input("Enter Student id to delete it: ")
    student = check_student_by_id(id)
    if not student:
        print("Student not found!")
        return

    data = {
        "id": id
    }
    url = "http://staging.bldt.ca/api/method/build_it.test.delete_student"
    result = requests.put(url, json=data)
    result_json = result.json()
    if result_json.get("status", False):
        print(result_json.get("message", "Success!"))
        delete_student_from_list(id)
    else:
        print(result_json.get("message", "Faield to delete!"))


########## Export Students To text File ############


def export_students_to_text_file():

    url = "http://staging.bldt.ca/api/method/build_it.test.get_students"
    result = requests.get(url)
    result_json = result.json()
    if result_json.get("status", False):
        print(result_json.get("message", "fetch data!"))
        result = result_json.get("data", [])
        all_stds_file = open("/Users/pc/Desktop/practicalTask/all_studetns.txt", "w")
        for res in result:
            id = res.get("id", "")
            full_name = res.get("full_name", "")
            mobile_number = res.get("mobile_number", "")
            age = res.get("age", "")
            level = res.get("level", "")
            all_stds_file.write(f"student Id :{id} / student Name : {full_name} / student mobile_num :{mobile_number} / student age :{age} / student level :{level}\n")
        all_stds_file.close()

    else:
        print(result_json.get("message", "Faield to fetch data"))


########## Export Student details To text File ############
def export_student_details_to_file():
    id = None
    while not isinstance(id, str) or id == "":
        id = input("Enter Student id to export: ")
    data = {
        "id": id
    }
    url = "http://staging.bldt.ca/api/method/build_it.test.get_student_details"
    result = requests.get(url, json=data)
    result_json = result.json()
    if result_json.get("status", False):
        print(result_json.get("message", "fetch data!"))
        rg = result_json.get("data")
        if not rg:
            print("Error")
            return
        details = open(f"/Users/pc/Desktop/practicalTask/std-details{id}.txt", "w")
        id = rg.get("id", "")
        full_name = rg.get("full_name", "")
        mobile_number = rg.get("mobile_number", "")
        age = rg.get("age", "")
        level = rg.get("level", "")
        details.write(f"student Id :{id} / student Name : {full_name} / student mobile_num :{mobile_number} / student age :{age} / student level :{level}\n")
        details.close()

    else:
        print(result_json.get("message", "Faield to fetch data"))


########### main dashboard ############
if __name__ == "__main__":
    while True:
        print("\nStudent formation system")
        print("----------------------------------------")
        print("1. Regsiter new student")
        print("2. Edit student Details")
        print("3. Delete student")
        print("4. Export students to text file")
        print("5. Export student details to text file")
        print("6. Exit :)")
        print("----------------------------------------")
        option = input("\t Your Option is : ")

        ####### switch case for choosen #######
        if option == "1":
            new_student = regester_student()
            students.append(new_student)
        if option == "2":
            new_student = edit_student()
        if option == "3":
            edited_student = delete_student()
        if option == "4":
            edited_student = export_students_to_text_file()
        if option == "5":
            edited_student = export_student_details_to_file()
        if option == "6":
            break
