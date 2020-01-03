

stopTimesFile = open('stop_times.txt','w')
routesFile = open('routes.txt','w')
tripsFile = open('trips.txt','w')
stopTimesFile.write('trip_id,arrival_time,departure_time,stop_id,stop_sequence,stop_headsign,pickup_type,drop_off_time,shape_dist_traveled\n')
tripsFile.write('route_id,service_id,trip_id,trip_headsign,direction_id,block_id,shape_id\n')
routesFile.write('route_id,agency_id,route_short_name,route_long_name,route_desc,route_type,route_url,route_color,route_text_color\n')

for metroline, route_id in [(1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7),(8,'1e'),(9,'4e')]:
    routesFile.write(f'{route_id},TehranMetro,{route_id},,,,,,\n')    
    for direction in [1,2]:
        for day, service_id in [(1,'Weekdays'),(2,'Thursdays'),(3,'Fridays'),(4,'Holidays')]:
            fid = open(f'line{metroline}{direction}{day}.csv')
            fid.readline()
            
            # getting header of file
            stationIDs = fid.readline().split(',')
            while (not(stationIDs[0].isnumeric())):
                stationIDs = fid.readline().split(',')
                
            stationIDs = list(map( lambda x:x.strip(), stationIDs))
            
            trips = fid.readlines()
            for service, tripTimes in enumerate(trips):
                tripid = f'line{route_id}_dir{direction}_{service_id}_service{service}'
                
                tripsFile.write(f'{route_id},{service_id},{tripid},,{direction-1},,\n')
                
                
                # updating the stop_times files
                tripTimes = tripTimes.split(',')
                stopNo = 0
                for j, stopTime in enumerate(tripTimes):
                    stopTime = stopTime.strip()
                    if (stopTime):
                        stopNo += 1
                        stopTimesFile.write(f'{tripid},{stopTime}:00,{stopTime}:00,{stationIDs[j]},{stopNo+1},,,,\n')
            
stopTimesFile.close()
tripsFile.close()
routesFile.close()