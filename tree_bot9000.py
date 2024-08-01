import pyautogui
import time

def initial_mine():
    # Look up a little bit
    print("Looking up by 300 pixels")
    pyautogui.moveRel(0, -300, duration=0.2)

    pyautogui.mouseDown(button='left')
    print("Start mining")

    time.sleep(0.8)

    # Look up a tiny bit more
    print("Looking up by 100 pixels")
    pyautogui.moveRel(0, -100, duration=0.3)

    # Continue mining
    time.sleep(1.1)

    # Stop mining
    pyautogui.mouseUp(button='left')
    print("Stop mining")

    pyautogui.keyDown('space')
    pyautogui.keyDown('w')
    time.sleep(0.6)
    pyautogui.keyUp('space')
    pyautogui.keyUp('w')
    pyautogui.moveRel(0, 175, duration=0.2)

def mine_tree():

    # Turn left by moving the mouse left
    print("Turning left by 320 pixels")
    pyautogui.moveRel(-319, 0, duration=0.5)

    # Start mining while looking up and down
    print("Start mining")
    pyautogui.mouseDown(button='left')
    time.sleep(0.1)
    pyautogui.moveRel(0, -101, duration=0.3)
    time.sleep(0.3)
    pyautogui.moveRel(0, 100, duration=0.3)
    time.sleep(0.1)

    # Stop mining
    pyautogui.mouseUp(button='left')
    print("Stop mining")

    pyautogui.keyDown('w')
    time.sleep(0.05)
    pyautogui.keyDown('space')
    pyautogui.keyUp('space')
    time.sleep(0.2)
    pyautogui.keyUp('w')

    # Wait before starting again
    time.sleep(1)


def main():
    print("Starting in 3 seconds...")
    time.sleep(3)  # Time to switch to Minecraft

    try:
        # Initial mining process
        initial_mine()
        print("Initial mine")

        # Repeating process from jumping and moving forward
        while True:
            mine_tree()
            print("Tree mine")
            # Additional delay between cycles if needed
            time.sleep(1)
    except KeyboardInterrupt:
        print("Script stopped by user.")

if __name__ == "__main__":
    main()
