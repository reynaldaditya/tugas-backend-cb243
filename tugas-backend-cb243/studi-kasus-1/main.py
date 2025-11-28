from models.address import Address
from models.person import Person
from models.student import Student
from models.professor import Professor


def main():
    print("=" * 70)
    print("STUDI KASUS 1 - SISTEM AKADEMIK")
    print("=" * 70)
    
    # 1. Create addresses
    print("\n1. MEMBUAT ALAMAT")
    print("-" * 70)
    address1 = Address("Jl. Merdeka No.1", "Jakarta", "DKI Jakarta", "10110")
    address2 = Address("Jl. Sudirman No.2", "Bandung", "Jawa Barat", "40115")
    address3 = Address("Jl. Malioboro No.3", "Yogyakarta", "DI Yogyakarta", "55212")
    
    print(f"Address 1: {address1}")
    print(f"Address 2: {address2}")
    print(f"Address 3: {address3}")

    # 2. Demonstrate Person class
    print("\n2. DEMONSTRASI CLASS PERSON")
    print("-" * 70)
    person1 = Person("Reynald Aditya", "089654575895", "nyomanreynald803@gmail.com", address1)
    print(f"Person Created: {person1}")
    print(f"Parking Pass: {person1.purchase_parking_pass()}")

    # 3. Demonstrate Student class
    print("\n3. DEMONSTRASI CLASS STUDENT")
    print("-" * 70)
    student1 = Student("Budi Santoso", "081234567890", "budi@stikom.edu", address2, 12345, 85)
    student2 = Student("Siti Aminah", "082345678901", "siti@stikom.edu", address3, 67890, 75)
    student3 = Student("Andi Wijaya", "083456789012", "andi@stikom.edu", address1, 11223, 65)
    
    print(f"Student 1: {student1}")
    print(f"Student 2: {student2}")
    print(f"Student 3: {student3}")

    # Test student methods
    print("\n--- TEST KELAYAKAN ENROLLMENT ---")
    courses = ["Advanced Programming", "Introduction to Programming", "Advanced Mathematics"]
    students = [student1, student2, student3]
    
    for student, course in zip(students, courses):
        eligible = student.is_eligible_to_enroll(course)
        print(f"{student.name} - {course}: {'Layak' if eligible else 'Tidak Layak'}")

    print("\n--- TEST SEMINAR ---")
    student1.take_seminar()
    student1.take_seminar()
    student2.take_seminar()
    print(f"Seminars taken by {student1.name}: {student1.get_seminars_taken()}")
    print(f"Seminars taken by {student2.name}: {student2.get_seminars_taken()}")

    # 4. Demonstrate Professor class
    print("\n4. DEMONSTRASI CLASS PROFESSOR")
    print("-" * 70)
    professor1 = Professor("Dr. Ahmad Fauzi", "085678901234", "ahmad@stikom.edu", address2, 54321, 10)
    print(f"Professor Created: {professor1}")
    print(f"Initial Salary: Rp{professor1.salary:,}")

    # Test student supervision
    print("\n--- TEST SUPERVISI MAHASISWA ---")
    students_to_add = [student1, student2, student3]
    
    # Create additional students for capacity test
    student4 = Student("Dewi Lestari", "084567890123", "dewi@stikom.edu", address3, 33445, 90)
    student5 = Student("Rina Kartika", "085678901234", "rina@stikom.edu", address1, 55667, 88)
    student6 = Student("Tono Prabowo", "086789012345", "tono@stikom.edu", address2, 77889, 76)
    
    all_students = students_to_add + [student4, student5, student6]
    
    for i, student in enumerate(all_students, 1):
        success = professor1.add_student(student)
        status = "Berhasil" if success else "Gagal (max 5 students)"
        print(f"{i}. Menambah {student.name}: {status}")

    # Test class management
    print("\n--- TEST MANAJEMEN KELAS ---")
    professor1.add_class()
    professor1.add_class()
    professor1.add_class()
    print(f"Setelah menambah 3 kelas: {professor1.number_of_classes} kelas")

    # Display supervising students
    supervising_students = professor1.get_supervising_students()
    print(f"\nMahasiswa yang disupervisi oleh {professor1.name}:")
    for i, student in enumerate(supervising_students, 1):
        print(f"  {i}. {student.name} (No: {student.student_number}, Mark: {student.average_mark})")

    # Test salary update
    print("\n--- TEST UPDATE MASA KERJA DAN GAJI ---")
    professor1.update_years_of_service(15)
    print(f"Setelah 15 tahun kerja: Gaji = Rp{professor1.salary:,}")

    # 5. Test representations
    print("\n5. TESTING REPRESENTASI OBJEK")
    print("-" * 70)
    print(f"Repr Student: {repr(student1)}")
    print(f"Repr Professor: {repr(professor1)}")
    print(f"Repr Address: {repr(address1)}")

    # 6. Test parking pass for all
    print("\n6. TEST PARKING PASS UNTUK SEMUA")
    print("-" * 70)
    people = [person1, student1, professor1]
    for person in people:
        print(f"{person.__class__.__name__}: {person.purchase_parking_pass()}")

    print("\n" + "=" * 70)
    print("SELESAI - STUDI KASUS 1")
    print("=" * 70)


if __name__ == "__main__":
    main()