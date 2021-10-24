""" 
    Unit converter
    Convert units to another. Includes temperatures, currency, volume and mass.
    Obviously, available conversions will be limited, but including more in the future won't be a big problem.
    INPUT:
    1) value - to be converted [NUMBER]
    2) unit (from) - unit from which to convert [STRING]
    3) unit (to) - unit to which to convert [STRING]
    OUTPUT:
    Converted value
"""


class Unit:
    def __init__(self, name, base, multiplier):
        self.name = name
        self.base = base
        self.mult = multiplier

    def get_name(self):
        return self.name

    def convert_to_si(self, value):
        return (value - self.base)/self.mult

    def convert_from_si(self, value):
        return self.base + self.mult*value


def get_value(text, container):
    v_str = input(text + ' (' + ','.join(container.keys()) + '): ')
    if v_str not in container.keys():
        print(v_str, 'not supported.')
        exit(0)
    else:
        return container[v_str]


# Static part - all units split by type and their conversion rates
conversions =   {'temperature': {
                    'C': Unit('C', 0, 1),
                    'F': Unit('F', 32, 1.8),
                    'K': Unit('K', 273.15, 1)
                    }
                }
# ----------------------

if __name__ == "__main__":
    units = get_value('What do you want to convert?', conversions)
    unit_from = get_value('Choose unit to convert from', units)
    unit_to   = get_value('Choose unit to convert to', units)
    
    value = None
    try:
        value = int(input('Provide value to convert: '))
    except:
        print('Incorrect value provided.')
        exit(0)
    
    value_si = unit_from.convert_to_si(value)
    value_converted = unit_to.convert_from_si(value_si)

    print('{:.2f}{} = {:.2f}{}'.format(value, unit_from.get_name(), value_converted, unit_to.get_name()))
