import math
def main():
    can_names = [
        "#1 Picnic", "#1 Tall", "#2", "#2.5", "#3 Cylinder", 
        "#5","#6Z","#8Z short","#10","#211","#300","#303"
    ]
    radius_cm = [
        6.83,7.78,8.73,10.32,10.79,13.02,5.40,6.83,15.72,6.83,7.62,8.10
    ]
    height_cm = [
        10.16,11.91,11.59,11.91,17.78,14.29,8.89,7.62,17.78,12.38,11.27,11.11
    ]
    cost_per_can = [
        0.28,0.43,0.45,0.61,0.86,0.83,0.22,0.26,1.53,0.34,0.38,0.42
    ]
    best_store = None
    best_cost = None
    max_store_eff = -1
    max_cost_eff = -1
    for i in range(len(can_names)):
        name = can_names[i]
        radius = radius_cm[i]
        height = height_cm[i]
        cost = cost_per_can[i]
        store_eff = compute_storage_efficiency(radius,height)
        cost_eff = compute_cost_efficiency(radius,height,cost)
        print(f"{name} {store_eff:.2f} {cost_eff:.0f}")
        if store_eff > max_store_eff:
            best_store = name
            max_store_eff = store_eff
        if cost_eff > max_cost_eff:
            best_cost = name
            max_cost_eff = cost_eff
    print()
    print("Best can size storage efficiency:", best_store )
    print("Best can size in cost effciency: ", best_cost)
    
main()
def compute_storage_efficiency(radius,height):
    volume = compute_volume(radius,height)
    surf_area = surface_area(radius,height)
    efficiency = volume / surf_area
    return efficiency

def compute_cost_efficiency (radius,height,cost):
    volume = compute_volume(radius,height)
    efficiency = volume / cost
    return efficiency

def compute_volume(radius,height):
    volume = math.pi * radius**2 * height
    return volume

def surface_area(radius,height):
    surface_area = 2 * math.pi * radius(radius + height)
    return surface_area
