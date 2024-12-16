class Truck:
    def __init__(self, truck_id):
        self.truck_id = truck_id
        self.packages = set()  # Using a set to hold the packages, preventing duplicates

    def add_package(self, package):
        self.packages.add(package)

    def __str__(self):
        return f"Truck {self.truck_id} with {len(self.packages)} packages"
