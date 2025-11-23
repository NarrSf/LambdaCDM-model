import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad, solve_ivp

# ΛCDM Cosmological Parameters

H0 = 67.4                    # km/s/Mpc
Omega_m = 0.315
Omega_L = 0.685
Omega_r = 9.24e-5            # radiation density today

# 1)H(z)
def H_of_z(z):
    return H0 * np.sqrt(Omega_m*(1+z)**3 +
                        Omega_r*(1+z)**4 +
                        Omega_L)
z = np.logspace(0, 3.5, 600)
Hz = H_of_z(z)
plt.figure(figsize=(6,4))
plt.plot(z, Hz)
plt.xscale("log")
plt.xlabel("z")
plt.ylabel("H(z) [km/s/Mpc]")
plt.title("H(z) in flat ΛCDM")
plt.grid(True, which="both", ls="--", alpha=0.5)
plt.tight_layout()
plt.show()

# 2)Age of Universe

Mpc = 3.0856776e22           # meters
H0_SI = H0 * 1000 / Mpc      # s^-1
def dt_dz(z):
    return 1.0 / ((1+z) * H0_SI *
                  np.sqrt(Omega_m*(1+z)**3 +
                          Omega_r*(1+z)**4 +
                          Omega_L))
z_max = 1e4
t0_sec, err = quad(dt_dz, 0, z_max,
                   epsabs=0, epsrel=1e-8, limit=500)
Gyr = 3.154e16               # seconds in one Gyr
t0_Gyr = t0_sec / Gyr
print(f"Age of Universe = {t0_Gyr:.4f} Gyr")   # ≈ 13.8 Gyr

# 3)Solve for a(t) via ODE

def H_of_a(a):
    return H0_SI * np.sqrt(Omega_m/a**3 +
                           Omega_r/a**4 +
                           Omega_L)
def da_dt(t, a):
    return a[0] * H_of_a(a[0])
a_initial = 1e-8
t_end = 14 * Gyr
sol = solve_ivp(da_dt, (0, t_end), [a_initial],
                max_step=1e15, rtol=1e-6)
t = sol.t / Gyr
a = sol.y[0]
plt.figure(figsize=(6,4))
plt.plot(t, a)
plt.yscale("log")
plt.xlabel("t [Gyr]")
plt.ylabel("a(t)")
plt.title("Scale factor a(t) in ΛCDM")
plt.grid(True, which="both", ls="--", alpha=0.5)
plt.tight_layout()
plt.show()
