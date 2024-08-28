class Elev:
    def __init__(self, namn, årskurs):
        self.namn = namn  # Attribut för elevens namn
        self.årskurs = årskurs  # Attribut för elevens årskurs

    def visa_info(self):
        return f"Elevens namn: {self.namn}, Årskurs: {self.årskurs}"

    def uppdatera_årskurs(self, ny_årskurs):
        self.årskurs = ny_årskurs  # Metod för att uppdatera årskurs
        return f"{self.namn}s årskurs har uppdaterats till {self.årskurs}"

# Skapa en lista för att hålla elever
elever = []

# Lägg till några elever i listan
elever.append(Elev("Anna", 5))
elever.append(Elev("Johan", 6))
elever.append(Elev("Sara", 4))

# Visa information om alla elever
for elev in elever:
    print(elev.visa_info())

# Uppdatera årskurs för en elev
print(elever[0].uppdatera_årskurs(6))
