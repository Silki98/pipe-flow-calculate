# Pipe Flow Calculator
# Calculates velocity, Reynolds number, flow type, friction factor and
# pressure drop for water or any other fluid flowing in a straight circular pipe.
#
# How to run: paste this code in one Google Colab cell (or run it in any
# Python environment) and type your values when asked.
# Press Enter to use the default value (water at about 20 C).
# After the result you can try new values without running the code again.

import numpy as np
import matplotlib.pyplot as plt


def get_value(question, default):
    # Keeps asking until the user enters a valid positive number
    while True:
        text = input(question + " [default " + str(default) + "]: ")
        if text == "":
            return default
        try:
            number = float(text)
        except ValueError:
            print("   Please enter a number, for example 0.05")
            continue
        if number <= 0:
            print("   The number must be greater than 0")
            continue
        return number


again = "y"

while again == "y":

    print()
    print("===== Pipe Flow Calculator =====")

    # Step 1: take the input values from the user
    density = get_value("Fluid density (kg/m3)", 1000)
    viscosity = get_value("Dynamic viscosity (Pa.s)", 0.001)
    diameter = get_value("Pipe inner diameter (m)", 0.05)
    length = get_value("Pipe length (m)", 10)
    flow_rate = get_value("Flow rate (m3/s)", 0.002)

    # Step 2: cross-sectional area of the pipe, A = pi * D^2 / 4
    area = 3.14159 * diameter**2 / 4

    # Step 3: velocity = flow rate / area
    velocity = flow_rate / area

    # Step 4: Reynolds number, Re = density * velocity * diameter / viscosity
    Re = density * velocity * diameter / viscosity

    # Step 5: decide the flow type and calculate the friction factor
    if Re < 2100:
        flow_type = "Laminar"
        f = 64 / Re                      # laminar flow: f = 64 / Re
    elif Re > 4000:
        flow_type = "Turbulent"
        f = 0.316 / Re**0.25             # turbulent flow: Blasius equation
    else:
        flow_type = "Transition (result is approximate)"
        f = 0.316 / Re**0.25

    # Step 6: pressure drop (Darcy-Weisbach equation)
    # pressure drop = f * (L / D) * (density * velocity^2 / 2)
    pressure_drop = f * (length / diameter) * (density * velocity**2 / 2)

    # Step 7: print the results
    print()
    print("------ Results ------")
    print("Pipe area        =", round(area * 10000, 2), "cm2")
    print("Velocity         =", round(velocity, 3), "m/s")
    print("Reynolds number  =", round(Re))
    print("Flow type        =", flow_type)
    print("Friction factor  =", round(f, 4))
    print("Pressure drop    =", round(pressure_drop, 1), "Pa")

    if Re > 100000:
        print("Note: the Blasius equation is accurate only up to Re = 100,000, "
              "so this result is approximate.")

    # Step 8: calculate pressure drop for many flow rates, to draw the graph
    flow_list = np.linspace(0.25 * flow_rate, 2.5 * flow_rate, 40)
    pressure_list = []

    for q in flow_list:
        v = q / area
        re = density * v * diameter / viscosity
        if re < 2100:
            ff = 64 / re
        else:
            ff = 0.316 / re**0.25
        dp = ff * (length / diameter) * (density * v**2 / 2)
        pressure_list.append(dp)

    # Step 9: plot the graph
    plt.figure(figsize=(7, 4))
    plt.plot(flow_list, pressure_list)
    plt.scatter([flow_rate], [pressure_drop], color="red", label="Your input")
    plt.xlabel("Flow rate (m3/s)")
    plt.ylabel("Pressure drop (Pa)")
    plt.title("Pressure drop vs flow rate")
    plt.grid(True)
    plt.legend()
    plt.show()

    # Step 10: ask whether to try new values
    again = input("Try different values? (y/n): ").strip().lower()

print("Thank you!")
