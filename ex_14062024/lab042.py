numbers = int(input("enter a number\n"))
browsers = str(input("enter the browser name\n"))
browsers = browsers.lower()   #lower funtion will change the valuen in lower case in case user has giver browser name in laps

match browsers:
    case "chrome":
        print("crome code executed")
    case "firefox":
        print("ff code executed")
    case _:
        print("no browser code executed")