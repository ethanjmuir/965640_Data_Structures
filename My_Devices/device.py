class Device:
    '''
    This is the device itself.

    Attributes 
    ----------
    brand : str
        This is the phone brand.
    screen_size : float
        This is the resolution of the main display.
    foldable : bool
        Is true if the phone is foldable.
    charge : int
        The phone's charge
    battery_size : int
        Size of the battery in mAh.
    operating_system : str
        Operating system running on the phone.
    warranty_duration_years : int
        Duration of user warranty.
    year_purchased : int
        The year the user bought the phone.
    
    Methods
    -------
    warranty_expiry(year_purchased : int , warranty_duration_years) -> int
        Tells user when their warranty expires.
    full_charge(charge : int) -> int
        Informs user of how much charge their phones need.
    charge_needed(charge : int) -> bool
        Is true if charge is below 20 percent.
    assistant_hotword(operating_system : str) -> str
        Returns summoning phrase for Google, Siri or Cortana.
    
    '''

    def __init__(self, brand = "not branded", screen_size = 5.8, foldable = False, charge = "100", battery_size = "2000", operating_system = "Android", warranty_duration_years = 3, year_purchased = 2020):
        self.brand = brand
        self.screen_size = screen_size
        self.foldable = foldable
        self.charge = charge
        self.battery_size = battery_size
        self.operating_system = operating_system
        self.year_purchased = year_purchased
        self.warranty_duration_years = warranty_duration_years

    def __str__(self):
        return self
   

    def warranty_expiry(self, year_purchased : int, warranty_duration_years : int) -> int:
        '''
        Tells user how old their phone is in relation to when they purchased it.
        '''
        if self.year_purchased + self.warranty_duration_years < 2020:
            return "Yeah um... your warranty is already expired.\n"
        elif self.year_purchased + self.warranty_duration_years == 2020:
            return "Your warranty expires this year.\n"
        else:
            return "Your warranty expires in " + str(self.year_purchased + self.warranty_duration_years) + ". \n"


    def full_charge(self, charge : int) -> int:
        '''
        Informs user of how much charge their phones need.
        '''
        self.full_charge = 100 - int(self.charge)
        return "Percentage Until Full Charge : " + str(self.full_charge) + "\n"

    def charge_needed(self, charge : int) -> bool:
        '''
        Is true if charge is below 20 percent.
        '''
        if self.charge <= 20:
            self.charge_needed = True 

        else:
            self.charge_needed = False

        return "Charge Needed : " + str(self.charge_needed) + "\n"

    def assistant_hotword(self, operating_system : str) -> str:
        '''
        Returns summoning phrase for Google, Siri or Cortana.
        '''

        if self.operating_system == "iOS" or self.operating_system == "MacOS":
            self.assistant_hotword = "Hey Siri!"

        elif self.operating_system == "Android":
            self.assistant_hotword = "Hey Google!"

        elif self.operating_system == "Windows":
            self.assistant_hotword = "Hey Cortana!"

        elif self.operating_system == "Linux":
            self.assistant_hotword = "Hey Mycroft"

        else:
            self.assistant_hotword = "The fact that you don't use any of these mainstream systems is alarming."
        
        return "Assistant Hotword : " + self.assistant_hotword + "\n"