import math

def compute_volume(radius, height):
    volume = math.pi * radius**2 * height
    return volume

def compute_surface_area(radius, height):
    surface_area = 2 * math.pi * radius * (radius + height)
    return surface_area

def compute_storage_efficiency(radius, height):
    volume = compute_volume(radius, height)
    surface_area = compute_surface_area(radius, height)
    storage_efficiency = volume / surface_area
    return storage_efficiency

def main():
    can_sizes = [
        ["#1 Picnic", 6.83, 10.16, 0.28],
        ["#1 Tall", 7.78, 11.91, 0.43],
        ["#2", 8.73, 11.59, 0.45],
        ["#2.5", 10.32, 11.91, 0.61],
        ["#3 Cylinder", 10.79, 17.78, 0.86],
        ["#5", 13.02, 14.29, 0.83],
        ["#6Z", 5.40, 8.89, 0.22],
        ["#8Z short", 6.83, 7.62, 0.26],
        ["#10", 15.72, 17.78, 1.53],
        ["#211", 6.83, 12.38, 0.34],
        ["#300", 7.62, 11.27, 0.38],
        ["#303", 8.10, 11.11, 0.42]
    ]

    for can in can_sizes:
        name, radius, height, cost = can
        storage_efficiency = compute_storage_efficiency(radius, height)
        print(f"{name} {storage_efficiency:.2f}")

    max_storage_efficiency = max(compute_storage_efficiency(radius, height) for _, radius, height, _ in can_sizes)
    max_storage_can = next(name for name, radius, height, _ in can_sizes if compute_storage_efficiency(radius, height) == max_storage_efficiency)
    print(f"\nCan size with the highest storage efficiency: {max_storage_can}")

    def compute_cost_efficiency(radius, height, cost):
        volume = compute_volume(radius, height)
        cost_efficiency = volume / cost
        return cost_efficiency

    print("\nCost efficiency:")
    for can in can_sizes:
        name, radius, height, cost = can
        cost_efficiency = compute_cost_efficiency(radius, height, cost)
        print(f"{name} {cost_efficiency:.2f}")

    max_cost_efficiency = max(compute_cost_efficiency(radius, height, cost) for _, radius, height, cost in can_sizes)
    max_cost_can = next(name for name, radius, height, cost in can_sizes if compute_cost_efficiency(radius, height, cost) == max_cost_efficiency)
    print(f"\nCan size with the highest cost efficiency: {max_cost_can}")

if __name__ == "__main__":
    main()