class Planet: #Описание абстрактной планеты
    pass

solar_system = []
for i in range(8):
    planet = Planet()
    solar_system.append(planet)

print(solar_system)

