from models.author import Author
from models.book import Book
from models.library_member import LibraryMember


def main():
    print("=" * 70)
    print("STUDI KASUS 2 - SISTEM PERPUSTAKAAN")
    print("=" * 70)
    
    # 1. Create authors
    print("\n1. MEMBUAT PENULIS")
    print("-" * 70)
    
    author1 = Author("Pramoedya Ananta Toer", 1925)
    author2 = Author("Andrea Hirata", 1967)
    author3 = Author("Dee Lestari", 1976)
    author4 = Author("Tere Liye", 1979)
    
    authors = [author1, author2, author3, author4]
    
    for author in authors:
        print(f"✓ {author.display_info()}")

    # 2. Create books
    print("\n2. MEMBUAT BUKU")
    print("-" * 70)
    
    books = [
        Book(101, "Bumi Manusia", author1, "978-0140256353"),
        Book(102, "Laskar Pelangi", author2, "978-9793062792"),
        Book(103, "Supernova: Kesatria, Puteri, dan Bintang Jatuh", author3, "978-9792228031"),
        Book(104, "Hafalan Shalat Delisa", author4, "978-9797808721"),
        Book(105, "Anak Semua Bangsa", author1, "978-0140256360"),
        Book(106, "Sang Pemimpi", author2, "978-9793062808")
    ]
    
    for book in books:
        print(f"✓ {book.get_book_info()}")

    # 3. Create library members
    print("\n3. MEMBUAT ANGGOTA PERPUSTAKAAN")
    print("-" * 70)
    
    member1 = LibraryMember(1001, "Ahmad Wijaya")
    member2 = LibraryMember(1002, "Sari Dewi")
    member3 = LibraryMember(1003, "Budi Pratama")
    
    members = [member1, member2, member3]
    
    for member in members:
        print(f"✓ {member.get_member_info()}")

    # 4. Demonstrate borrowing items
    print("\n4. DEMONSTRASI PEMINJAMAN BUKU")
    print("-" * 70)
    
    # Member 1 borrows books
    print(f"\n--- {member1.name} MEMINJAM BUKU ---")
    member1.borrow_item(books[0])  # Bumi Manusia
    member1.borrow_item(books[1])  # Laskar Pelangi
    member1.borrow_item(books[4])  # Anak Semua Bangsa
    
    # Member 2 borrows books
    print(f"\n--- {member2.name} MEMINJAM BUKU ---")
    member2.borrow_item(books[2])  # Supernova
    member2.borrow_item(books[3])  # Hafalan Shalat Delisa
    
    # Member 3 borrows books
    print(f"\n--- {member3.name} MEMINJAM BUKU ---")
    member3.borrow_item(books[5])  # Sang Pemimpi

    # 5. Display borrowed items
    print("\n5. DAFTAR BUKU YANG DIPINJAM")
    print("-" * 70)
    
    for member in members:
        member.display_borrowed_items()
        print()

    # 6. Demonstrate returning items
    print("\n6. DEMONSTRASI PENGEMBALIAN BUKU")
    print("-" * 70)
    
    print(f"\n--- {member1.name} MENGEMBALIKAN BUKU ---")
    member1.return_item(books[1])  # Return Laskar Pelangi
    
    print(f"\n--- {member2.name} MENGEMBALIKAN BUKU ---")
    member2.return_item(books[2])  # Return Supernova

    # Show updated borrowed items
    print("\n--- STATUS PEMINJAMAN SETELAH PENGEMBALIAN ---")
    for member in members:
        member.display_borrowed_items()
        print()

    # 7. Calculate late fees
    print("\n7. PERHITUNGAN DENDA KETERLAMBATAN")
    print("-" * 70)
    
    # Simulate late returns
    days_late_member1 = {101: 5, 104: 2}   # 5 days late for Bumi Manusia
    days_late_member2 = {103: 7}           # 7 days late for Hafalan Shalat Delisa
    days_late_member3 = {106: 10}          # 10 days late for Sang Pemimpi
    
    print(f"\n--- DENDA {member1.name} ---")
    total_fee1 = member1.calculate_total_late_fees(days_late_member1)
    print(f"   TOTAL DENDA: Rp {total_fee1:,.0f}")
    
    print(f"\n--- DENDA {member2.name} ---")
    total_fee2 = member2.calculate_total_late_fees(days_late_member2)
    print(f"   TOTAL DENDA: Rp {total_fee2:,.0f}")
    
    print(f"\n--- DENDA {member3.name} ---")
    total_fee3 = member3.calculate_total_late_fees(days_late_member3)
    print(f"   TOTAL DENDA: Rp {total_fee3:,.0f}")

    # 8. Test book information display
    print("\n8. INFORMASI DETAIL BUKU")
    print("-" * 70)
    
    print("\n--- INFORMASI BUKU 1 ---")
    books[0].display_info()
    
    print("\n--- INFORMASI BUKU 3 ---")
    books[2].display_info()

    # 9. Test abstract class implementation
    print("\n9. TEST ABSTRACT CLASS DAN POLYMORPHISM")
    print("-" * 70)
    
    # Test late fee calculation for different books
    test_books = [books[0], books[1], books[3]]
    test_days = [3, 0, 7]
    
    for book, days in zip(test_books, test_days):
        try:
            fee = book.calculate_late_fee(days)
            print(f"'{book.title}': {days} hari terlambat = Rp {fee:,.0f}")
        except ValueError as e:
            print(f"'{book.title}': Error - {e}")

    # 10. Final status
    print("\n10. STATUS AKHIR SISTEM")
    print("-" * 70)
    
    total_borrowed = sum(len(member.borrowed_items) for member in members)
    print(f"Total buku yang masih dipinjam: {total_borrowed}")
    print(f"Total anggota perpustakaan: {len(members)}")
    print(f"Total buku dalam katalog: {len(books)}")
    
    print("\n" + "=" * 70)
    print("SELESAI - STUDI KASUS 2")
    print("=" * 70)


if __name__ == "__main__":
    main()