from phone import Phone 
from laptop import Laptop

# NOTE : Submit: Source code, .txt file, UML diagrams. (as mentioned by Mr. Seidel)

iphone_xr = Phone("Apple", 6.1, False, 48, 2942, "iOS", 1, 2018, "glass")
macbook_pro = Laptop("Apple", 13, True, 82, 4475, "MacOS", 82, 2017, "aluminium", 6.1)
galaxy_z = Phone("Samsung", 6.7, True, 56, 2900, "Android", 5262, 2020, "glass")
pixel_5 = Phone("Google", 5.8, False, 18, 3000, "Android", 2, 2020, "polycarbonate")
xps_15 = Laptop("Dell", 15.3, True, 20, 5000, "Windows", -800, 2019, "aluminium", 5.5)
blade_stealth = Laptop("Razer", 12.3, True, 58, 3475, "Linux", -4223, 2017, "aluminium", 4.3)

my_devices = [iphone_xr, macbook_pro, galaxy_z, pixel_5, xps_15, blade_stealth]

file_output = open('output.txt', 'w')

for i in range(len(my_devices)):
    file_output.write(str(my_devices[i]))
    file_output.write(str(my_devices[i].full_charge(my_devices[i].charge)))
    file_output.write(str(my_devices[i].charge_needed(my_devices[i].charge)))
    file_output.write(my_devices[i].assistant_hotword(my_devices[i].operating_system))
    file_output.write(my_devices[i].warranty_expiry(my_devices[i].year_purchased, my_devices[i].warranty_duration_years))

    if isinstance(my_devices[i], Phone): 
        file_output.write(my_devices[i].case_needed(my_devices[i].back_material))
    elif isinstance(my_devices[i], Laptop):
        file_output.write(my_devices[i].mouse_needed(my_devices[i].trackpad_width))

file_output.close()

file_input = open('output.txt', 'r')
device_analysis = file_input.readlines()
print(''.join(device_analysis))
file_input.close()