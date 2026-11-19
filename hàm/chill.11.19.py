def xep_loai(diem):
    if diem < 0 or diem > 10:
        return None

    if diem >= 8:
        return "Giỏi"
    elif diem >= 6:
        return "Khá"
    elif diem >= 5:
        return "Trung bình"
    else:
        return "Yếu"
def thong_ke_xep_loai(students):
    result = {
        "Giỏi": 0,
        "Khá": 0,
        "Trung bình": 0,
        "Yếu": 0
    }

    for ten, diem in students.items():
        loai = xep_loai(diem)

        if loai is not None:
            result[loai] += 1

    return result
students = {
    "An": 9,
    "Bình": 4,
    "Chi": 7,
    "Dũng": 5,
    "Hà": 8
}

ket_qua = thong_ke_xep_loai(students)

print(ket_qua)