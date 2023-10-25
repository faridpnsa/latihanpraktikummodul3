# Kegiatan 1
data = [
    {"minggu": 3, "hari": 3, "jam": 7, "menit": 21},
    {"minggu": 5, "hari": 5, "jam": 8, "menit": 11},
    {"minggu": 7, "hari": 1, "jam": 5, "menit": 33}
]
def konversi(minggu=0):
    def hari(hari=0):
        def jam(jam=0):
            def menit(menit=0):
                return ((minggu*7 + hari)*24 + jam)*60 + menit
            return menit
        return jam
    return hari
output_data = []
for item in data:
    minggu = item["minggu"]
    hari = item["hari"]
    jam = item["jam"]
    menit = item["menit"]
    konvert = konversi(minggu)(hari)(jam)(menit)
    output_data.append(konvert)

# Kegiatan 2
filtered_data = [[str(value) for value in item.values()] for item in data]

# Kegiatan 3
random_list = [105, 3.1, "Hello", 737, "Python", 2.7, "World", 412, 5.5, "AI"]
data_float = list(filter(lambda x: type(x) == float, random_list))
data_int = list(filter(lambda x: type(x) == int, random_list))
data_string = list(filter(lambda x: type(x) == str, random_list))
mapped_int = [{'ratusan': i//100, 'puluhan': (i % 100)//10, 'satuan': (i % 100) % 10} for i in data_int]

# Output
print("Output Kegiatan 1:", output_data)
print("Output Kegiatan 2:", filtered_data)
print("Output Kegiatan 3:")
print("Data Float:", data_float)
print("Data Int:")
for item in mapped_int:
    print(item)
print("Data String:", data_string)
