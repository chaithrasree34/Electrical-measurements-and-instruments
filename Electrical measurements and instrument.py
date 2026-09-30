# Electrical-measurements-and-instruments
# Electrical Measurements and Instruments

print("Electrical Measurements and Instruments")
print("--------------------------------------")
print("1. Voltmeter - Calculate Voltage")
print("2. Ammeter - Calculate Current")
print("3. Ohmmeter - Calculate Resistance")
print("4. Wattmeter - Calculate Power")
print("5. Energy Meter - Calculate Energy")

choice = int(input("\nEnter your choice (1-5): "))

if choice == 1:
    # Voltmeter
    current = float(input("Enter current (A): "))
    resistance = float(input("Enter resistance (Ohm): "))

    voltage = current * resistance

    print("\nVoltmeter Reading =", voltage, "V")

elif choice == 2:
    # Ammeter
    voltage = float(input("Enter voltage (V): "))
    resistance = float(input("Enter resistance (Ohm): "))

    current = voltage / resistance

    print("\nAmmeter Reading =", current, "A")

elif choice == 3:
    # Ohmmeter
    voltage = float(input("Enter voltage (V): "))
    current = float(input("Enter current (A): "))

    resistance = voltage / current

    print("\nOhmmeter Reading =", resistance, "Ohm")

elif choice == 4:
    # Wattmeter
    voltage = float(input("Enter voltage (V): "))
    current = float(input("Enter current (A): "))
    power_factor = float(input("Enter power factor: "))

    power = voltage * current * power_factor

    print("\nWattmeter Reading =", power, "W")

elif choice == 5:
    # Energy Meter
    power = float(input("Enter power (W): "))
    time = float(input("Enter operating time (hours): "))

    energy = (power * time) / 1000

    print("\nEnergy Meter Reading =", energy, "kWh")

else:
    print("\nInvalid choice!")
