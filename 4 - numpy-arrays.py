import numpy as np
import math

# DOT PRODUCT

# regions data temp - rainfall - humidity
kanto = [73, 67, 43]
johto = [91, 88, 64]
hoenn = [87, 134, 58]
sinnoh = [102, 43, 37]
unova = [69, 96, 70]

# weights of data
weights = [0.3, 0.2, 0.5]


kanto = np.array(kanto)
johto = np.array(johto)
hoenn = np.array(hoenn)
sinnoh = np.array(sinnoh)
unova = np.array(unova)


def calculate_yield(region_name, region_data, weights):
    # (region_data * weights).sum()
    print(f"Yield in {region_name} region is {math.ceil(np.dot(region_data, weights))}")


kanto_yield = calculate_yield("Kandto", kanto, weights)
johto_yield = calculate_yield("Johto", johto, weights)
hoenn_yield = calculate_yield("Hoenn", hoenn, weights)
sinnoh_yield = calculate_yield("Sinnoh", sinnoh, weights)
unova_yield = calculate_yield("Unova", unova, weights)
