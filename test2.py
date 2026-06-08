football_list = [
    {
    "id": "CT007",
    "name": "Nguyen Quang Hai",
    "total_match": 10,
    "goal": 5,
    "assist": 4,
    "effect": 33,
    "rank": "Trụ cột đội bóng"
    }
]

def validate_id(id, list):
    for player in list:
        if player["id"] == id:
            return player
    return None

def phan_loai_phong_do(point):
    if point >= 50:
        return "Ngôi sao đẳng cấp"
    elif point >= 30 and point < 50:
        return "Trụ cột đội bóng"
    elif point >= 15 and point < 30:
        return "Dự bị chiến lược"
    else:
        return "Cần thanh lý / Cho mượn" 

def show_list(list):
    if not list:
        print("danh sách cầu thủ trống")
    else:
        print(f"{"id":<10} | {"name":<20} | {"total_match":<15} | {"goal":<10} | {"assist":<10} | {"effect":<10} | {"rank":<20}")
        print("-"*110)
        for player in list:
            print(f"{player["id"]:<10} | {player["name"]:<20} | {player["total_match"]:<15} | {player["goal"]:<10} | {player["assist"]:<10} | {player["effect"]:<10} | {player["rank"]:<20}")
        print("-"*110)

def add_player(list):
    while True:
            new_id = input("nhập mã cầu thủ mới: ").strip().upper()
            found = False
            if new_id == "":
                print("mã cầu thủ không được để trống")
                continue
            else:
                for player in list:
                    if player["id"] == new_id:
                        found = True
                        break
            if found == True:
                print("cầu thủ đã tồn tại")
            else:
                break

    while True:
        new_name = input("nhập tên cầu thủ mới: ").strip().title()
        if new_name == "":
            print("tên cầu thủ không được trống")
        else:
            break 
    
    while True:
        try:
            total_match = int(input("nhập tổng trận đã tham gia: "))
            if total_match < 0 or total_match > 50:
                print("số trận phải nằm trong khoảng từ 0 đến 50")
            else:
                break
        except ValueError:
            print("giá trị không hợp lệ")
        
        

    while True:
        try:
            goal = int(input("nhập số bàn thắng: "))
            assist = int(input("nhập số đường bóng kiến tạo: "))
            if goal < 0 or assist < 0:
                print("Số bàn thắng và Số kiến tạo phải lớn hơn hoặc bằng 0")
            else: 
                break
        except ValueError:
            print("giá trị không hợp lệ")

    effect_point = (total_match * 1) + (goal * 3) + (assist * 2)

    rank = phan_loai_phong_do(effect_point)
    
    new_player = {
        "id": new_id,
        "name": new_name,
        "total_match": total_match,
        "goal": goal,
        "assist": assist,
        "effect": effect_point,
        "rank": rank
    }

    football_list.append(new_player)
    print("thêm cầu thủ thành công")

def update_player(list):
    while True:
            search_id = input("nhập mã cầu thủ cần tìm: ").strip().upper()
            if search_id == "":
                print("mã cầu thủ không được để trống")
                continue
            else:
                if validate_id(search_id, list) == None:
                    print("cầu thủ chưa tồn tại trong danh sách")
                else:
                    player = validate_id(search_id, list)
                    break

    while True:
        new_name = input("nhập tên cầu thủ mới: ").strip().title()
        if new_name == "":
            print("tên cầu thủ không được trống")
        else:
            break 
    
    while True:
        try:
            total_match = int(input("nhập tổng trận đã tham gia: "))
            if total_match < 0 or total_match > 50:
                print("số trận phải nằm trong khoảng từ 0 đến 50")
            else:
                break
        except ValueError:
            print("giá trị không hợp lệ")
        
        

    while True:
        try:
            goal = int(input("nhập số bàn thắng: "))
            assist = int(input("nhập số đường bóng kiến tạo: "))
            if goal < 0 or assist < 0:
                print("Số bàn thắng và Số kiến tạo phải lớn hơn hoặc bằng 0")
            else: 
                break
        except ValueError:
            print("giá trị không hợp lệ")

    effect_point = (total_match * 1) + (goal * 3) + (assist * 2)

    rank = phan_loai_phong_do(effect_point)
    
    player["name"] = new_name
    player["total_match"] = total_match
    player["goal"] = goal
    player["assist"] = assist
    player["effect"] = effect_point
    player["rank"] = rank
    print("cập nhật cầu thủ thành công")

def delete_player(list):
    delete_id = input("nhập id cầu thủ muốn xóa: ").strip().upper()

    found = validate_id(delete_id, list)

    if found == None:
        print("không tìm thấy cầu thủ")
    else:
        confirm = input("bạn có chắc muốn xóa cầu thủ này khỏi danh sách không (Y/N): ").strip().upper()

        if confirm == "Y":
            list.remove(found)
            print("xóa thành công")
        elif confirm == "N":
            print("đã hủy thao tác")
            return
        else:
            print("mời chọn lại")
            return

while True:
    print("""
    ====== MENU QUẢN LÝ TUYỂN THỦ ======
    1. Hiển thị danh sách cầu thủ
    2. Tiếp nhận cầu thủ mới
    3. Cập nhật thông tin và chỉ số
    4. Xóa cầu thủ (Thanh lý hợp đồng)
    5. Tìm kiếm cầu thủ
    6. Thống kê phân loại phong độ
    7. Đánh giá phong độ tự động
    8. Thoát chương trình  
    ==================================== 
""")
    
    try:
        choice = int(input("nhập lựa chọn từ 1 đến 8: "))
    except ValueError:
        print("lựa chọn không hợp lệ")

    match choice:
        case 8:
            print("đã thoát chương trình")
            break
        case 1:
            show_list(football_list)
        case 2:
            add_player(football_list)
        case 3: 
            update_player(football_list)
        case 4:
            delete_player(football_list)