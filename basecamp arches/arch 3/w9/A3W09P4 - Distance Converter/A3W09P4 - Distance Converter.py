class Converter:
    to_meter = {
        'meters': 1.0,
        'inches': 0.0254,
        'feet': 0.3048,
        'yards': 0.9144,
        'miles': 1609.344,
        'kilometers': 1000.0,
        'centimeters': 0.01,
        'millimeters': 0.001
    }

    def __init__(self, length, unit):
        unit = unit.lower()
        if unit not in self.to_meter:
            raise ValueError(f"unsupported unit: {unit}")
        self.meter = length * self.to_meter[unit]

    def meters(self):
        return self.meter

    def inches(self):
        return self.meter / self.to_meter['inches']

    def feet(self):
        return self.meter / self.to_meter['feet']

    def yards(self):
        return self.meter / self.to_meter['yards']

    def miles(self):
        return self.meter / self.to_meter['miles']

    def kilometers(self):
        return self.meter / self.to_meter['kilometers']

    def centimeters(self):
        return self.meter / self.to_meter['centimeters']

    def millimeters(self):
        return self.meter / self.to_meter['millimeters']