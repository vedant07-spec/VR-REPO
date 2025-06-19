import math

class ElectronicsCalculator:
    
    @staticmethod
    def ohms_law():
        print("\nOhm's Law Calculator:")
        print("Choose the parameter you want to calculate:")
        print("1. Voltage (V)")
        print("2. Current (I)")
        print("3. Resistance (R)")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            current = float(input("Enter current (I in amperes): "))
            resistance = float(input("Enter resistance (R in ohms): "))
            voltage = current * resistance
            print(f"Voltage (V) = {voltage} V")
        elif choice == 2:
            voltage = float(input("Enter voltage (V in volts): "))
            resistance = float(input("Enter resistance (R in ohms): "))
            current = voltage / resistance
            print(f"Current (I) = {current} A")
        elif choice == 3:
            voltage = float(input("Enter voltage (V in volts): "))
            current = float(input("Enter current (I in amperes): "))
            resistance = voltage / current
            print(f"Resistance (R) = {resistance} ohms")
        else:
            print("Invalid choice")

    @staticmethod
    def power_calculations():
        print("\nPower Calculation:")
        print("Choose the parameter you want to calculate:")
        print("1. Power (P)")
        print("2. Voltage (V)")
        print("3. Current (I)")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            voltage = float(input("Enter voltage (V in volts): "))
            current = float(input("Enter current (I in amperes): "))
            power = voltage * current
            print(f"Power (P) = {power} watts")
        elif choice == 2:
            power = float(input("Enter power (P in watts): "))
            current = float(input("Enter current (I in amperes): "))
            voltage = power / current
            print(f"Voltage (V) = {voltage} V")
        elif choice == 3:
            power = float(input("Enter power (P in watts): "))
            voltage = float(input("Enter voltage (V in volts): "))
            current = power / voltage
            print(f"Current (I) = {current} A")
        else:
            print("Invalid choice")

    @staticmethod
    def resistor_color_code():
        print("\nResistor Color Code Decoder (4-band):")
        color_codes = {
            'black': 0, 'brown': 1, 'red': 2, 'orange': 3, 'yellow': 4,
            'green': 5, 'blue': 6, 'violet': 7, 'gray': 8, 'white': 9
        }
        band1 = input("Enter first color band: ").lower()
        band2 = input("Enter second color band: ").lower()
        multiplier_band = input("Enter multiplier band: ").lower()
        tolerance_band = input("Enter tolerance band: ").lower()

        if band1 in color_codes and band2 in color_codes and multiplier_band in color_codes:
            resistance = (color_codes[band1] * 10 + color_codes[band2]) * (10 ** color_codes[multiplier_band])
            tolerance = {'brown': 1, 'red': 2, 'green': 0.5, 'blue': 0.25, 'violet': 0.1, 'gold': 5, 'silver': 10}.get(tolerance_band, 20)
            print(f"Resistance: {resistance} ohms ±{tolerance}%")
        else:
            print("Invalid color code")

    @staticmethod
    def reactance_calculations():
        print("\nReactance Calculator:")
        print("1. Capacitive Reactance (Xc)")
        print("2. Inductive Reactance (Xl)")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            frequency = float(input("Enter frequency (in Hz): "))
            capacitance = float(input("Enter capacitance (in Farads): "))
            xc = 1 / (2 * math.pi * frequency * capacitance)
            print(f"Capacitive Reactance (Xc) = {xc} ohms")
        elif choice == 2:
            frequency = float(input("Enter frequency (in Hz): "))
            inductance = float(input("Enter inductance (in Henries): "))
            xl = 2 * math.pi * frequency * inductance
            print(f"Inductive Reactance (Xl) = {xl} ohms")
        else:
            print("Invalid choice")

    @staticmethod
    def battery_life_estimation():
        print("\nBattery Life Estimator:")
        capacity = float(input("Enter battery capacity (in mAh): "))
        load_current = float(input("Enter load current (in mA): "))
        battery_life = capacity / load_current
        print(f"Estimated Battery Life = {battery_life} hours")

# Main Program
def main():
    calculator = ElectronicsCalculator()
    while True:
        print("\n--- Electronics Ultimate Calculator ---")
        print("1. Ohm's Law")
        print("2. Power Calculations")
        print("3. Resistor Color Code")
        print("4. Reactance Calculations")
        print("5. Battery Life Estimation")
        print("6. Exit")
        choice = int(input("Choose an option: "))

        if choice == 1:
            calculator.ohms_law()
        elif choice == 2:
            calculator.power_calculations()
        elif choice == 3:
            calculator.resistor_color_code()
        elif choice == 4:
            calculator.reactance_calculations()
        elif choice == 5:
            calculator.battery_life_estimation()
        elif choice == 6:
            print("Exiting Calculator.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()