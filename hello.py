import math
def rumus_abc (a, b, c):
    x_1 =(-b + math.sqrt(math.pow(b,2) -4*a*c))/(2*a)

    x_2 =(-b - math.sqrt(math.pow(b,2) -4*a*c))/(2*a)

    print (x_1)
    print (x_2)

    print("akarnya adalah " + str(x_1)+ " dan " + str(x_2) + ".")
    
rumus_abc(1,2,1)
rumus_abc(2,-5,-3)

nama_depan = "Darma"
nama_tengah = "Yanto"
nama_belakang = "Putra"
nama_lengkap = nama_depan + " " + nama_tengah+" "+ nama_belakang
print (nama_lengkap)

a1 = 10
a2 = 3
print (a1*a2)
print (oct(a1*a2))