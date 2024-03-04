from matplotlib import pyplot as plt
import fastf1
import fastf1.plotting

fastf1.plotting.setup_mpl()

session = fastf1.get_session(2024, 'Bahrain', 'Q')

session.load()
fast1 = session.laps.pick_driver('LEC').pick_fastest()
car1_data = fast1.get_car_data()
t1 = car1_data['Time']
vCar1 = car1_data['Speed']

fast2 = session.laps.pick_driver('VER').pick_fastest()
car2_data = fast2.get_car_data()
t2 = car2_data['Time']
vCar2 = car2_data['Speed']

# The rest is just plotting
fig, ax = plt.subplots()
ax.plot(t1, vCar1, label='LEC', color='red')
ax.plot(t2, vCar2, label='VER', color='blue')
ax.set_xlabel('Time [s]')
ax.set_ylabel('Speed [km/h]')
ax.set_title('LEC vs VER fastest lap - 2024 Bahrain GP Qualifying')
ax.legend()
plt.show()