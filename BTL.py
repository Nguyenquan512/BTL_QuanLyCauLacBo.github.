import json
import os
ds_caulacbo = {}
ds_thanhvien = {}
ds_sukien = {}

def them_clb():
    id = int(input("Nhập ID CLB: "))
    if id in ds_caulacbo:
        print("ID đã tồn tại.")
        return
    ten = input("Tên CLB: ")
    mota = input("Mô tả: ")
    ds_caulacbo[id] = {"ten": ten, "mota": mota, "thanhvien": []}
    print("Đã thêm câu lạc bộ.")

def xem_ds_clb():
    if not ds_caulacbo:
        print("Chưa có CLB nào.")
        return
    for id, clb in ds_caulacbo.items():
        print(f"ID: {id} | Tên: {clb['ten']} | Mô tả: {clb['mota']}")

def capnhat_clb():
    id = int(input("Nhập ID CLB: "))
    if id not in ds_caulacbo:
        print("Không tìm thấy CLB.")
        return
    ten = input("Tên mới: ")
    mota = input("Mô tả mới: ")
    ds_caulacbo[id]["ten"] = ten
    ds_caulacbo[id]["mota"] = mota
    print("Đã cập nhật CLB.")

def xoa_clb():
    id = int(input("Nhập ID CLB: "))
    if id in ds_caulacbo:
        del ds_caulacbo[id]
        print("Đã xoá CLB.")
    else:
        print("Không tìm thấy CLB.")

def them_thanhvien():
    id = int(input("Nhập ID thành viên: "))
    if id in ds_thanhvien:
        print("ID đã tồn tại.")
        return
    ten = input("Tên thành viên: ")
    email = input("Email: ")
    ds_thanhvien[id] = {"ten": ten, "email": email, "clb": []}
    print("Đã thêm thành viên.")

def xem_ds_thanhvien():
    if not ds_thanhvien:
        print("Chưa có thành viên nào.")
        return
    for id, tv in ds_thanhvien.items():
        print(f"ID: {id} | Tên: {tv['ten']} | Email: {tv['email']}")

def capnhat_thanhvien():
    id = int(input("ID thành viên: "))
    if id not in ds_thanhvien:
        print("Không tìm thấy thành viên.")
        return
    ten = input("Tên mới: ")
    email = input("Email mới: ")
    ds_thanhvien[id]["ten"] = ten
    ds_thanhvien[id]["email"] = email
    print("Đã cập nhật thành viên.")

def xoa_thanhvien():
    id = int(input("ID thành viên: "))
    if id in ds_thanhvien:
        del ds_thanhvien[id]
        print("Đã xoá thành viên.")
    else:
        print("Không tìm thấy thành viên.")

def gan_tv_vao_clb():
    idtv = int(input("ID thành viên: "))
    idclb = int(input("ID CLB: "))
    if idtv in ds_thanhvien and idclb in ds_caulacbo:
        ds_thanhvien[idtv]["clb"].append(idclb)
        ds_caulacbo[idclb]["thanhvien"].append(idtv)
        print("Đã gán thành viên vào CLB.")
    else:
        print("ID không hợp lệ.")

def xem_tv_clb():
    idclb = int(input("ID CLB: "))
    if idclb not in ds_caulacbo:
        print("Không tìm thấy CLB.")
        return
    print(f"Danh sách thành viên của CLB {ds_caulacbo[idclb]['ten']}:")
    for idtv in ds_caulacbo[idclb]["thanhvien"]:
        print(f"- {ds_thanhvien[idtv]['ten']} ({ds_thanhvien[idtv]['email']})")

def tao_sukien():
    id = int(input("Nhập ID sự kiện: "))
    if id in ds_sukien:
        print("ID đã tồn tại.")
        return
    ten = input("Tên sự kiện: ")
    ngay = input("Ngày tổ chức (YYYY-MM-DD): ")
    idclb = int(input("ID CLB tổ chức: "))
    if idclb not in ds_caulacbo:
        print("Không tìm thấy CLB.")
        return
    ds_sukien[id] = {"ten": ten, "ngay": ngay, "id_clb": idclb, "nguoithamgia": []}
    print("Đã tạo sự kiện.")

def xem_ds_sukien():
    if not ds_sukien:
        print("Chưa có sự kiện nào.")
        return
    for id, sk in ds_sukien.items():
        clb_ten = ds_caulacbo[sk["id_clb"]]["ten"]
        print(f"ID: {id} | Tên: {sk['ten']} | Ngày: {sk['ngay']} | CLB tổ chức: {clb_ten}")

def capnhat_sukien():
    id = int(input("ID sự kiện: "))
    if id not in ds_sukien:
        print("Không tìm thấy sự kiện.")
        return
    ten = input("Tên mới: ")
    ngay = input("Ngày mới: ")
    ds_sukien[id]["ten"] = ten
    ds_sukien[id]["ngay"] = ngay
    print("Đã cập nhật sự kiện.")

def xoa_sukien():
    id = int(input("ID sự kiện: "))
    if id in ds_sukien:
        del ds_sukien[id]
        print("Đã xoá sự kiện.")
    else:
        print("Không tìm thấy sự kiện.")

def dang_ky_sukien():
    idtv = int(input("ID thành viên: "))
    idsk = int(input("ID sự kiện: "))
    if idtv in ds_thanhvien and idsk in ds_sukien:
        ds_sukien[idsk]["nguoithamgia"].append(idtv)
        print("Đã đăng ký sự kiện.")
    else:
        print("ID không hợp lệ.")

def xem_nguoithamgia():
    idsk = int(input("ID sự kiện: "))
    if idsk not in ds_sukien:
        print("Không tìm thấy sự kiện.")
        return
    print(f"Danh sách người tham gia sự kiện {ds_sukien[idsk]['ten']}:")
    for idtv in ds_sukien[idsk]["nguoithamgia"]:
        print(f"- {ds_thanhvien[idtv]['ten']}")

def tim_clb_theo_ten():
    keyword = input("Nhập từ khoá: ").lower()
    found = False
    for id, clb in ds_caulacbo.items():
        if keyword in clb["ten"].lower():
            print(f"ID: {id} | Tên: {clb['ten']}")
            found = True
    if not found:
        print("Không tìm thấy CLB.")

def tim_thanhvien_theo_email():
    email = input("Nhập email: ")
    for id, tv in ds_thanhvien.items():
        if tv["email"] == email:
            print(f"ID: {id} | Tên: {tv['ten']}")
            return
    print("Không tìm thấy thành viên.")

def thong_ke_so_luong():
    print(f"Số lượng CLB: {len(ds_caulacbo)}")
    print(f"Số lượng thành viên: {len(ds_thanhvien)}")
    print(f"Số lượng sự kiện: {len(ds_sukien)}")

def luu_du_lieu():
    with open("clb_data.json", "w", encoding="utf-8") as f:
        json.dump({
            "ds_caulacbo": ds_caulacbo,
            "ds_thanhvien": ds_thanhvien,
            "ds_sukien": ds_sukien,
            "id_tv": id_tv,
            "id_clb": id_clb,
            "id_sk": id_sk
        }, f, ensure_ascii=False, indent=2)
    print("Đã lưu dữ liệu ra file clb_data.json.")

def doc_du_lieu():
    global ds_caulacbo, ds_thanhvien, ds_sukien, id_tv, id_clb, id_sk
    if not os.path.exists("clb_data.json"):
        print("Không tìm thấy file dữ liệu.")
        return
    with open("clb_data.json", "r", encoding="utf-8") as f:
        data = json.load(f)
        ds_caulacbo = data.get("ds_caulacbo", {})
        ds_thanhvien = data.get("ds_thanhvien", {})
        ds_sukien = data.get("ds_sukien", {})
        id_tv = data.get("id_tv", 1)
        id_clb = data.get("id_clb", 1)
        id_sk = data.get("id_sk", 1)
    print("Đã đọc dữ liệu từ file.")

def ket_thuc():
    print("Tạm biệt!")
    exit()

def menu():
    while True:
        print("\n======= MENU QUẢN LÝ CÂU LẠC BỘ =======")
        print("1. Thêm câu lạc bộ")
        print("2. Xem danh sách câu lạc bộ")
        print("3. Cập nhật câu lạc bộ")
        print("4. Xoá câu lạc bộ")
        print("5. Thêm thành viên")
        print("6. Xem danh sách thành viên")
        print("7. Cập nhật thành viên")
        print("8. Xoá thành viên")
        print("9. Gán thành viên vào CLB")
        print("10. Xem thành viên của CLB")
        print("11. Tạo sự kiện")
        print("12. Xem sự kiện")
        print("13. Cập nhật sự kiện")
        print("14. Xoá sự kiện")
        print("15. Đăng ký tham gia sự kiện")
        print("16. Xem người tham gia sự kiện")
        print("17. Tìm CLB theo tên")
        print("18. Tìm thành viên theo email")
        print("19. Thống kê số lượng")
        print("20. Lưu dữ liệu ra file JSON")
        print("21. Đọc dữ liệu từ file JSON")
        print("22. Thoát")

        try:
            chon = int(input("Nhập lựa chọn (1-20): "))
            if chon == 1:
                them_clb()
            elif chon == 2:
                xem_ds_clb()
            elif chon == 3:
                capnhat_clb()
            elif chon == 4:
                xoa_clb()
            elif chon == 5:
                them_thanhvien()
            elif chon == 6:
                xem_ds_thanhvien()
            elif chon == 7:
                capnhat_thanhvien()
            elif chon == 8:
                xoa_thanhvien()
            elif chon == 9:
                gan_tv_vao_clb()
            elif chon == 10:
                xem_tv_clb()
            elif chon == 11:
                tao_sukien()
            elif chon == 12:
                xem_ds_sukien()
            elif chon == 13:
                capnhat_sukien()
            elif chon == 14:
                xoa_sukien()
            elif chon == 15:
                dang_ky_sukien()
            elif chon == 16:
                xem_nguoithamgia()
            elif chon == 17:
                tim_clb_theo_ten()
            elif chon == 18:
                tim_thanhvien_theo_email()
            elif chon == 19:
                thong_ke_so_luong()
            elif chon == 21:
                luu_du_lieu()
            elif chon == 22:
                doc_du_lieu()
            elif chon == 20:
                ket_thuc()
            else:
                print("Lựa chọn không hợp lệ.")
        except ValueError:
            print("Vui lòng nhập số hợp lệ.")

menu()