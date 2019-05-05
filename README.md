# Electric_bill
this is a great program to calculate your electric bill

alculating your electric bill:



	This is a program that calculates and give you a estimate value of your total  electric bill in month & year. It's very simple the program, it will ask you some question and you have to answer it  correctly. There two ways to use the program: finding Kilowatt Hour by wattage, or by amperage. 

First question:
	The program will ask you how do you want to find KWH(kilowatt hour)like this:
		If you don't know the wattage of your device
type 'v' to find Kilowatt Hour anod:other methods

	If you don’t type nothing or something else that is not ‘v’. By default it will begin with the method of finding KWH by wattage 


Second step:
	The rest of the question answers will be number. You can use int or float number for specific: time, wattage, amp and money.




###################################################################################################################################
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

#########################################################################################################################################
