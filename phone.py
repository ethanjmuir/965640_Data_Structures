from device import Device

class Phone(Device):
    '''
    This is the phone itself.

    Attributes 
    ----------
    back_material : str
        The material that the back of the phone is made of. 
    
    Methods
    -------
    case_needed(back_material : str) -> bool
        Returns whether the user must get a case for their phone depending on the back material.
    
    '''

    def __init__(self, brand, screen_size, foldable, charge, battery_size, operating_system, warranty_duration_years, year_purchased, back_material):
        super().__init__(brand, screen_size, foldable , charge, battery_size, operating_system, warranty_duration_years, year_purchased)
        self.back_material = back_material
    
    def __str__(self):
        return str("\nBrand : " + self.brand + "\nScreen Size : " + str(self.screen_size) + " Inches" + "\nFoldable : " + str(self.foldable) + "\nCharge : " + str(self.charge) + " %" + "\nBattery Size : " + str(self.battery_size) + " mAh" + "\nOperating System : " + self.operating_system + "\nYear Purchased : " + str(self.year_purchased) + "\nBack Material : " + self.back_material + "\n")

    def case_needed(self, back_material):
        if back_material == "glass" or back_material == "ceramic":
            self.case_needed = True
        else:
            self.case_needed = False
        return "Case Needed : " + str(self.case_needed) + "\n"

