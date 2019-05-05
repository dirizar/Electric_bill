"""Find the wattage on the appliance label.
Most high-power appliances have an energy label on the back or base of the appliance.
Look here to find the wattage, listed as "W." This is usually the maximum power the device operates at,
which may be much higher than the actual average wattage.
 The steps below will find a rough estimate of kWh from this number,
but your actual kWh usage is usually lower."""

class KiloWattHour:

    def __init__(self,watt,hour, dollar):
        self.watt = watt
        self.dollar = dollar
        self.hour = hour

    def watt_hour(self,watt, hour, day=1):
        """Multiply wattage by hours used each day."""
        #this step converts your answer from watt hours into kilowatt hours.
        step1 = watt * hour
        step2 = step1 / day
        return round(step2)


    def kilo_watt_hour(self,watt_hour, day=1):
        step1 = watt_hour / day
        step2 = 1000 / 1
        return step1 / step2


    def kwh_per_month(self,kwh, month=1, day=1):
        step1 = kwh / day
        step2 = 30 / month              #30 is equeal to days in a month
        return round(step1 * step2)

    def kwh_per_year(self,kwh, day=1,year=1):
        step1 = kwh / day
        step2 = 365 / year               #366 is equal to days in a year
        return round(step1 * step2)


    def cost_of_electricity_month(self, dollar, kwh_month, month=1):
        step1 = dollar
        step2 = kwh_month / month
        return round(step2 * step1)


    def cost_of_electricity_year(self, dollars, kwh_year, year=1):
        step1 = dollars
        step2 = kwh_year / year
        return round(step2 * step1)


    def run(self):

        print("\n\nRESULTS:")
        watt_hour = self.watt_hour(self.watt, self.hour)
        kilo_watt_hour = self.kilo_watt_hour(watt_hour)
        print( kilo_watt_hour, " Kilo Watt hour per day")

        kwh_per_month = self.kwh_per_month(kilo_watt_hour)
        print(kwh_per_month, " is your Kilo Watt Hour per month")

        kwh_per_year = self.kwh_per_year(kilo_watt_hour)
        print(kwh_per_year, " is your Kilo Watt Hour per year")

        cost_per_month = self.cost_of_electricity_year(self.dollar, kwh_per_month)
        print(cost_per_month, "$ is your total of money you need to pay your electrty bill in one month")


        cost_in_year = self.cost_of_electricity_year(self.dollar, kwh_per_year)
        print(cost_in_year, "$ is your total of money you need to pay your electrty bill in one year")


class Kilo_Watt_Hour:

    def __init__(self,  amp, hour, dollar):
        self.amp = amp
        self.hour = hour
        self.dollar = dollar

    def watt(self,amp,volts=120):       #getting wattage by multipling
        step1 = amp * volts
        return round(step1)

    def watt_hour(self, watts, hour, day=1):
        step1 = watts * hour
        step2 = step1 // day
        return round(step2 / day)

    def kilo_watt_per_day(self, watt_hour, day=1):
        """Divide by 1000 to find Kilo Watt hour"""
        step1 = watt_hour / day
        step2 = 1000
        return step1 / step2

    def kilowatt_hour(self, kilowatt, day=1):
        """Multiply to find the kilowatt hours for a larger time period"""
        step1 = kilowatt / day
        return step1 * 31       #31 is days

    def cost_of_electricity_month(self, dollars, kwh_month, month=1):
        step1 = dollars
        step2 = kwh_month / month
        return round(step2 * step1)

    def run(self):
        print("RESULT:")
        watts = self.watt(self.amp)
        watt_hour_day = self.watt_hour(watts, self.hour)
        kilo_watt_per_day = self.kilo_watt_per_day(watt_hour_day, self.hour)
        print("\n", kilo_watt_per_day, " is your kilo Watt per day ")
        kilo_watt_hour = self.kilowatt_hour(kilo_watt_per_day)
        print(kilo_watt_hour, " is your Kilo Watt Hours in one month")
        cost_kilo_watt_hour = self.cost_of_electricity_month(self.dollar, kilo_watt_hour)
        print(cost_kilo_watt_hour, "$ is your total of money you need to pay your electrty bill in one month")



########################################################################################################################
    print("""
  ______ _           _        _      _ _           _     _ _ _             _            _       _             
 |  ____| |         | |      (_)    (_) |         | |   (_) | |           | |          | |     | |            
 | |__  | | ___  ___| |_ _ __ _  ___ _| |_ _   _  | |__  _| | |   ___ __ _| | ___ _   _| | __ _| |_ ___  _ __ 
 |  __| | |/ _ \/ __| __| '__| |/ __| | __| | | | | '_ \| | | |  / __/ _` | |/ __| | | | |/ _` | __/ _ \| '__|
 | |____| |  __/ (__| |_| |  | | (__| | |_| |_| | | |_) | | | | | (_| (_| | | (__| |_| | | (_| | || (_) | |   
 |______|_|\___|\___|\__|_|  |_|\___|_|\__|\__, | |_.__/|_|_|_|  \___\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|   
                                            __/ |                                                             
                                           |___/                                                        
 ------------------------------------------------------------------------------------------------------------------------  

                                                                                                        \n """)
ask = input("""If you don't know the wattage of your device 
type 'v' to find Kilo Watt Hour another way\n""")


if ask == "v":
    while True:
        try:
            amp = float(input("type your device amperage \n"))
        except ValueError:
            print("type a float like 1.0")
        else:
            break
    while True:
        try:
            time_in_use = float(input("type the amount of time the device being in used \n"))
        except ValueError:
            print("type a float like 1.0")
        else:
            break
    while True:
        try:
            cost = float(input("cost of Kilo Watt hour \n"))
        except ValueError:
            print("type a float like 1.0")
        else:
            break

    kwh = Kilo_Watt_Hour(amp, time_in_use, cost)
    kwh.run()

else:
    while True:
        try:
            watt = int(input("Tell me your wattage:\n"))
        except ValueError:
            print("pls use int ")
        else:
            break
    while True:
        try:
            time = float(input("""Tell me how much your device works in hours everyday. 
Please use float for specific time example '0.30' hour.minutes \n """))
        except ValueError:
            print("pls use float")
        else:
            break

    while True:
        try:
            kilo_watt_hour_cost = float(input("Tell me the cost of 1 kilo watt hour in your home town:\n"))
        except (FloatingPointError, ValueError):
            print("pls use float")
        else:
            break

    kwh = KiloWattHour(watt, time, kilo_watt_hour_cost)
    kwh.run()