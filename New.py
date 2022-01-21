class India:
    def capital(self):
        print("New Delhi is the captial of India")

    def language(self):
        print("Hindi and English")

class USA:
    def capital(self):
        print("Washington DC is the captial of India")

    def language(self):
        print("English")

ind = India()
us = USA()

for country in (ind,us):
    country.capital()
    country.language()
    
