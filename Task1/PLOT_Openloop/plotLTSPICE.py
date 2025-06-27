import pandas as pd
import matplotlib.pyplot as plt

# Baca file CSV (ubah path kalau perlu)
df = pd.read_csv("plotLTSPICE.csv")

# Tampilkan beberapa baris awal (opsional)
print(df.head())

# Plot grafik
plt.figure(figsize=(10, 6))
plt.plot(df['time'], df['V(n001)'], label='V(n001)', color='blue')
plt.plot(df['time'], df['V(n003)'], label='V(n003)', color='green')
plt.plot(df['time'], df['I(R1)'], label='I(R1)', color='red')

# Penyesuaian tampilan
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Plot dari CSV File')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()