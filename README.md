# Calculating a Module's IV Curves

## UG EEE 4531

## Brief Description:
Examples of modeling IV curves using a single-diode circuit equivalent model.

Calculating a module IV curve for certain operating conditions is a two-step process. Multiple methods exist for both parts of the process. Here we use the De Soto model [1]_ to calculate the electrical parameters for an IV curve at a certain irradiance and temperature using the module's base characteristics at reference conditions. Those parameters are then used to calculate the module's IV curve by solving the single-diode equation using the Lambert W method.

The single-diode equation is a circuit-equivalent model of a PV cell and has five electrical parameters that depend on the operating conditions. For more details on the single-diode equation and the five parameters, see the `PVPMC single diode page <https://pvpmc.sandia.gov/modeling-steps/2-dc-module-iv/diode-equivalent-circuit-models/>`.

## References
- [1] W. De Soto et al., "Improvement and validation of a model for photovoltaic array performance", Solar Energy, vol 80, pp. 78-88, 2006.

## Python Frameworks Used:
- pvlib
- pandas
- matplotlib
