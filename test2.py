#print(Responses.bot_res(api_method.flight_price(Responses.code_date(raw_message))))
import Responses
import api_method
message = "I need a flight from ORD to LAX on 07-24"
print(Responses.code_date(message))
info = Responses.code_date(message)
print(info[0])
print(api_method.flight_price(info[0], info[1], info[2]))