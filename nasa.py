class Base:
    def __init__(self, age, cost, year_built, weight):
        self.age = age
        self.cost = cost
        self.year_built = year_built
        self.weight = weight

    def get_info(self):
        return f"Age: {self.age}, Cost: {self.cost}, Year Built: {self.year_built}, Weight: {self.weight} kg"


class SpaceShuttle(Base):
    FUEL_COST = 3.5  # Cost per kg of fuel
    BASE_SALARY = 50000  # Average personnel salary per person

    def __init__(self, age, cost, year_built, weight, burn_rate):
        super().__init__(age, cost, year_built, weight)
        self.burn_rate = burn_rate

    def calculate_mission_cost(self, orbit_height, personnel_count):
        fuel_cost = self.FUEL_COST * self.burn_rate * (2500 / orbit_height)
        personnel_expenditures = personnel_count * self.BASE_SALARY
        return fuel_cost + personnel_expenditures

    def get_full_report(self, orbit_height, personnel_count):
        mission_cost = self.calculate_mission_cost(orbit_height, personnel_count)
        return f"""Space Shuttle Info: {self.get_info()} Burn Rate: {self.burn_rate} kg/mile

        Mission Cost:
        Fuel Cost: {mission_cost - (personnel_count * self.BASE_SALARY)}
        Personnel Expenditures: {personnel_count * self.BASE_SALARY}
        Total Mission Cost: {mission_cost}"""


# Example usage:
shuttle = SpaceShuttle(age=5, cost=100000000, year_built=2018, weight=50000, burn_rate=1000)
orbit_height = 300  # miles
personnel_count = 10

print(shuttle.get_full_report(orbit_height, personnel_count))

# Writing report to a file
with open("mission_report.txt", "w") as file:
    file.write(shuttle.get_full_report(orbit_height, personnel_count))
