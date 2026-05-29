from application.app import App

def main():
    app = App()

    try:
        app.run()
    except KeyboardInterrupt:
        print("Exit")


if __name__ == "__main__":
    main()
