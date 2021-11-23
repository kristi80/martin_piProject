from random import randint
from sense_hat import SenseHat
import time
import os

# Om du kjører koden lokalt kan du sette DEBUG til True.
# -- printer til terminal i stedet for RPi sensehat
DEBUG = True

if not DEBUG:
    from sense_hat import SenseHat
    sense = SenseHat()

ROWS = 8
COLS = 8

FPS = 5
FRAME_DURATION = 1 / FPS

GATE_FREQUENCY = 8
FUEL_FREQUENCY = 23
GATE_WIDTH = 2
CAR_Y_POS = 6
GAME_LENGTH = 200
CAR_COLOR = (255, 255, 255)
GATE_COLOR = (255, 0, 0)
NOCOLOR = (0, 0, 0)



def get_gate_pos():
    """Returner x-posisjon til gate som du skal treffe med bilen"""
    #Gjør så det er større sannsynlighet for å treffe porter i midten
    skew = lambda x: - (1/16) * (x - 4)**2 + 1

    port_pos = skew(random.randint(0, 99) / 100) 
    pass


def increment_buffer(buffer):
    """Flytt banen en piksel nedover"""
    pass


def intro_graphic():
    sense.low_light = True
    TheGame = 'THE GAME'
    sense.show_message('Welcome to', scroll_speed=0.06, text_colour=[0,0,0], back_colour=[194, 27, 209])

    sense.low_ligh = False
    for q in range(0, len(TheGame)-1, 2):
      sense.show_letter(TheGame[q], text_colour=[255, 255, 255], back_colour=[0, 0 ,0])
      time.sleep(0.5)
      sense.show_letter(TheGame[q+1], text_colour=[0,0,0], back_colour=[255, 255, 255])
      time.sleep(0.5)
    sense.low_light = True

    sense.show_message('Pitch to control', text_colour=[0,0,0], back_colour=[194, 27, 209])
    sense.clear()
    pass


def game_over_graphic(score):
    points = str(123) # midlertidig poengsum, for at proragm skal kjøre
 
    sense.low_light = True   # Lav lysintensitet

    sense.show_message("Game Over!", text_colour=[255, 0, 0], back_colour=[50, 166, 168])

    for p in range(0, len(points)):   # Prointer hvert siffer i poengsum
      sense.show_letter(points[p], back_colour=[194, 27, 209])
      time.sleep(0.5)
      sense.clear(194, 27, 209)  # Clearer ut forgie siffer
      time.sleep(0.5)

    sense.show_message("Points", back_colour=[194, 27, 209])   # Printer points til slutt
    sense.clear()  # Clearer matrise
    pass


def get_imu_values():
    """Få xyz-verdi"""
    _gyro = sense.get_gyroscope()
    pitch = _gyro["pitch"]
    return round(pitch)


def calculate_car_position(imu_values):
    """Returner x-posisjon for bilen"""
    if pitch in range(0, 5);
        return int(4)
    elif pitch in range(5, 10):
        return int(5)
    elif pitch in range(10, 15):
        return int(6)
    elif pitch in range(15, 20):
        return int(7)
    elif pitch in range(0, -5):
        return int(3)
    elif pitch in range(-5, -10):
        return int(2)
    elif pitch in range(-5, -10):
        return int(1)
    elif pitch in range(-10, -15):
        return int(0)
    else:
        pass


def debug_print(buffer):
    os.system("clear")
    for line in buffer:
        for char in line:
            if char == NOCOLOR:
                print("..", end="")
            if char == CAR_COLOR:
                print("XX", end="")
            if char == GATE_COLOR:
                print("OO", end="")
        print()
    print()


def main():
    running = True
    iterator = 0
    score = 0
    buffer = []

    ROWS = 8
    COLS = 8

    GATE_FREQUENCY = 8
    GATE_WIDTH = 4
    CAR_Y_POS = 1
    GAME_LENGTH = 120
    CAR_COLOR = (255, 255, 255)

    intro_graphic()

    #Spillet starter
    while running:
        #Finn nye gyro-verdier for xyz
        imu_values = get_imu_values()

        #Finn ut hvor bilen skal stå
        car_x_pos = calculate_car_position(imu_values)

        #TODO: Legg bilen til i printebuffer
        buffer[CAR_Y_POS][car_x_pos] = CAR_COLOR
        
        #Etter "GATE_FREQUENCY" iterasjoner, lag en ny gate
        if iterator % GATE_FREQUENCY == 0:
            gate_x_pos = get_gate_pos()
            gate_y_start = iterator


        #TODO: legg til fuel-tønner som dukker opp etter FUEL_FREQUENCY
        # antall iterasjoner. Når du treffer fuel fyller du opp baren
        # på høyre side av skjermen. Går du tom for fuel er spillet over.

        #Legg gaten til i printebuffer
        print(gate_x_pos)

        gate_y_pos = abs(iterator - gate_y_start)

        #Inkrementer iterator
        iterator += 1

        #Når bilen passerer en gate, sjekk om du traff
        if CAR_Y_POS == gate_y_pos:
            if gate_x_pos <= car_x_pos <= gate_x_pos + GATE_WIDTH:
                if car_x_pos == gate_x_pos + GATE_WIDTH // 2:
                    score += 3
                    print("Score + 3")
                else:
                    score += 1
                    print("Score + 1")


        #Inkrementer iterator
        iterator += 1

        #Print banen
        if DEBUG:
            debug_print(buffer)
        else:
            #Får alt over på éi liste i stedet for ei liste av lister
            flat_buffer = [element for sublist in buffer for element in sublist]

            #Printer til sensehat-skjermen
            sense.set_pixels(buffer)


        #Når det har gått GAME_LENGTH antall iterasjoner, stopp spillet
        if iterator >= GAME_LENGTH:
            game_over_graphics(score)
            running = False


if __name__ == "__main__":
    main()
