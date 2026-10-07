def sapa (nama,salam="hallo"):
    return f"{salam}, {nama}!"

print(sapa("anggun"))
print(sapa(salam="hai", nama="sayangggg"))

def total(*angka):
    return sum(angka)
print(total(1,2,3,4))