'''Tom Eade - April 2026
    Single Lap speed trace
    Use FastF1 to create a speed trace
    interactive - allow user input for session, driver, lap'''

import fastf1
import plotly.graph_objects as go
import os

#create cache if not already and saves any downloads into cache
os.makedirs('cache', exist_ok=True)
fastf1.Cache.enable_cache('cache')

#While True loops allow for input choices without rerunning all code
while True:
#Input for race, year and session
    track = input('Input track/circuit: ')
#Ensure input for year is as a number
    while True:
        try:
            gpYear = int(input('Input year: '))
            break
        except ValueError:
            print('Input Year as number')

    Sess = input('Input Session (i.e. R, Q, FP1): ')

#Download session data with error cases
    try:
        session = fastf1.get_session(gpYear, track,Sess)
        session.load()
    except Exception as e:
        print(f'No session found, Check Input. Error {e}')
        continue

#Picking drivers and lap and loading
    while True:
        driver = input('Enter the driver name: i.e. VER, NOR etc. ')
        while True:
            try:
                lap_no = int(input('Enter lap - if fastest enter 0: '))
                break
            except ValueError:
                print('Input Lap number as integer')
        try:
            if lap_no == 0:
                lap = session.laps.pick_drivers(driver).pick_fastest()
                if lap.empty:
                    print(f'Driver {driver} not found - check driver code')
                    continue
                lap_label = 'Fastest Lap'
            else:
                lap = session.laps.pick_drivers(driver)
                if lap.empty:
                    print(f'Driver {driver} not found - check driver code')
                    continue
                lap = lap[lap['LapNumber'] == lap_no]
                if lap.empty:
                    print(f'Lap {lap_no} not found for {driver}')
                    continue
                lap_label = f'Lap {lap_no}'
        except Exception as e:
            print(f'Error selecting lap. Error: {e}')
            continue
#Load telemetry data, exception to handle edge case i.e. corrupt/missing data
        try:
            tel = lap.get_telemetry()
        except Exception as e:
            print(f'lap telemetry not found - Error: {e}')
            continue

#Plot distance against speed for lap
        fig = go.Figure()
        fig.add_trace(go.Scatter
                  (x=tel['Distance'],
                   y=tel['Speed'],
                   mode='lines',
                   name = driver))
        fig.update_layout(
            title = f'{driver} {track} {Sess} {gpYear}: {lap_label}',
            xaxis_title='Distance (m)',
            yaxis_title='Speed (km/h)',
            hovermode = 'x unified'
        )
        fig.show()
#Allow user to change data without rerunning whole code
        change = input('Change session/driver+lap/exit? ')
        if change == 'session':
            break
        elif change == 'exit':
            exit()
