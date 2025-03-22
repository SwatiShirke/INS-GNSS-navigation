"""This file constains implementation for Unscented Kalman Filter for IMU-GNSS fusion."""

class UKF:
    def __ini__(self, P, Q, R, dt):
        self.P = P
        self.Q = Q
        self.R = R
        self.dt = dt
        self.kappa = 1
        self.alpha = 0.01
        self.beta = 2

    def predict(self):
        "to be implemented non linear state estimation model"

    def update(self):
        "TBD non linear meadurement model and update"

    def cal_nominal_covar():
        "TBD to calculate covariance for nominal state"

    def cal_estimate_covar():
        "TBD cal covarinace for final state estimation after updation"

    def cal_gain():
        pass 

    def cal_sensor_covar():
        "TBD sensor covariance"

        

