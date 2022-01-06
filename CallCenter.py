import random
import string


class CallCenterEmployee:
    available = True
    timeInCall = 0
    callDuration = 0

    def assignCall(self, callDuration, greeting):
        if self.available: 
            self.available = False
            self.callDuration = callDuration
            print (greeting)

    def update(self):
        if not self.available:
            self.timeInCall += 1 
            if self.callDuration <= self.timeInCall:
                self.timeInCall = 0
                self.available = True
                print("have a nice day!")




class Operator(CallCenterEmployee):
    def takeCall(self, callDuration):
        super().assignCall(callDuration, "Thank you for calling, this is Fre's minion speaking" )


class Supervisor(CallCenterEmployee):
    def takeCall(self, callDuration):
        super().assignCall(callDuration, "Thank you for calling, this is Fre's boss speaking" )


class Director(CallCenterEmployee):
    def takeCall(self, callDuration):
        super().assignCall(callDuration ,  "Thank you for calling, this is a Fre's God speaking")





class CallCenter:

    def __init__(self, numOperators, numSupervisors, numDirectors):

        self.employees = []

        for i in range(numOperators):
            self.employees.append(Operator())

        for i in range(numSupervisors):
            self.employees.append(Supervisor())

        for i in range(numDirectors):
            self.employees.append(Director())

        print("We are now open to recieve calls!")



    callQueue = []


    def recieveCall(self, duration):
        self.callQueue.append(duration)
    
    def takeCall(self):

        if self.callQueue:
            callDuration = self.callQueue.pop()
            callTaken = False

            for employee in self.employees:
                if employee.available == True:
                    employee.takeCall(callDuration)
                    callTaken = True
                    break
                

            if callTaken == False:
                print("Please hold for the next available representative")
                self.callQueue.insert(0, callDuration)

    
    def healthCheck(self):
        for e in self.employees:
            print(str(e.available) + " "  + str(e.timeInCall) + " " + str(e))
    
    def startWorking(self, Callfrequency, avgCallDuration, endTime):

        time = 0 

        while time < endTime:
            if(time%Callfrequency==0):
                self.recieveCall( avgCallDuration )
                print("recieving call...")
            self.takeCall()
            for e in self.employees:
                e.update()
            time+=1






