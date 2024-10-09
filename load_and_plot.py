import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np

dir_file = "/examples/signal_2009_009_M12_D17_CH_SENIN_HHN.npz"
data_npz = np.load(dir_file, allow_pickle=True)
data = {key: data_npz[key] for key in data_npz}

fig = plt.figure(figsize=(8, 6))
gs = gridspec.GridSpec(3, 1, height_ratios=[1, 1, 1])  # Three rows, one column

# Create the subplots
ax1 = fig.add_subplot(gs[0])
ax2 = fig.add_subplot(gs[1], sharex=ax1)
ax3 = fig.add_subplot(gs[2], sharex=ax1)

# Data for each plot
waveforms = ["earthquake_waveform_Z", "earthquake_waveform_N", "earthquake_waveform_E"]
axes = [ax1, ax2, ax3]

# Loop over axes to plot data and add common settings
for ax, waveform in zip(axes, waveforms):
    ax.plot(data[waveform], color="k")
    ax.set_xlim(0, 18000)
    ax.set_ylabel("Amplitude [m/s]")
    ax.axvline(x=6000, color='tab:red', linestyle='--', label="Earthquake signal start")
    ax.legend()

# Set x-label for the last axis
ax3.set_xlabel("Time [samples]")

ttl_str = "Magnitude " + str(data["magnitude"]) + " recorded in " + str(np.round(data["distance"],1))
ttl_str += " [km] at station " + str(data["code"][0]) + "." +str(data["code"][1]) + "." +str(data["code"][2][:2])
ax1.set_title(ttl_str)
# Display the plot
plt.tight_layout()
plt.show()
