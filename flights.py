import random as rndm
from scipy import stats
from numpy import percentile
import string
import logging
from collections import namedtuple

MAX_WEIGHT = 200000
MIN_WEIGHT = 200
MAX_WING_AREA = 900
MIN_WING_AREA = 25

TURBULENCE_SIGMA = 0.75
WINGS_SIGMA = 0.2
TURBULENCE_FACTOR = 3

InfoObject = namedtuple('InfoObject', ['flight_code', 'old_angle', 'disruption',
                                       'after_disruption', 'correction', 'angle'])


class Environment:

    def __init__(self):
        self.planes = []

    def add_plane(self):
        self.planes.append(Plane())

    def turbulence(self):
        while True:
            for plane in self.planes:
                old_angle = plane.wings_angle
                turbulence_value = rndm.gauss(0, TURBULENCE_SIGMA)
                disruption = plane.disrupt_plane(turbulence_value)
                after_disruption = plane.wings_angle
                correction = plane.tilt_correction()
                yield InfoObject(plane.flight_code, old_angle, disruption, after_disruption,
                                 correction, plane.wings_angle)


class Plane:

    def __init__(self):
        self.flight_code = set_flight_code()
        self.weight_percentile = 0
        self.wing_area_percentile = 0
        self.weight = rndm.randint(MIN_WEIGHT, MAX_WEIGHT)
        self.wing_area = 0
        self.turbulence_sensitivity_factor = 0

        self.set_other_properties(self.weight)

        self.wings_angle = 0

    def set_other_properties(self, weight):
        self.weight_percentile = stats.percentileofscore(range(MIN_WEIGHT, MAX_WEIGHT), weight)
        mean_value = percentile((MIN_WING_AREA, MAX_WING_AREA), int(round(self.weight_percentile)))
        self.wing_area = int(round(rndm.gauss(mean_value, mean_value * WINGS_SIGMA)))
        self.wing_area_percentile = stats.percentileofscore(range(MIN_WING_AREA, MAX_WING_AREA), self.wing_area)
        self.turbulence_sensitivity_factor = self.weight_percentile / self.wing_area_percentile

    def disrupt_plane(self, turbulence_value):
        disruption = turbulence_value * TURBULENCE_FACTOR * self.turbulence_sensitivity_factor
        self.wings_angle += disruption
        return disruption

    def tilt_correction(self):
        correction = (rndm.random() * rndm.randint(0, abs(int(self.wings_angle))))
        if correction == 0:
            correction = rndm.random()
            while correction > abs(self.wings_angle):
                correction = rndm.random()

        if self.wings_angle > 0:
            self.wings_angle -= correction
            correction = -correction
        else:
            self.wings_angle += correction

        return correction


def set_flight_code():
    code = ''.join(rndm.choice(string.ascii_uppercase) for _ in range(2))
    code += ''.join(rndm.choice(string.digits) for _ in range(4))
    return code


if __name__ == "__main__":
    e = Environment()
    e.add_plane()
    e.add_plane()
    e.add_plane()
    e.add_plane()
    for t in e.turbulence():
        logging.info(t.flight_code)
        logging.info("old angle: " + str(t.old_angle))
        logging.info("disruption: " + str(t.disruption))
        logging.info("after disruption: " + str(t.after_disruption))
        logging.info("tilt correction: " + str(t.correction))
        logging.info("new angle: " + str(t.angle))
        logging.info("------------------------\n")
