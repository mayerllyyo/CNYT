## Double Slit Experiment Simulation with Waves

### Objective

This project aims to simulate the double slit experiment using Python, focusing on the wave nature of light. By modeling light as waves and observing the interference pattern that emerges when these waves pass through two slits and overlap on a screen, we aim to gain insights into the phenomena of constructive and destructive interference.

### Background

The double slit experiment is a fundamental demonstration of the wave-particle duality of light and matter. When coherent light passes through two closely spaced slits, it creates an interference pattern of bright and dark fringes on a detection screen. This pattern results from the constructive and destructive interference of the waves emanating from the slits.

### References

For a deeper understanding of the mathematics behind interference, refer to:

- [Mathematics of Interference](https://phys.libretexts.org/Bookshelves/University_Physics/University_Physics_(OpenStax)/University_Physics_III_-_Optics_and_Modern_Physics_(OpenStax)/03%3A_Interference/3.03%3A_Mathematics_of_Interference)

### Task

Your task is to simulate the wave interference pattern using Python. Below are the steps to accomplish this:

1. **Setup the Environment**: Ensure you have Python installed along with the necessary libraries such as NumPy for numerical calculations and Matplotlib for plotting.

2. **Define Parameters**:
   - Define the distance between the slits, the wavelength of the light, the distance from the slits to the screen, and the number of points on the screen where intensity will be calculated.

3. **Model the Waves**:
   - Model each slit as a point source of waves using the Huygens-Fresnel principle.
   - Assume the wavefronts are straight lines perpendicular to the direction of propagation.

4. **Calculate Intensity**:
   - Use the principle of superposition to calculate the resultant wave amplitude at each point on the screen by summing the contributions from each slit.
   - The intensity of light at each point is proportional to the square of the amplitude of the resultant wave.

5. **Plot the Results**:
   - Plot the calculated intensity pattern on the screen using Matplotlib.
   - Observe the series of bright and dark fringes, demonstrating the interference pattern.

### Hints

- Utilize NumPy arrays for efficient calculations of wave amplitudes and intensities across the screen.
- Remember to consider the phase difference between the waves from the two slits, which contributes to constructive and destructive interference.

### Sample Code Skeleton

```python
import numpy as np
import matplotlib.pyplot as plt

# Define parameters
slit_distance = ...
wavelength = ...
screen_distance = ...
num_points = ...

# Model the waves
# Calculate intensity
# Plot the results
