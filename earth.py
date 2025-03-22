"""This file holds all WGS84 (World Geodetic System 1984) paramters such as curvature, rotation rate and gravity model."""

import numpy as np



class Earth():
    def __init__(self):
        self.rate = 7.292115e-5
        self.A = 6378137.0                  #semi_major_axis
        self.E2 = 6.6943799901413e-3        #Squared eccentricity of Earth ellipsoi
        self.GE = 9.7803253359              ##: Gravity at the equator
        self.GP = 9.8321849378              #gravity at the pole
        self.F = (1 - self.E2) ** 0.5 * self.GP / self.GE - 1



    def principal_radii(self,lat, alt):
        """Compute the principal radii of curvature of Earth ellipsoid.

        Parameters
        ----------
        lat, alt : array_like
        Latitude and altitude.

        Returns
        -------
        rn : float or ndarray
            Principle radius in North direction.
        re : float or ndarray
            Principle radius in East direction.
        rp : float or ndarray
            Radius of cross-section along the parallel.
        """
        self.sin_lat = np.sin(np.deg2rad(lat))
        self.cos_lat = np.sqrt(1 - self.sin_lat**2)

        x = 1 - self.E2 * self.sin_lat**2
        re = self.A / np.sqrt(x)
        rn = re * (1 - self.E2) / x

        return rn + alt, re + alt, (re + alt) * self.cos_lat
