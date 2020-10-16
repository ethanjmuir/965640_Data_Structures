from device import Device

class Laptop(Device):
    '''
    This is the laptop itself.

    Attributes 
    ----------
    material : str
        What the laptop is made from.
    
    Methods
    -------
    mouse_needed(trackpad_width : float) -> bool
        Tells user whether they should get a mouse or not, depending on how big their trackpad is.
    
    '''

    def __init__(self, brand, screen_size, foldable, charge, battery_size, operating_system, warranty_duration_years, year_purchased, material, trackpad_width):
        super().__init__(brand, screen_size, foldable, charge, battery_size, operating_system, warranty_duration_years, year_purchased)
        self.material = material
        self.trackpad_width = trackpad_width
    
    def __str__(self):
        return str("\nBrand : " + self.brand + "\nScreen Size : " + str(self.screen_size) + " Inches" + "\nFoldable : " + str(self.foldable) + "\nCharge : " + str(self.charge) + " %" + "\nBattery Size : " + str(self.battery_size) + " mAh" + "\nOperating System : " + self.operating_system + "\nYear Purchased : " + str(self.year_purchased) + "\nMaterial : " + self.material + "\nTrackpad Width : " + str(self.trackpad_width) + " Inches\n")

    def mouse_needed(self, trackpad_width):
        if trackpad_width < 4.5:
            self.mouse_needed = True 
        else:
            self.mouse_needed = False 
        return "Mouse Needed : " + str(self.mouse_needed) + "\n"
