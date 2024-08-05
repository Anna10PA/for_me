# 0. lower() - შრიფტებს აპატარავებს 
name = "ANA"
print(name.lower()) # ana

# 1. upper() - ადიდებს 
name = "Ana"
print(name.upper()) # ANA

# 2. replace() - ადგილს უცვლის. 0 ადგილში რაც წერია იმის ადგილას ჩაიწერება 1-ში რაც წერია (a მაგივრად b)
a = "ana"
print(a.replace("a", "b")) # bnb

# 3. spilt() - სტრიქონს ქვესტრიქონებად 
a = "Annna "
print(a.split("n")) # n -ს მაგივრად '', დაიწერება

# 4.                                                                     f ფუნქცია
# f == format()
# f( format() ) - ის გამოყენებით შესაძლებელია, რომ int და float ერთმანეთს დაუკავშირდნენ გადაყვანის გარეშე. 
# ცვლად(ებ)თან დაიწერება ხვეული ფრჩხილები ( ანუ {}).

# N 0
name = "Ana"
lastname = "Puturidze"
age = 15
print(f"{name}  {lastname} is {age} years old")

# N
num = 12
f = 12.56
name = "Ana"
B = True

print (f"{num} {f} {name} {B}")
# ან
a = f"{num} {f} {name} {B}"
print(a)

# f ფუნქცია შეიძლება მოდიფიკატორის მნიშვნელობის შესაცვლელადაც გამოიყენება. ორი წერტილის (:) დამატებით და შემდეგ შეიძლება დაემატოს მაგ: .2f 
# .2f გამოიყენება რიცხვების ფორმის შეცვლაში, როგორც სტრიქონები ორი ათობითი ადგილით. ანუ 3 მაგივრად 3.00 დაიწერება 
# (ერთი f, ერთი ათობითი ადგილია)
print(f"{3:.2f}")

# 
price = 15
product = "chocolate"

shop = f"In shope {product} price is {price:.2f} GEL"
print(shop)
# ან 
print(f"In shope {product} price is {price:.2f} GEL")

# არითმეტიკული მოქმედებებიც შეიძლება {} - შიგნით
print(f"{12*3} is \"3\" + \"6\"")
