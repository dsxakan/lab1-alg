#Bu modul bizga itertools.permutations funksiyasidan foydalanish imkonini beradi, bu esa barcha mumkin bo'lgan marshrutlarni yaratadi.
import itertools

# Masofa matritsasi - shaharlar orasidagi masofalarni bildiradi
# Masalan, distance_matrix[i][j] i-shahardan j-shaharga bo'lgan masofani ko'rsatadi
distance_matrix = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

# Shaharlar soni
n = len(distance_matrix)

# Barcha shaharlar ro'yxati, masalan [0, 1, 2, 3]
#Shaharlar ro'yxatini yaratamiz, bu yerda range(n) 0 dan n gacha sonlar ketma-ketligini bildiradi.
cities = list(range(n))

# Eng qisqa masofani cheksiz katta qiymatga o'rnatamiz
min_path_length = float('inf')

# Eng qisqa marshrutni saqlash uchun bo'sh ro'yxat //Самый короткий маршрут
min_path = []

# Barcha mumkin bo'lgan marshrutlarni ko'rib chiqish
for permutation in itertools.permutations(cities):
    # Hozirgi marshrutning umumiy masofasini hisoblash //Начальное значение
    current_length = 0
    #Bu tsikl orqali marshrutdagi ketma-ket shaharlar orasidagi masofalarni qo'shamiz. Misol uchun, agar permutation (0, 2, 1, 3) bo'lsa:
    for i in range(n - 1):
        current_length += distance_matrix[permutation[i]][permutation[i + 1]]
    # Oxirgi shahardan boshlang'ich shaharga qaytish masofasi
    current_length += distance_matrix[permutation[-1]][permutation[0]]
    
    # Agar hozirgi marshrut eng qisqa bo'lsa, uni saqlaymiz
    if current_length < min_path_length:
        min_path_length = current_length
        min_path = permutation

# Natijalarni chiqarish
print(f"Самый короткий маршрут: {min_path}")
print(f"Кратчайшее расстояние маршрута: {min_path_length}")
