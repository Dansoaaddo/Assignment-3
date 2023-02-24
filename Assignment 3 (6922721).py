# List cars available and their prices 
cars ={"Chevrolet":30000,
"Mercedes-Benz":65000,
"Ford":50000,
"Lamborghini":65000,
"Tesla":80000,
"Jeep":20000,
"Cadilla":185000,
"Hyundai":92000,
"Alfa Romeo":24500,
"Nissan":60500,
"Maserati":46700,
"BMW":30000,
"Audi":21300,
"Volkswagen":90000,
"Kantanka":54000,
"Kia":35000,
"Peugeot":45000,
"Ferrari":123000,
"Volvo":80000,
"Honda":78000,
"Opel":45000,
"Suzuki":345000,
"Bentley":65000,
"Chyrsler":34000,
"Rolls Royce":430000,
"Mistubishi":650000,
"Jaguar":54000,
"Mini cooper":52000,
"Lexus":43000,
"Subaru":74400}
# get user to input car name
carName=input("What car brand are you looking to purchase?  ")
if carName in cars:
    print("Yes, it is available")
    carPrice=cars[carName]
    print("The price is ${}".format(carPrice))
else:
    print("Sorry, we do not have it at the moment")


