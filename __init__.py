DEVELOPER_MODE = False

def unitTest():
    print("Hello, world!")
    pass

def run():
    print("Running")
    pass

if __name__ == "__main__":
    if DEVELOPER_MODE:
        unitTest()
    else:
        run()