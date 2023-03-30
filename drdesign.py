def balance_power(mass, propel_diam, motor_eff, propel_eff):
    """
    Calculate how much power is required to provide a thrust to a
    drone that matches its weight, given a certain configuration
    of propellers and motors.

    :param mass: Mass (in kg)
    :param propel_diam: Propellers diameter (in meters)
    :param motor_eff: Motor efficiency (between 0 and 1)
    :param propel_eff: Propellers efficiency (between 0 and 1)
    :return: The power required to generate a lift that balances the weight
        of the vehicle, in Watts
    """
    import math

    # Air density at sea level and room temperature is about 1.225 kg/m^3
    density = 1.225
    # Gravity acceleration = 9.8 m/s^2
    g = 9.8

    return (
            (1/(propel_diam * motor_eff * propel_eff)) *
            math.sqrt((2 * math.pow(mass,3) * math.pow(g,3))/(math.pi * density))
    )
