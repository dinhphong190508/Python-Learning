def tong_so_chan(ds):
    tong =0
    for i in ds:
        if i%2==0:
            tong+=i
    return tong
print(tong_so_chan([1, 2, 3, 4, 5, 6]))

def dem_xuat_hien(ds,x):
    dem=0
    for i in ds:
        if x==i:
            dem+=1
    return dem
print(dem_xuat_hien([1, 2, 3, 2, 4, 2, 5], 2))
   

def tim_vi_tri_chan(ds):
    ds_chan=[]                                  
    for index,value in enumerate(ds):
        if value %2 ==0:
            ds_chan.append(index)
    return ds_chan
print(tim_vi_tri_chan([5, 2, 7, 4, 9, 6]))
#có thể code nhanh hơn
'''
ds_chan=[
index
for index,value in enumerate(ds)
if value %2 ==0
]
'''

#filter() để lọc dữ liệu bên trong 
def binh_phuong_so_le(ds):
    ds_binhphuong_le=[
        x**2   # đây là biểu thức tạo giá trị
        for x in ds
        if x %2 !=0
    ]
    return ds_binhphuong_le


print(binh_phuong_so_le([1, 2, 3, 4, 5, 6, 7]))

#cách 2 của hàm bình phương lẻ
'''def binh_phuong_le(ds):
    ds_le= filter(lambda x:x%2 !=0 ,ds) #filter lọc phần tử thỏa mãn điều kiện ,#lambda tạo một hàm nhỏ
    #filter(hàm kiểm tra điều kiện , dữ liệu cần lọc)
    ds_binhphuong=map(lambda x:x**2,ds_le) #map biến đổi từng phần tử,nó không có nhiệm vụ lịc phần tử
    return ds_binhphuong
print(binh_phuong_so_le([1, 2, 3, 4, 5, 6, 7]))'''
#cachs 2 kết hợp cả map và filter
def binh_phuong_le(ds):
    return list(
        map(
            lambda x:x**2,
            filter(lambda x:x%2 !=0 ,ds)
        )
    )
print(binh_phuong_so_le([1, 2, 3, 4, 5, 6, 7]))

#áp dụng map và filter
def nhan_doi(ds):
    return list(
        map(
            lambda x: x*2,
            ds
        )
    )
print(nhan_doi([2,4,6,8]))

def nhan_doi_lon_hon5(ds):
    return list(
        map(
            lambda x: x*2,
            filter(lambda x :x>5 , ds)
        )
    )
print(nhan_doi_lon_hon5([2,4,6,8,10]))


#baitap:cho 2 danh sach ,tính tổng từng cặp phần tử ở vị trí tương ứng , trả về list
def tong_2_ds(ds1,ds2):
    #n1=len(ds1)
    #n2=len(ds2)
    #dùng min để tìm độ dài danh sách ngắn hơn
    n=min(len(ds1),len(ds2))
    a=0
    ds_tra_ve=[]
    for x in range(n): #chú ý chỉ lặp đến độ dài dánh sách ngắn hơn
        a=ds1[x] + ds2[x]
        ds_tra_ve.append(a)
    return ds_tra_ve
#    else:
  #      for x in range(n1):
  #          a=ds1[x] + ds2[x]
  #          ds_tra_ve.append(a)
  #      return ds_tra_ve

print(tong_2_ds([1,2,3,4],[10,20,30,40]))
#cách 2 dùng map+lambda
def sum_2_ds(ds1,ds2):
    return list(map(lambda x,y: x+y ,ds1,ds2))  #hàm nhận 2 tham số x ,y , nó sẽ tự cung cấp tương ứng x của ds1 ,y của ds2
print(sum_2_ds([1,2,3,4],[10,20,30,40]))

#cách 3 dùng zip() :ghép các phần tử tương ứng
ds1=[1,2,3]
ds2=[10,20]
ket_qua =zip(ds1,ds2) #ghép các phần tử cùng vị trí thành tuple,chỉ lấy số phần tử bằng độ dài list ngắn hơn
print(list(ket_qua))
#áp dụng với bài trên dùng for với zip
#cap[0] , cap[1]... là lấy phần tử đầu tiên, lấy phần tử thứ 2 ...của tuple
def tong_2_danhsach(ds1,ds2):
    return list(map(
         lambda x: x[0] + x[1],#lambda x: x[0] + x[1],lambda cap: cap[0] + cap[1]
        zip(ds1,ds2)
    ))
print(tong_2_danhsach([1,2,3,4],[10,20,30,44]))


#nâng cấp kỹ năng xử lý dữ liệu
#Cho danh sach ten va diem , ghep ten va diem tuong ung , xep loại tên theo điểm
def xep_loai(ten,diem):
    dic_ds=dict(zip(ten,diem))
    ket_qua={}
    for x ,y in dic_ds.items():
        if y>10 or y<0:
            raise ValueError("Điểm không hợp lệ") #nếu không hợp lệ, nó sẽ dừng chương trình tại đây       
        elif y>=8:
            ket_qua[x]="Giỏi"
        elif y>=6.5:
            ket_qua[x]="Khá"
        elif y<6.5:
            ket_qua[x]="Trung bình"
    return ket_qua
ten = ["An", "Bình", "Cường", "Dũng"]
diem = [8, 6, 9, 7]
print(xep_loai(ten,diem))
#nếu yêu cầu bài trên muốn trả về kiểu dữ liệu tuple chứ không phải dic
def xep_loai2(ten,diem):
    ketqua=[]
    for t ,d in zip(ten,diem):  # duyệt từng cặp ,lấy ten gán cho t,diem gán cho d
        if d>=8:
            loai="Giỏi"
        elif d>=6.5:
            loai="Khá"
        elif d<6.5:
            loai="Trung bình"
        ketqua.append((t,loai))  #thêm cặp phần tử (t,loai) , chú ý nó phải ở trong vòng for để lưu kết quả
    return ketqua
ten = ["An", "Bình", "Cường", "Dũng"]
diem = [8, 6, 9, 7]
print(xep_loai2(ten,diem))
#cách nâng cao dùng map() + lambda
def xep_loai3(ten,diem):
    return list(map(
        lambda x :(   # tạo hàm ngắn gọn , x ở đây là cặp (tên ,điểm) do lúc sau truyền zip
            x[0], #lấy phần tử trong tuple bằng chỉ số
            "Giỏi" if x[1]>=8
            else "Khá" if x[1]>=6.5
            else "Trung bình"
        ),
        zip(ten,diem)
    ))
ten = ["An", "Bình", "Cường", "Dũng"]
diem = [8, 6, 9, 7]
print(xep_loai3(ten,diem))
            
