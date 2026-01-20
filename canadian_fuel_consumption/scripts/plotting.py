import matplotlib.pyplot as plt

def scatter_emissions(cdf):

    fig, axes = plt.subplots(1, 3, figsize=(18, 5))

    # 1. Consommation vs émissions
    axes[0].scatter(cdf['Combinee (L/100 km)'], cdf['Emissions de CO2 (g/km)'])
    axes[0].set_title("Relation entre la consommation et les émissions")
    axes[0].set_xlabel("Consommation combinée (L/100 km)")
    axes[0].set_ylabel("Émissions de CO2 (g/km)")

    # 2. Cylindrée vs émissions
    axes[1].scatter(cdf['Cylindree (L)'], cdf['Emissions de CO2 (g/km)'])
    axes[1].set_title("Relation entre la cylindrée et les émissions")
    axes[1].set_xlabel("Cylindrée (L)")
    axes[1].set_ylabel("Émissions de CO2 (g/km)")

    # 3. Cylindres vs émissions
    axes[2].scatter(cdf['Cylindres'], cdf['Emissions de CO2 (g/km)'])
    axes[2].set_title("Relation entre le nombre de cylindres et les émissions")
    axes[2].set_xlabel("Nombre de cylindres")
    axes[2].set_ylabel("Émissions de CO2 (g/km)")

    plt.tight_layout()
    plt.show()