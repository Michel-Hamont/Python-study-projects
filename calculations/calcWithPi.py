## calc with pi.py

# Constante pi (π)
PI = 3.14159265359

class Cirkel():
        
    # constructor
    def __init__ (self, straal):
        self.straal = straal

    # Computed properties
    @property
    def diameter(self):
        return 2 * self.straal

    @property
    def omtrek(self):
        return 2 * PI * self.straal

    @property
    def oppervlakte(self):
        return PI * (self.straal ** 2)

    # Alleen hier voor het testen van __str__()
    def nepper(self):
        pass

    # Printer
    def __str__(self):
        result=''
        all = dir(self)
        for attr in all:
            # Geen 'magic', geen methods
            if attr[0:2] != '__'  and \
               type(getattr(self, attr)).__name__  != 'method':
                result += "{:<11}: {}\n".format(attr, str(getattr(self, attr)))
        return result

    # Toon in shell
    def __repr__(self):
        return str(self)
    
        
    # ----- comparison operators -------
    # c1 == c2
    def __eq__(self, other):
        return self.straal == other.straal

    # c1 != c2
    def __ne__(self, other):
        # return not (self == other)
        return self.straal != other.straal
    
    # c1 > c2
    def __gt__(self, other):
        return self.straal > other.straal
    
    # c1 >= c2
    def __ge__(self, other):
        # return (self > other) or (self == other)
        return self.straal >= other.straal
    
    # c1 < c2
    def __lt__(self, other):
        # return not (self >= other)
        return self.straal < other.straal
    
    # c1 <= c2
    def __le__(self, other):
        # return not (self > other)
        return self.straal <= other.straal
        


class Bol(Cirkel):
    # constructor (__init__) is hetzelfde als in Cirkel()

    # Computed properties
    @property
    def oppervlakte(self):
        return 4 * PI * (self.straal ** 2)

    @property
    def volume(self):
        return (4/3) * PI * (self.straal ** 3)

    


