#!/bin/python3
from sense_hat import SenseHat
from time import sleep
from math import sin
from random import choice

# Init
sense = SenseHat()

# Constants
ROWS = 8
COLS = 8


def gunnar():
    ### Conway's Game of Life ###
    # Constants
    live_colour = (255, 255, 255)
    dead_colour = (0, 0, 0)
    rand_area = ((2,2), (5,5))

    # Defining helper functions
    def count_neighbours(grid, pos_y, pos_x):
        neighbours = 0
        for y in range(-1, 2):
            for x in range(-1, 2):
                if grid[(pos_y + y) % ROWS][(pos_x + x) % COLS] == 1:
                    neighbours += 1
        return neighbours

    def print_to_led(grid, live_colour):
        led_array = [element for sublist in grid for element in sublist]
        sense.set_pixels([live_colour if cell == 1 else dead_colour for cell in led_array])

    def rainbow(n):
        colorsin = lambda x: int(127 * sin(x) + 127)
        return (colorsin(n), colorsin(n + 85), colorsin(n + 170))


    # Initializing grid with random data in the middle, seeded by sensor reading
    humidity = sense.get_humidity()
    seed = list(bin(hash(humidity))[2:])
    simulation = [[choice([int(n) for n in seed])
                    if rand_area[0][0] < x < rand_area[1][0]
                    or rand_area[0][1] < y < rand_area[1][1]
                    else 0
                    for x in range(ROWS)] for y in range(COLS)]


    # Run for 30 generations then quit
    for generation in range(30):
        live_colour = rainbow(generation)
        print_to_led(simulation, live_colour)
        for y, row in enumerate(simulation):
            for x, cell in enumerate(row):
                neighbours = count_neighbours(simulation, y, x)

                # Any live cell with fewer than two live neighbours
                # dies, as if by underpopulation.
                if (cell == 1) and (neighbours < 2):
                    cell = 0

                # Any live cell with two or three live neighbours lives
                # on to the next generation.
                elif (cell == 1) and (neighbours in [2, 3]):
                    cell = 1

                # Any live cell with more than three live neighbours dies,
                # as if by overpopulation.
                elif (cell == 1) and (neighbours > 3):
                    cell = 0

                # Any dead cell with exactly three live neighbours becomes
                # a live cell, as if by reproduction
                elif (cell == 0) and (neighbours == 3):
                    cell = 1

                simulation[y][x] = cell
        sleep(0.3)
    return humidity


def martin():
    r = (255, 0 , 0)
    g = (0, 255, 0)
    b = (0, 0, 255)
    
    c = (0, 180, 255)
    m = (255, 0, 199)
    y = (120, 255, 0)
    
    available_colors = [r, g, b, c, m, y]
    
    i = 0
    for i in range ( 0, 10):
      for _y in range (0, 8):
        for _x in range (0, 8):
          random_colors = choice(available_colors)
          sense.set_pixel(_x,_y, random_colors)
          _x += 1 
        _y += 1
        i += 1
        
    compass = sense.get_compass()
    return compass

def funksjonen_til_kristian():
  r = (255, 0, 0)
  g = (0, 255, 0)
  b = (0, 0, 255)
  
  c = (0, 255, 255)
  m = (255, 0, 255)
  y = (0, 255, 255)
  k = (0, 0, 0)
  w = (255, 255, 255)
  
  avalible_colors = [r, g, b, c, m, y, k]
  sense.set_rotation(90)
  
  myImage = [
    k, k, r, r, r, r, y, y,
    k, m, k, k, k, k, g, y,
    r, k, b, b, b, b, k, r,
    r, k, b, m, g, b, k, r,
    r, k, b, g, m, b, k, r,
    r, k, b, b, b, b, k, r,
    y, g, k, k, k, k, m, k,
    y, y, r, r, r, r, k, k,
    ]
  myImage2 = [
    w, k, r, r, r, r, y, y,
    w, m, k, k, k, k, g, y,
    w, k, b, b, b, b, k, r,
    w, k, b, m, g, b, k, r,
    w, k, b, g, m, b, k, r,
    w, k, b, b, b, b, k, r,
    w, g, k, k, k, k, m, k,
    w, y, r, r, r, r, k, k,
    ]
  myImage3 = [
    w, w, r, r, r, r, y, y,
    w, w, k, k, k, k, g, y,
    w, w, b, b, b, b, k, r,
    w, w, b, m, g, b, k, r,
    w, w, b, g, m, b, k, r,
    w, w, b, b, b, b, k, r,
    w, w, k, k, k, k, m, k,
    w, w, r, r, r, r, k, k,
    ]
  myImage4 = [
    w, w, w, r, r, r, y, y,
    w, w, w, k, k, k, g, y,
    w, w, w, b, b, b, k, r,
    w, w, w, m, g, b, k, r,
    w, w, w, g, m, b, k, r,
    w, w, w, b, b, b, k, r,
    w, w, w, k, k, k, m, k,
    w, w, w, r, r, r, k, k,
    ]
  myImage5 = [
    w, w, w, w, r, r, y, y,
    w, w, w, w, k, k, g, y,
    w, w, w, w, b, b, k, r,
    w, w, w, w, g, b, k, r,
    w, w, w, w, m, b, k, r,
    w, w, w, w, b, b, k, r,
    w, w, w, w, k, k, m, k,
    w, w, w, w, r, r, k, k,
    ]
    
  #--------------Bilder for oppover:  
  myImageUp = [
    k, k, r, r, r, r, y, y,
    k, m, k, k, k, k, g, y,
    r, k, b, b, b, b, k, r,
    r, k, b, m, g, b, k, r,
    r, k, b, g, m, b, k, r,
    r, k, b, b, b, b, k, r,
    y, g, k, k, k, k, m, k,
    y, y, r, r, r, r, k, k,
    ]
  myImageUp2 = [
    k, k, r, r, r, r, y, w,
    k, m, k, k, k, k, g, w,
    r, k, b, b, b, b, k, w,
    r, k, b, m, g, b, k, w,
    r, k, b, g, m, b, k, w,
    r, k, b, b, b, b, k, w,
    y, g, k, k, k, k, m, w,
    y, y, r, r, r, r, k, w,
    ]
  myImageUp3 = [
    k, k, r, r, r, r, w, w,
    k, m, k, k, k, k, w, w,
    r, k, b, b, b, b, w, w,
    r, k, b, m, g, b, w, w,
    r, k, b, g, m, b, w, w,
    r, k, b, b, b, b, w, w,
    y, g, k, k, k, k, w, w,
    y, y, r, r, r, r, w, w,
    ]
  myImageUp4 = [
    k, k, r, r, r, w, w, w,
    k, m, k, k, k, w, w, w,
    r, k, b, b, b, w, w, w,
    r, k, b, m, g, w, w, w,
    r, k, b, g, m, w, w, w,
    r, k, b, b, b, w, w, w,
    y, g, k, k, k, w, w, w,
    y, y, r, r, r, w, w, w,
    ]
  myImageUp5 = [
    k, k, r, r, w, w, w, w,
    k, m, k, k, w, w, w, w,
    r, k, b, b, w, w, w, w,
    r, k, b, m, w, w, w, w,
    r, k, b, g, w, w, w, w,
    r, k, b, b, w, w, w, w,
    y, g, k, k, w, w, w, w,
    y, y, r, r, w, w, w, w,
    ]
    
  
  
  sense.set_imu_config(True, True, True)
  
  
  def getIMUValues():
    # Gather all three sensor values from IMU
    compass = sense.get_compass()
    gyro = sense.get_gyroscope()
    accel = sense.get_accelerometer()
    
  
    return {"compass":compass, "accel":accel, "gyro":gyro}
    
  diff = 5
  var = 270
  
  t_end = time.time() + 10

  while time.time() < t_end:
    IMUValues = getIMUValues()
    compass = round(IMUValues["compass"])
    accel = (IMUValues["accel"])
    gyro = (IMUValues["gyro"]["pitch"])
    print(gyro)
    #nedover rot
    if gyro <= (90 + var) and gyro > (80 + var):
      sense.set_pixels(myImageUp)
    elif gyro <= (80 + var) and gyro > (75 + var):
      sense.set_pixels(myImageUp2)
    elif gyro <= (80 - diff + var) and gyro > (75 - diff + var):
      sense.set_pixels(myImageUp3)
    elif gyro <= (80 - diff*2 + var) and gyro > (75 - diff*2 + var):
      sense.set_pixels(myImageUp4)
    elif gyro <= (80 - diff*3 + var) and gyro > (75 - diff*3 + var):
      sense.set_pixels(myImageUp5)
    #oppover rot
    elif gyro >= (0) and gyro < (10):
      sense.set_pixels(myImage)
    elif gyro >= (10) and gyro < (15):
      sense.set_pixels(myImage2)
    elif gyro >= (10 + diff) and gyro < (15 + diff):
      sense.set_pixels(myImage3)
    elif gyro >= (10 + diff*2) and gyro < (15 + diff*2):
      sense.set_pixels(myImage4)
    elif gyro >= (10 + diff*3) and gyro < (15 + diff*3):
      sense.set_pixels(myImage5)
    else:
      sense.clear()

def main():
    with open("sensor_values.csv", "w") as csvfile:
        csvwriter = csv.writer(csvfile)
        
        # Main program loop
        while True:
            #aleksander()
            #andre()
            humidity = gunnar()
            #knut_ola()
            funksjonen_til_kristian()
            compass = martin()
            
            # Sensor values to be written in sensor_values.csv
            sensor_values = [humidity, compass]
            
            for value in sensor_values:
                csv_writer.writerow(sensor_values)
            
        
        
if __name__ == "__main__":
    main()
