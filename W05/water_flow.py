def water_column_height(tower_height, tank_height):
    """Calculate and return the height of a column of water in a tank."""
    h = tower_height + (3 * tank_height) / 4
    return h

def pressure_gain_from_water_height(height):
    """Calculate and return the pressure caused by Earth's gravity pulling on the water."""
    ρ = 998.2  # density of water (kilogram / meter^3)
    g = 9.80665  # acceleration from Earth's gravity (meter / second^2)
    P = (ρ * g * height) / 1000
    return P

def pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity):
    """Calculate and return the water pressure lost due to friction in a pipe."""
    ρ = 998.2  # density of water (kilogram / meter^3)
    P = (-friction_factor * pipe_length * ρ * fluid_velocity**2) / (2000 * pipe_diameter)
    return P