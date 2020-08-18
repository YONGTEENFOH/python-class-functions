from guitar import guitar

guitar1 = guitar("yamaha", 350, "good")
guitar2 = guitar("ibanez", 150, "bad")
guitar3 = guitar("gibson", 200, "good")

print(guitar3.less_than_RM200_and_good())