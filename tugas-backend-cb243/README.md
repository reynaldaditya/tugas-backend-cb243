# Tugas 1 - CB243: Pengembangan Sistem Backend

**Nama:** I Nyoman Reynald Aditya Parmanda 
**NIM:** 240030245
**Kelas:** CB243  
**Mata Kuliah:** Pengembangan Sistem Backend

## Deskripsi Tugas
Implementasi dua studi kasus sistem menggunakan konsep Object-Oriented Programming (OOP) dalam Python murni tanpa framework sesuai dengan class diagram yang diberikan.

## Struktur Proyek
TUGAS-BACKEND-CB243/
├── studi-kasus-1/ # Sistem Akademik
│ ├── main.py
│ ├── models/
│ │ ├── init.py
│ │ ├── person.py
│ │ ├── student.py
│ │ ├── professor.py
│ │ └── address.py
├── studi-kasus-2/ # Sistem Perpustakaan
│ ├── main.py
│ ├── models/
│ │ ├── init.py
│ │ ├── library_item.py
│ │ ├── book.py
│ │ ├── author.py
│ │ └── library_member.py
├── requirements.txt
└── README.md 


## Cara Menjalankan

### Prerequisites
- Python 3.7 atau lebih tinggi
- Tidak memerlukan library external

### Studi Kasus 1 - Sistem Akademik

cd studikasus1
python main.py

### Studi Kasus 2 - Sistem Perpustakaan

cd studikasus2
python main.py

# Studi Kasus 1: Sistem Akademik
## Class Diagram Implementasi
Person
├── name: str
├── phone_number: str  
├── email_address: str
└── address: Address
    │
    ├── Student
    │   ├── student_number: int
    │   ├── average_mark: int
    │   ├── is_eligible_to_enroll()
    │   └── get_seminars_taken()
    │
    └── Professor
        ├── _staff_number: int (protected)
        ├── __years_of_service: int (private) 
        ├── number_of_classes: int
        ├── _salary: int (protected)
        ├── add_student()
        └── remove_student()

### Fitur Utama:

- Inheritance: Student dan Professor mewarisi dari Person

- Encapsulation: Attribute dengan visibility public, protected, dan private

- Relasi: Professor dapat mensupervisi maksimal 5 Student

- Method: Pembelian parking pass, validasi enrollment, manajemen kelas

Contoh Output Studi Kasus 1:

======================================================================
STUDI KASUS 1 - SISTEM AKADEMIK
======================================================================

1. MEMBUAT ALAMAT
----------------------------------------------------------------------
Address 1: Jl. Merdeka No.1, Jakarta, DKI Jakarta 10110, Indonesia
Address 2: Jl. Sudirman No.2, Bandung, Jawa Barat 40115, Indonesia
Address 3: Jl. Malioboro No.3, Yogyakarta, DI Yogyakarta 55212, Indonesia

2. DEMONSTRASI CLASS PERSON
----------------------------------------------------------------------
Person Created: Name: Reynald Aditya, Phone: 089654575895, Email: nyomanreynald803@gmail.com, Address: Jl. Merdeka No.1, Jakarta, DKI Jakarta 10110, Indonesia
Parking Pass: Reynald Aditya has purchased a parking pass.

3. DEMONSTRASI CLASS STUDENT
----------------------------------------------------------------------
Student 1: Name: Budi Santoso, Phone: 081234567890, Email: budi@stikom.edu, Address: Jl. Sudirman No.2, Bandung, Jawa Barat 40115, Indonesia | Student Number: 12345 | Average Mark: 85 | Seminars Taken: 0
Student 2: Name: Siti Aminah, Phone: 082345678901, Email: siti@stikom.edu, Address: Jl. Malioboro No.3, Yogyakarta, DI Yogyakarta 55212, Indonesia | Student Number: 67890 | Average Mark: 75 | Seminars Taken: 0
Student 3: Name: Andi Wijaya, Phone: 083456789012, Email: andi@stikom.edu, Address: Jl. Merdeka No.1, Jakarta, DKI Jakarta 10110, Indonesia | Student Number: 11223 | Average Mark: 65 | Seminars Taken: 0

--- TEST KELAYAKAN ENROLLMENT ---
Budi Santoso - Advanced Programming: Layak    
Siti Aminah - Introduction to Programming: Layak
Andi Wijaya - Advanced Mathematics: Tidak Layak

--- TEST SEMINAR ---
Seminars taken by Budi Santoso: 2
Seminars taken by Siti Aminah: 1

4. DEMONSTRASI CLASS PROFESSOR
----------------------------------------------------------------------
Professor Created: Name: Dr. Ahmad Fauzi, Phone: 085678901234, Email: ahmad@stikom.edu, Address: Jl. Sudirman No.2, Bandung, Jawa Barat 40115, Indonesia | Staff Number: 54321 | Years of Service: 10 | Classes: 0 | Salary: Rp10,000,000 | Supervising: 0 students
Initial Salary: Rp10,000,000

--- TEST SUPERVISI MAHASISWA ---
1. Menambah Budi Santoso: Berhasil
2. Menambah Siti Aminah: Berhasil
3. Menambah Andi Wijaya: Berhasil
4. Menambah Dewi Lestari: Berhasil
5. Menambah Rina Kartika: Berhasil
6. Menambah Tono Prabowo: Gagal (max 5 students)

--- TEST MANAJEMEN KELAS ---
Setelah menambah 3 kelas: 3 kelas

Mahasiswa yang disupervisi oleh Dr. Ahmad Fauzi:
  1. Budi Santoso (No: 12345, Mark: 85)       
  2. Siti Aminah (No: 67890, Mark: 75)        
  3. Andi Wijaya (No: 11223, Mark: 65)        
  4. Dewi Lestari (No: 33445, Mark: 90)       
  5. Rina Kartika (No: 55667, Mark: 88)       

--- TEST UPDATE MASA KERJA DAN GAJI ---       
Setelah 15 tahun kerja: Gaji = Rp12,500,000   

5. TESTING REPRESENTASI OBJEK
----------------------------------------------------------------------
Repr Student: Student(name='Budi Santoso', phone_number='081234567890', email_address='budi@stikom.edu', address=Address(street='Jl. Sudirman No.2', city='Bandung', state='Jawa Barat', postal_code='40115', country='Indonesia'), student_number=12345, average_mark=85, seminars_taken=2)
Repr Professor: Professor(name='Dr. Ahmad Fauzi', phone_number='085678901234', email_address='ahmad@stikom.edu', address=Address(street='Jl. Sudirman No.2', city='Bandung', state='Jawa Barat', postal_code='40115', country='Indonesia'), staff_number=54321, years_of_service=15, number_of_classes=3, salary=12500000)        
Repr Address: Address(street='Jl. Merdeka No.1', city='Jakarta', state='DKI Jakarta', postal_code='10110', country='Indonesia')

6. TEST PARKING PASS UNTUK SEMUA
----------------------------------------------------------------------
Person: Reynald Aditya has purchased a parking pass.
Student: Budi Santoso has purchased a parking pass.
Professor: Dr. Ahmad Fauzi has purchased a parking pass.

======================================================================
SELESAI - STUDI KASUS 1
======================================================================


# Studi Kasus 2: Sistem Perpustakaan
## Class Diagram Implementasi

LibraryItem (Abstract)
├── item_id: int
├── title: str
├── display_info() (abstract)
└── calculate_late_fee() (abstract)
    │
    └── Book
        ├── isbn: str
        ├── author: Author
        ├── display_info()
        └── calculate_late_fee()

Author
├── name: str
├── birth_year: int
└── get_age()

LibraryMember
├── member_id: int
├── name: str
├── borrowed_items: LibraryItem[]
├── borrow_item()
└── return_item()

### Fitur Utama:

- Abstraction: LibraryItem sebagai abstract base class

- Polymorphism: Method calculate_late_fee() diimplementasikan berbeda

- Composition: Book memiliki Author

- Aggregation: LibraryMember meminjam LibraryItem

### Contoh Output Studi Kasus 2:

======================================================================
STUDI KASUS 2 - SISTEM PERPUSTAKAAN
======================================================================

1. MEMBUAT PENULIS
----------------------------------------------------------------------
✓ Author: Pramoedya Ananta Toer (Born: 1925, Age: 100)
✓ Author: Andrea Hirata (Born: 1967, Age: 58) 
✓ Author: Dee Lestari (Born: 1976, Age: 49)   
✓ Author: Tere Liye (Born: 1979, Age: 46)     

2. MEMBUAT BUKU
----------------------------------------------------------------------
✓ Book 'Bumi Manusia' by Pramoedya Ananta Toer (ISBN: 978-0140256353)
✓ Book 'Laskar Pelangi' by Andrea Hirata (ISBN: 978-9793062792)
✓ Book 'Supernova: Kesatria, Puteri, dan Bintang Jatuh' by Dee Lestari (ISBN: 978-9792228031)
✓ Book 'Hafalan Shalat Delisa' by Tere Liye (ISBN: 978-9797808721)
✓ Book 'Anak Semua Bangsa' by Pramoedya Ananta Toer (ISBN: 978-0140256360)
✓ Book 'Sang Pemimpi' by Andrea Hirata (ISBN: 978-9793062808)

3. MEMBUAT ANGGOTA PERPUSTAKAAN
----------------------------------------------------------------------
✓ Member 1001: Ahmad Wijaya (0 items borrowed)
✓ Member 1002: Sari Dewi (0 items borrowed)   
✓ Member 1003: Budi Pratama (0 items borrowed)

4. DEMONSTRASI PEMINJAMAN BUKU
----------------------------------------------------------------------

--- Ahmad Wijaya MEMINJAM BUKU ---
✅ Ahmad Wijaya successfully borrowed 'Bumi Manusia'
✅ Ahmad Wijaya successfully borrowed 'Laskar Pelangi'
✅ Ahmad Wijaya successfully borrowed 'Anak Semua Bangsa'

--- Sari Dewi MEMINJAM BUKU ---
✅ Sari Dewi successfully borrowed 'Supernova: Kesatria, Puteri, dan Bintang Jatuh'
✅ Sari Dewi successfully borrowed 'Hafalan Shalat Delisa'

--- Budi Pratama MEMINJAM BUKU ---
✅ Budi Pratama successfully borrowed 'Sang Pemimpi'

5. DAFTAR BUKU YANG DIPINJAM
----------------------------------------------------------------------
📚 Ahmad Wijaya's borrowed items (3 items):   
  1. Bumi Manusia (ID: 101)
  2. Laskar Pelangi (ID: 102)
  3. Anak Semua Bangsa (ID: 105)

📚 Sari Dewi's borrowed items (2 items):      
  1. Supernova: Kesatria, Puteri, dan Bintang Jatuh (ID: 103)
  2. Hafalan Shalat Delisa (ID: 104)

📚 Budi Pratama's borrowed items (1 items):   
  1. Sang Pemimpi (ID: 106)


6. DEMONSTRASI PENGEMBALIAN BUKU
----------------------------------------------------------------------

--- Ahmad Wijaya MENGEMBALIKAN BUKU ---       
✅ Ahmad Wijaya successfully returned 'Laskar Pelangi'

--- Sari Dewi MENGEMBALIKAN BUKU ---
✅ Sari Dewi successfully returned 'Supernova: Kesatria, Puteri, dan Bintang Jatuh'

--- STATUS PEMINJAMAN SETELAH PENGEMBALIAN ---
📚 Ahmad Wijaya's borrowed items (2 items):   
  1. Bumi Manusia (ID: 101)
  2. Anak Semua Bangsa (ID: 105)

📚 Sari Dewi's borrowed items (1 items):      
  1. Hafalan Shalat Delisa (ID: 104)

📚 Budi Pratama's borrowed items (1 items):   
  1. Sang Pemimpi (ID: 106)


7. PERHITUNGAN DENDA KETERLAMBATAN
----------------------------------------------------------------------

--- DENDA Ahmad Wijaya ---
   - 'Bumi Manusia': 5 days late = Rp 10,000  
   TOTAL DENDA: Rp 10,000

--- DENDA Sari Dewi ---
   TOTAL DENDA: Rp 0

--- DENDA Budi Pratama ---
   - 'Sang Pemimpi': 10 days late = Rp 20,000 
   TOTAL DENDA: Rp 20,000

8. INFORMASI DETAIL BUKU
----------------------------------------------------------------------

--- INFORMASI BUKU 1 ---
Book ID: 101
Title: Bumi Manusia
Author: Pramoedya Ananta Toer
ISBN: 978-0140256353
Author Info: Author: Pramoedya Ananta Toer (Born: 1925, Age: 100)

--- INFORMASI BUKU 3 ---
Book ID: 103
Title: Supernova: Kesatria, Puteri, dan Bintang Jatuh
Author: Dee Lestari
ISBN: 978-9792228031
Author Info: Author: Dee Lestari (Born: 1976, Age: 49)

9. TEST ABSTRACT CLASS DAN POLYMORPHISM       
----------------------------------------------------------------------
'Bumi Manusia': 3 hari terlambat = Rp 6,000   
'Laskar Pelangi': 0 hari terlambat = Rp 0     
'Hafalan Shalat Delisa': 7 hari terlambat = Rp 14,000

10. STATUS AKHIR SISTEM
----------------------------------------------------------------------
Total buku yang masih dipinjam: 4
Total anggota perpustakaan: 3
Total buku dalam katalog: 6

======================================================================
SELESAI - STUDI KASUS 2
======================================================================

# Proses Berpikir dan Analisis

## Analisis UML dan Design Decisions

### Studi Kasus 1 - Sistem Akademik:
- Identifikasi Inheritance Hierarchy: Person sebagai base class dengan Student dan Professor sebagai subclass

- Relasi Object: Professor memiliki relasi "supervises" dengan Student (1..5) diimplementasikan sebagai list dengan validasi kapasitas

### Encapsulation:

- Protected attributes menggunakan prefix _ (_staff_number, _salary)
- Private attributes menggunakan prefix __ (__years_of_service)

### Business Logic:

- Validasi average mark antara 0-100
- Batas maksimal 5 students per professor
- Perhitungan salary otomatis berdasarkan years_of_service

### Studi Kasus 2 - Sistem Perpustakaan:
- Abstract Class Pattern: LibraryItem sebagai abstract base class dengan method abstract display_info() dan calculate_late_fee()
- Composition: Book memiliki Author sebagai komposisi wajib
- Aggregation: LibraryMember memiliki borrowed_items sebagai aggregation (bisa kosong)

### Polymorphism:

> Method calculate_late_fee() memiliki implementasi berbeda

> Method display_info() dioverride di subclass

- Type Hints: Penggunaan extensive type hints untuk maintainability

## Tantangan dan Solusi yang Diatasi

### Circular Import Issues

- Masalah: Student dan Professor saling referensi
- Solusi: Menggunakan from __future__ import annotations dan TYPE_CHECKING

### Abstract Class Implementation

- Masalah: Python tidak memiliki abstract class native
- Solusi: Menggunakan ABC module dari Python standard library

### Data Integrity

- Masalah: Validasi input dan business rules
- Solusi: Implementasi error handling dan validation methods

### UML Compliance

- Masalah: Attribute visibility sesuai notasi UML
- Solusi: Implementasi public, protected, private dengan Python convention

# Dokumentasi Penggunaan AI

## Prompt 1: Analisis Awal Requirements
Reynald: "Tolong bantu analisis Tugas berikut [File tugas.pdf]"
AI Response: Memberikan breakdown lengkap struktur tugas, analisis requirement OOP, dan identifikasi key components untuk kedua studi kasus.

## Prompt 2: Code Review Studi Kasus 1
Reynald:"Saya sudah membuatnya , tolong di review [File code.py]"
AI Response: Melakukan review menyeluruh, mengidentifikasi:
- Ketidaksesuaian dengan UML (adanya attribute 'age' yang tidak ada di diagram)
- Visibility attributes yang perlu disesuaikan
- Saran improvement untuk encapsulation dan type safety

## Prompt 3: Penutup
Reynald:"Baik, Terimakasih atas bantuannya selama mengerjakan tugas ini. dan semua sudah berjalan dengan normal "
AI Response:"Waaa mantap kali Mang Reynald! 🔥😎
Congrats! Tugas backend done, GitHub jalan, VSCode nyambung, dan kamu berhasil ngelewatin hal yang biasanya bikin banyak orang ambyar pertama kali belajar.

Progress kayak gini bukti kamu makin naik level—pelan tapi konsisten, dan itu yang bikin kuat. 🚀

Kalau nanti ada tugas lain, proyek, atau mau lanjut roadmap belajarnya, panggil aja SageAI.
Santai... kita gas terus petualangan Mang Rey sebagai si kelelawar network-engineer + AI adventurer 🦇💻✨

Bangga sama progress-mu hari ini!"

# Etika Penggunaan AI:
- AI digunakan sebagai asisten analisis dan code review tool
- Semua kode dipahami sepenuhnya dan melalui proses modifikasi sesuai kebutuhan
- Dokumentasi proses berpikir ditulis secara mandiri
- Konsep OOP diterapkan dengan pemahaman penuh

# Konsep OOP yang Diimplementasikan

# Protected attribute
self._staff_number

# Private attribute  
self.__years_of_service

# Public method dengan validation
def update_average_mark(self, new_mark: int) -> None:
    if 0 <= new_mark <= 100:
        self.average_mark = new_mark

# Inheritance
# Student mewarisi Person
class Student(Person):

# Book mewarisi LibraryItem  
class Book(LibraryItem):

# Polymorphism
# Abstract method yang diimplementasikan berbeda
def calculate_late_fee(self, days_late: int) -> float:
    # Implementasi berbeda di setiap subclass
    
# Abstraction
# Abstract base class
class LibraryItem(ABC):
    @abstractmethod
    def display_info(self) -> None:
        pass

# Teknologi dan Tools
- Programming Language: Python 3.7+
- Paradigm: Object-Oriented Programming (OOP)
- Tools: Standard Library Python (abc, typing, datetime)
- Development: Visual Studio Code, Git & GitHub
- Documentation: Markdown

# Hasil Pembelajaran
## Technical Skills:
- Penerapan 4 pilar OOP dalam scenario nyata
- Implementasi UML class diagram ke dalam code
- Management complex object relationships
- Python specific features (ABC, type hints, properties)
## Soft Skills:
- Analytical thinking dalam menganalisis requirements
- Problem solving untuk mengatasi technical challenges
- Documentation best practices
- Version control dengan Git

# Hasil dan Demonstrasi
Kedua sistem berhasil diimplementasikan dengan:'
- 100% Compliance dengan UML diagram
- Clean Architecture dan separation of concerns
- Comprehensive Documentation
- Error Handling dan data validation
- Demonstrable Features dengan main.py