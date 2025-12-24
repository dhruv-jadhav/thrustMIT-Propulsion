import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
def noise_gen():
    file_path = r"C:\vs code\propulsion\thrustMIT-Propulsion\pressure_data_research_motor_knsb.csv"
    df = pd.read_csv(file_path)
    time_values = df['time'].tolist()
    base_pressure = df['pressure'].tolist()
    avg_pressure = np.mean(base_pressure)
    target_value = 2.603
    noise_avg = avg_pressure-target_value
    print(avg_pressure)
    noise_pressure = np.random.normal(0,np.sqrt((noise_avg)),len(base_pressure))
    noise_data = base_pressure + noise_pressure 
    return noise_data,base_pressure,time_values

noise_data,base_pressure,time_values = noise_gen()
fig, plots = plt.subplots(2, 2, figsize=(15,9))
plots[0,0].plot(time_values, base_pressure)
plots[0,1].plot(time_values, noise_data)
plots[0,0].set_title('base pressure')
plots[0,1].set_title('noise pressure')
fig.tight_layout()
plt.show()
data = {
    'Time': time_values,
    'Pressure': noise_data
}
df = pd.DataFrame(data)
df.to_csv('noise_motor_data.csv', index=False)
