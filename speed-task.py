speed_driver = float(input("Please enter your speed"))
average_speed = float(input("Please enter the average speed"))
points = (speed_driver - average_speed) / 5


if speed_driver < 60:
    print("Ok")
else:
    print(points)
    if points >= 12:
        print("Its time to go to jail")
