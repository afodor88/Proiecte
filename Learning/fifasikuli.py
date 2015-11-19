alreadyopened = ""
while True:
    openApp(r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" + " --start-maximized")
    wait(15) # waits 15 seconds
    if exists("1447930681516.png"):
        alreadyopened = "1"
    if alreadyopened:
        if exists("1446954832967.png", 60):
            click("1446954832967.png")
            wait("1446677297757.png", 60)
            hover("1446677363463.png")
            hover("1446677556851.png")
            click("1446677392383.png")
            click("1446751479776.png")
            wait(15) # waits 5 seconds
            #closeApp("FIFA")
            click("1446763406004.png")
            wait(3600)

        else:
            wait("1446677297757.png", 60)
            hover("1446677363463.png")
            hover("1446677556851.png")
            click("1446677392383.png")
            click("1446751479776.png")
            wait(15) # waits 5 seconds
            #closeApp("FIFA")
            click("1446763406004.png")
            wait(3600)
    else:

        type("l", KeyModifier.CTRL) # press lowercase L + CTRL
        type("http://www.easports.com/fifa/football-club/ultimate-team")
        type(Key.ENTER)

        if exists("1446954832967.png", 60):
            click("1446954832967.png")
            wait("1446677297757.png", 60)
            hover("1446677363463.png")
            hover("1446677556851.png")
            click("1446677392383.png")
            click("1446751479776.png")
            wait(15) # waits 5 seconds
            #closeApp("FIFA")
            click("1446763406004.png")
            wait(3600)

        else:
            wait("1446677297757.png", 60)
            hover("1446677363463.png")
            hover("1446677556851.png")
            click("1446677392383.png")
            click("1446751479776.png")
            wait(15) # waits 5 seconds
            #closeApp("FIFA")
            click("1446763406004.png")
            wait(3600)
