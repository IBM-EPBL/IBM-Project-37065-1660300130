import requests ,json

pnr_no = "4465877280"


a = "https://indianrailapi.com/api/v2/PNRCheck/apikey/375b8caa6a27e3d1b9922c851245c93f/PNRNumber/"+ pnr_no + "/"

dk = requests.get(a)
result = dk.json()

if result["ResponseCode"] == '200': 

	pnr_number = result['PnrNumber']
	train_name = result["TrainNumber"] 
	Journey_class = result["JourneyClass"] 
	Chat_Prepared = result["ChatPrepared"] 
	from_station = result["From"] 
	to_station = result["To"]
	dateof_journey = result["JourneyDate"]
	passengers_list = result["Passangers"] 

	print(f"PnrNumber {pnr_number}\nTrain Name {train_name}\nJourney Class {Journey_class}\nChart Preadared {Chat_Prepared}\nFrom Station {from_station} To {to_station}\nJourney Date {dateof_journey}")

	for passenger in passengers_list: 

		passenger_num = passenger["Passenger"]

		current_status = passenger["CurrentStatus"] 

		booking_status = passenger["BookingStatus"] 

		print(" passenger number : " + str(passenger_num) 
			 + "\n current status : " + str(current_status) 
			+ "\n booking_status : " + str(booking_status)) 
  
else:	
	print("Wrong Pnr Number")	
