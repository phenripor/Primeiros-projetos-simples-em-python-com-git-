
bat_type = int(input("Selecione o tipo de bateria caseira: \n - bateria de limão (1) \n - bateria de batata (2) \n - bateria de água salgada (3)\n - bateria de Alumínio-ar (4)\n - bateria de carvão (5) \n - bateria de sal Fundido (6) \n - bateria de vinagre (7)\n - bateria de lata de aluminio e clareador (8)\n - bateria de terra (9)\n "))

match bat_type:
    case 1:
        print("Quantos limões estão sendo usados?")
        num_lemons = int(input())
        voltage_per_lemon = 0.9
        total_voltage = num_lemons * voltage_per_lemon
        print(f"A voltagem total da bateria de limão é: {total_voltage:.2f} volts")
    case 2:
        print("Quantas batatas estão sendo usadas?")
        num_potatoes = int(input())
        voltage_per_potato = 0.5
        total_voltage = num_potatoes * voltage_per_potato
        print(f"A voltagem total da bateria de batata é: {total_voltage:.2f} volts")
    case 3:
        print("Quantos copos de água salgada estão sendo usados?")
        num_saltwater = int(input())
        voltage_per_saltwater = 0.7
        total_voltage = num_saltwater * voltage_per_saltwater
        print(f"A voltagem total da bateria de água salgada é: {total_voltage:.2f} volts")
    case 4:
        print("Quantas baterias de Alumínio-ar estão sendo usadas?")
        num_aluminum_air = int(input())
        voltage_per_aluminum_air = 1.2
        total_voltage = num_aluminum_air * voltage_per_aluminum_air
        print(f"A voltagem total da bateria de Alumínio-ar é: {total_voltage:.2f} volts")
    case 5:
        print("Quantas baterias de carvão estão sendo usadas?")
        num_charcoal = int(input())
        voltage_per_charcoal = 0.8
        total_voltage = num_charcoal * voltage_per_charcoal
        print(f"A voltagem total da bateria de carvão é: {total_voltage:.2f} volts")
    case 6:
        print("Quantas baterias de sal fundido estão sendo usadas?")
        num_salt_fusion = int(input())
        voltage_per_salt_fusion = 1.0
        total_voltage = num_salt_fusion * voltage_per_salt_fusion
        print(f"A voltagem total da bateria de sal fundido é: {total_voltage:.2f} volts")
    case 7:
        print("Quantas baterias de vinagre estão sendo usadas?")
        num_vinegar = int(input())
        voltage_per_vinegar = 0.6
        total_voltage = num_vinegar * voltage_per_vinegar
        print(f"A voltagem total da bateria de vinagre é: {total_voltage:.2f} volts")
    case 8:
        print("Quantas baterias de lata de alumínio e clareador estão sendo usadas?")
        num_aluminum_bleach = int(input())
        voltage_per_aluminum_bleach = 0.9
        total_voltage = num_aluminum_bleach * voltage_per_aluminum_bleach
        print(f"A voltagem total da bateria de lata de alumínio e clareador é: {total_voltage:.2f} volts")
    case 9:
        print("Quantas baterias de terra estão sendo usadas?")
        num_earth = int(input())
        voltage_per_earth = 0.4
        total_voltage = num_earth * voltage_per_earth
        print(f"A voltagem total da bateria de terra é: {total_voltage:.2f} volts")
    case _:
        print("Inválido, tente novamente.")