# drone.py
"""
An IDLE-shell session
-----------------------------------------------------------------
>>> qc1 = QuadCopter()
>>> qc1.move([(0,0,1000)])
...flying...
'flown: 10.0 meter, 253.0625 seconds left'
>>> qc1.move([(0,0,1000),(1000,0,0),(200,200,-200),(77,0,0),(0,0,-500)])
...flying...
...flying...
...flying...
...flying...
...flying...
'flown: 39.23410161513776 meter, 188.3125 seconds left'
>>> qc1.move([(0,0,1000)])
...flying...
'flown: 49.23410161513776 meter, 100.296875 seconds left'
>>> print(qc1)
      distance: 49.23410161513776   
      dt_start: 2015-06-11 17:15:31.468750
      maxspeed: 0.5                 
       maxtime: 300                 
      position: (1277, 200, 2300)   
   secondsleft: 96.859375           
     spaceunit: 0.01                

>>> qc1.move([(0,0,1000),(1000,0,0),(200,200,-200),(77,0,0),(0,0,500)])
...flying...
...flying...
...flying...
...flying...
...flying...
'flown: 78.4682032302755 meter, 24.703125 seconds left'
>>> qc1.move([(0,0,1000)])
...flying...
'Battery empty: crash!!'
-----------------------------------------------------------------
"""

import datetime as dt
import time
import math

class Drone(object):
    """Generalisation of a flying machine"""
    # resolution of our 3d model in meters
    spaceunit = 0.01  # 1 cm
        

class QuadCopter(Drone):
    """Remote controlled helicopter with four roters"""
    # constructor
    def __init__(self, start_position_xyz=(0, 0, 0), max_meter_per_sec=0.5, battery_life_secs=100):
        self.position = start_position_xyz
        self.maxspeed = max_meter_per_sec
        self.maxtime  = battery_life_secs
        self.dt_start  = dt.datetime.utcnow()
        self.distance  = 0   # total distance flown in meters

    @property
    def secondsleft(self):
        """remaining battery life"""
        return self.maxtime - (dt.datetime.utcnow() - self.dt_start).total_seconds()

    # printer
    def __str__(self):
        """print (instance)"""
        toprint = dict([(attr, getattr(self,attr)) for attr in dir(self) \
                        if not attr.startswith('__') and not 'method' in str(getattr(self,attr))])
        result =''
        for key in sorted(toprint):
            result += "{:>14}: {:<30}\n".format(key, str(toprint[key]))
        return result    


    def move(self, command_list=[(0,0,0)]):
        """ Moves the quadcopter.
        - A command is a tuple(backward_forward, left_right, down_up).
        - Example:  (0,0,100) moves the QC 100 units (1 meter)  up.
        - Example:  (-10,0,0) moves the QC 10 units backwards.
        - Example:  (0,100,-10) moves the QC 100 units to the right and 10 units down.
        Before and after every move/command the battery life (secondsleft) is checked.
        A move calculates the distance covered, the new position, and the time it takes
        to fly the distance at max speed. When the QC is flying no new commands will
        be processed (time.sleep(seconds_flying)).
        """
        self.command = command_list
        secondsflown = 0
        # we maken een lijst van de positie-tuple om die te kunnen updaten
        positie = list(self.position)
        # we loopen door de command_list
        for total_command in self.command:
            for command in total_command:
                diepte = total_command[0]
                breedte = total_command[1]
                hoogte = total_command[2]
                # we berekenen de afstand die per command wordt afgelegd
                # (**0.5 = wortel), /100 om de afstand in cm om te zetten naar meters
                afstand = ((diepte**2) + (breedte**2) + (hoogte**2))**0.5/100
                seconds_flying = afstand / self.maxspeed
            # we bekijken of er nog batterij over is
            if seconds_flying < self.secondsleft:
                print('...flying...')
                #we wachten de vliegtijd af om met de volgende te kunnen starten
                time.sleep(seconds_flying)
                # we updaten de afgelegde afstand
                self.distance += afstand
                # we updaten de gevlogen tijd
                secondsflown += seconds_flying
                # en we updaten de positie per eenheid
                positie[0] += diepte
                positie[1] += breedte
                positie[2] += hoogte
                # die we vervolgens weer omzetten naar een tuple
                self.position = tuple(positie)
                
            elif seconds_flying >= self.secondsleft and self.secondsleft > 0:
                #wat als de batterij opraakt tijdens de vlucht
                print('...flying...')
                #dan legt ie de afstand af tot de batterij dood is
                self.distance += afstand * (self.secondsleft/seconds_flying)
                # en updaten we de positie met de afgelegde afstand
                # zodat je de drone kunt terugvinden, hoogte is dan natuurlijk 0
                positie[0] += diepte* (self.secondsleft/seconds_flying)
                positie[1] += breedte* (self.secondsleft/seconds_flying)
                positie[2] = 0.0
                # hij vliegt nog zolang als hij batterijtijd heeft
                time.sleep(self.secondsleft)
                # hij crasht
                print('Battery empty: crash!')
                # we updaten de gevlogen tijd met de tijd die er nog was tot de crash
                secondsflown += self.secondsleft
                # en updaten de positie om je drone te kunnen terugvinden
                self.position = tuple(positie)
            elif self.secondsleft <= 0:
                # als er nog opdrachten komen om te vliegen na de crash
                print('Battery emtpy!')

        print('flown:', self.distance, 'meter', self.secondsleft, 'seconds left')
        
    
# tests
### aantal extra tests meegegeven omdat in het idle voorbeeld de tijd ###
### volgens mij niet goed afloopt, iig niet met 0.5m/s ###
qc1 = QuadCopter()
qc1.move([(0,0,1000)])
qc1.move([(0,0,1000),(1000,0,0),(200,200,-200),(77,0,0),(0,0,-500)])
qc1.move([(0,0,1000)])
print(qc1)
qc1.move([(0,0,1000),(1000,0,0),(200,200,-200),(77,0,0),(0,0,500)])
qc1.move([(0,0,1000),(1000,0,0),(200,200,-200),(77,0,0),(0,0,500)])
qc1.move([(0,0,2000),(1500,0,0),(200,200,-200),(77,0,0),(0,0,500)])
print(qc1)


        
    
    
                                

    
    

    
        
