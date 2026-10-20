# Pipe Flow Calculator

A Python tool that calculates the velocity, Reynolds number, flow type (laminar / transition / turbulent), friction factor and pressure drop for a fluid flowing through a straight circular pipe. It also plots pressure drop against flow rate.

## Features
- Takes user input for fluid density, viscosity, pipe diameter, pipe length and flow rate
- Press Enter to use default values (water at about 20 °C)
- Classifies the flow as laminar, transition or turbulent
- Plots pressure drop vs flow rate with your input marked on the graph
- Lets you try new values without restarting the program

## How to run
1. Open [Google Colab](https://colab.research.google.com) and create a new notebook.
2. Paste the code from `pipe_flow_input.py` into a cell and run it.
3. Type your values when asked.

To run locally: `pip install numpy matplotlib`, then `python pipe_flow_input.py`.

## Equations used
- Area: A = πD² / 4
- Velocity: v = Q / A
- Reynolds number: Re = ρvD / μ
- Friction factor: f = 64 / Re (laminar), f = 0.316 / Re^0.25 (turbulent, Blasius)
- Pressure drop (Darcy–Weisbach): ΔP = f · (L / D) · (ρv² / 2)

Flow type: Re < 2100 is laminar, Re > 4000 is turbulent, in between is transition.

## Example
Default input (water, D = 0.05 m, L = 10 m, Q = 0.002 m³/s):

| Quantity | Result |
|---|---|
| Velocity | 1.019 m/s |
| Reynolds number | 50930 |
| Flow type | Turbulent |
| Friction factor | 0.021 |
| Pressure drop | 2182.5 Pa |

## Limitations
- Only for straight, smooth, circular pipes (no bends, valves or fittings)
- The Blasius equation is accurate only up to about Re = 100,000
- Results in the transition zone (Re 2100 to 4000) are approximate

## Author
Silki Kumari, B.Tech Chemical Engineering, Banasthali Vidyapith

## License
MIT License
