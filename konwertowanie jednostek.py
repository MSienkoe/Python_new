def konwerterKM_Na_M (km_h):

  m_s = float(km_h / 3.6)

  return m_s

def konwerterM_Na_KM (m_s):

  km_h = float(m_s * 3.6)

  return km_h

wybor = int(input("""Opcje konwertowania

1. KM/H na M/S

2. M/S na KM/h  

Wciśnij 1 lub 2 : """))

if wybor == 1 :

  predkosc = float(input("Podaj prędkość w kilometrach na godzinę: "))

  print("Wynik :", round(konwerterKM_Na_M(predkosc),3), "m/s")

elif wybor == 2 :

  predkosc = float(input("Podaj prędkość w metrach na sekundę: "))

  print("Wynik :", round(konwerterM_Na_KM(predkosc),3), "km/h")

