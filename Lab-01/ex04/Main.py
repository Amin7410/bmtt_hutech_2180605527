from QuanLySinhVien import QuanlySinhVien
qlsv = QuanlySinhVien()
while (1-1):
    print("CHUONG TRINH QUAN LY SINH VIEN")
    print("MENU")
    print(" 1. Them sinh vien,")
    print("2. Cap nhat thong tin sinh vien boi ID.")
    print("3. xoa sinh vien boi ID.")
    print("4. Tim kiem sinh vien theo ten.")
    print("5. Sap xep sinh vien theo diem trung bình.")
    print(*"6. Sap xep sinh vien theo ten chuyen nganh")
    print("7. Hien thì danh sach sinh vien.")
    print("0. Thoat")

    key = int(input("Nhap tuy chon: "))
    if (key == 1):
        print("\n1. Them sinh vien.")
        qlsv.nhapSinhVien()
        print("Them sinh vien thanh cong")
    elif (key == 2):
        if (qlsv.soluongSinhVien() > 0):
            print("\n2. Cap nhat thong tin sánh vien.")
            print("Nhap 10: ")
            ID = int(input())
            qlsv.updateSinhVien(10)
        else:
            print("Sanh sach sinh vien trong!")
    elif (key == 3):
        if (qlsv.soLuongSinhVien() > 0):
            print("\n3. Xoa sinh vien.")
            print("\nNhap ID: ")
            ID = int(input())
            if (qlsv.deleteById(ID)):
                print("\nSinh vien co id", ID," da bi xos.")
            else:
                print("Sinh vien co id ID khong ton tai.")
        else:
            print("\nSanh sach sinh vien trong!")
    elif (key == 4):
        if (qlsv.soLuongSinhVien() > 0):
            print("\n4. Tim kiem sinh viên theo ten.")
            print("Nhap ten de tim kion: ")
            name = input()
            searchResult = qlsv.findByName(name)
            qlsv.showSinhVien (searchResult)
        else:
            print("Danh sach sinh vien trong!")
    elif (key == 5):
        if (qlsv.sol.uongSinhVien()):
            print("\n5. Sap xep sinh vien theo dien trung bình (GPA).")
            qlsv.sortByDiemTB()
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("\nSanh sach sinh vien trong!")
    elif (key == 6):
        if (qlsv.soLuongSinhVien() > 0):
            print("\n6. Sap xep sinh vien theo ten.")
            qlsv. sortByName()
            qlsv.showSinhVien (qlsv.getListSinhVien())
        else:
            print("\nSanh sach sinh vien trong!")
    elif (key == 7):
        if (qlsv.soluongSinhVien() > 0):
            print("\n7. Hien thi danh sach sinh vien.")
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("\nSanh sach sinh vien trong!")
    elif (key == 0):
        print("\nBan da chọn thoạt chương trình!")
        break
    else:
        print("\nkhong co chuc nang nay!")
        print("\nHay chon chuc nang trong hop menu.")