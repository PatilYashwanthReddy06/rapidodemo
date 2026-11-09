class rapido:
    customer = "passenger"
    city = "Banglore"
   
    def __init__(self,passengername,mobile_no,vehicle_type,company):
        self.passengername = passengername
        self.mobile_no = mobile_no
        self.vehicle_type = vehicle_type
        self.company = company     
rapido.founder = "ABC"

r1 = rapido("yashwanth", 351522581,"car","vw")
print(r1.__dict__)
r2 = rapido("Rohit", 35152225,"car","nissan")
print(r2.__dict__)