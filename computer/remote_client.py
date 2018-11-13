from socket import *
import pygame
from pygame.locals import *

# create a socket and bind socket to the host
pygame.init()
window = pygame.display.set_mode((160, 1))
client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(('192.168.1.174', 8004))

def control():
    gear = 1
    while True:
        for event in pygame.event.get():
                if event.type == KEYDOWN:
                    key_input = pygame.key.get_pressed()

                    # gaenge
                    if key_input[pygame.K_1]:
                        print("Erster Gang")
                        gear = 1

                    if key_input[pygame.K_2]:
                        print("Zweiter Gang")
                        gear = 2
                    if key_input[pygame.K_3]:
                        print("Dritter Gang")
                        gear = 3
                    if key_input[pygame.K_8]:
                        print("Lock")
                        client_socket.send(str(15))
                    if key_input[pygame.K_9]:
                        print("Unlock")
                        client_socket.send(str(16))


                    # simple Eingaben
                    elif key_input[pygame.K_KP8]:
                        print("Vorwaerts")
                        if gear == 1:
                            client_socket.send(str(1))
                        elif gear == 2:
                            client_socket.send(str(2))
                        elif gear == 3:
                            client_socket.send(str(3))

                    elif key_input[pygame.K_KP2]:
                        print("Rueckwaerts")
                        client_socket.send(str(4))

                    elif key_input[pygame.K_KP6]:
                        print("Rechts")
                        client_socket.send(str(5))

                    elif key_input[pygame.K_KP4]:
                        print("Links")
                        client_socket.send(str(6))


                    # komplexe Eingaben
                    if key_input[pygame.K_KP9]:
                        print("Vorwaerts Rechts")
                        if gear == 1:
                            client_socket.send(str(7))
                        elif gear == 2:
                            client_socket.send(str(8))
                        elif gear == 3:
                            client_socket.send(str(9))

                    elif key_input[pygame.K_KP7]:
                        print("Vorwaerts Links")
                        if gear == 1:
                            client_socket.send(str(10))
                        elif gear == 2:
                            client_socket.send(str(11))
                        elif gear == 3:
                            client_socket.send(str(12))

                    elif key_input[pygame.K_KP3]:
                        print("Rueckwaerts Rechts")
                        client_socket.send(str(13))

                    elif key_input[pygame.K_KP1]:
                        print("Rueckwaerts Links")
                        client_socket.send(str(14))


                    # exit
                    elif key_input[pygame.K_x] or key_input[pygame.K_q]:
                        print 'Exit'
                        client_socket.close()
                        break

		elif event.type == KEYUP:
		    print("Reset")
                    client_socket.send(str(0))

if __name__ == '__main__':
    control()
