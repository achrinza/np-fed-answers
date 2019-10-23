from game import Game

def main():
    game = Game()
    game.start()

if __name__ == "__main__":
    try:
        main()

    # Catch the earliest KeyboardInterrupt that Game() couldn't catch.
    except KeyboardInterrupt:
        print()
        print("=======================")
        print("Early KeyboardInterrupt")
        print("Exiting...")
        print("=======================")