
# Full Report on Lambda-CDM Cosmological Model

## Introduction

This project explores the behavior of the standard cosmological model, known as the Lambda-CDM model. This model describes the Universe as flat and made of three main components: matter (including dark matter), radiation, and dark energy represented as a cosmological constant. The numerical values used here follow the Planck 2018 measurements.

The project consists of three major tasks:

1. Computing and plotting how the expansion rate of the Universe changes with redshift.
2. Calculating the age of the Universe using numerical integration.
3. Solving for the time evolution of the scale factor, which describes how distances in the Universe grow with time.

---

## Part 1: Computing and Plotting the Expansion Rate

A function is written to compute the expansion rate of the Universe as a function of redshift. This function includes the contribution of matter, radiation, and dark energy. Using this function, the expansion rate is calculated for a wide range of redshifts and displayed on a plot.

The plot shows the expected physical behavior:

* At low redshift, which corresponds to recent cosmic times, the expansion rate changes slowly.
* At intermediate redshift, the Universe was dominated by matter, and the expansion rate increases more quickly.
* At very high redshift, the radiation component becomes dominant, causing the expansion rate to rise extremely fast.

The shape of the plot matches the well-established behavior known from cosmology.

---

## Part 2: Computing the Age of the Universe

In this section, a numerical integration method is used to determine the age of the Universe. The integration is based on a relation that connects cosmic time to redshift. Since the computation must be performed in physical units, the Hubble constant is converted into units of per-second.

The integral is then evaluated from redshift zero to a very large value. Using a high upper limit works well because extremely early times contribute very little to the total age.

After converting the result into billions of years, the computed age is approximately thirteen point seven billion years. This agrees closely with the widely accepted value from the Planck mission, which is around thirteen point eight billion years. This confirms that the numerical implementation is correct.

---

## Part 3: Solving the Evolution of the Scale Factor

This part of the project involves solving the equation that describes how the scale factor evolves over time. The scale factor indicates how distances between points in the Universe grow as time passes. The equation for the scale factor depends on the same components as before: matter, radiation, and dark energy.

A numerical differential-equation solver is used to compute the evolution. The initial value of the scale factor is chosen to be extremely small to represent an early stage of the Universe. The system is then evolved forward in time up to fourteen billion years.

The resulting plot clearly shows the three well-known phases of cosmic history:

1. **Radiation era:** very rapid early expansion.
2. **Matter era:** expansion slows and follows a smoother growth.
3. **Dark-energy era:** expansion begins to accelerate again in the later Universe.

The scale factor reaches its present-day value at roughly the same time as the age computed in the previous section, confirming that the model and the code are internally consistent.

---

## Conclusion

This project successfully reproduces the key predictions of the Lambda-CDM cosmological model. The calculated expansion rate, the numerical estimate of the age of the Universe, and the evolution of the scale factor all match both theoretical expectations and observational data. The results demonstrate the correctness of the numerical implementation and the internal consistency of the Lambda-CDM framework.

