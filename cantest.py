from Tkinter import * #GUI library
import tkFont #makes every thing look nice suplys diffrent fonts and such
import sqlite3 #i use this to hold all of the data for the events
import datetime #what do you think
import unidecode #GRRRRRRRRRR

#Giovanni Rescigno : LAB-progaming/clone computers
#date started: 6/20/13
#License: GPL 2.0 (complty open!!!!! have fun)



class mainGui: #the class containg the Gui and handlers

	def __init__(self, master):

		self.app = Frame(master)
		self.app.pack(side = TOP, fill=X)

		self.ListFrame = Frame(self.app, width=200)
		self.ListFrame.pack(side = LEFT, fill=Y)

		self.infoFrame = Frame(self.app, width = 350)
		self.infoFrame.pack(side = LEFT, fill=Y)

		self.listofdata(self.ListFrame) #fuction that handles the data
		self.viewerEvent(self.infoFrame) #fuction that handles the data being displayed

		for self.dataoflist in SQLdata.getDataFromSQLITE():

			self.data.insert(END, " " + self.dataoflist[0])


	def listofdata(self, master):

		self.listboxholder = Frame(master)
		self.listboxholder.grid(row = 0, column = 0, padx=5)

		self.data = Listbox(self.listboxholder, height = 25, width = 25)
		self.data.pack(side = LEFT, fill = Y)

		self.scroller = Scrollbar(self.listboxholder)
		self.scroller.pack(side = LEFT, fill = Y)		

		self.data.configure(yscrollcommand = self.scroller.set)
		self.scroller.configure(command = self.data.yview)

		self.data.bind('<<ListboxSelect>>', self.listhandler)

		self.buttonBox = Frame(master)
		self.buttonBox.grid(row = 1, column = 0, sticky = W)

		self.addNewEvent = Button(self.buttonBox, text = "+")
		self.addNewEvent.pack(side=LEFT, padx = 2)

		self.distroyEvent = Button(self.buttonBox, text = "-")
		self.distroyEvent.pack(side=LEFT)

	def viewerEvent(self, master):

		self.titleFont = tkFont.Font(family="Helvetica", weight="bold", size=20)# declaration of fonts up here
		self.subtitle = tkFont.Font(family="Helvetica", weight="bold", size=14)
		self.bodyFont = tkFont.Font(family="Helvetica", weight="normal", size=14)

		self.topFrame = Frame(master)
		self.topFrame.pack(side = TOP, fill = X, padx = 5, pady = 5)


		self.EventName = StringVar()# var holding the Name of the event 
		self.titleLabel = Label(self.topFrame, font=self.titleFont, textvariable=self.EventName)
		self.titleLabel.pack(side = LEFT)

		self.CheckVar1 = IntVar()#holds the state of the check box
		self.finnished = Checkbutton(self.topFrame, text = "Done", variable = self.CheckVar1, 
			onvalue = 1, offvalue = 0)
		self.finnished.pack(side = RIGHT)

		self.hr = Frame(master, bg = "black", height = 2, width = 350)
		self.hr.pack(fill = X, padx = 3) 


		self.dateframe = Frame(master)
		self.dateframe.pack(fill=X, padx = 5, pady = 10)

		self.dateLabel = Label(self.dateframe, text = "Date: ", font = self.subtitle)
		self.dateLabel.pack(side = LEFT)

		self.dateOfEvent = StringVar()#var holding the date
		self.datedata = Label(self.dateframe, textvariable = self.dateOfEvent, font = self.bodyFont)
		self.datedata.pack(side = LEFT, padx = 10)


		self.timedata = Frame(master)
		self.timedata.pack(fill = X, padx = 5, pady = 10)

		self.timeLabel = Label(self.timedata, text = "Time: ", font = self.subtitle)
		self.timeLabel.pack(side = LEFT)

		self.startTimeData = StringVar() #var holding the time an event starts
		self.startTime = Label(self.timedata, textvariable = self.startTimeData, font = self.bodyFont)
		self.startTime.pack(side = LEFT, padx = 10)

		self.endTimeData = StringVar() #var holding the time that event ends
		self.endTime = Label(self.timedata, textvariable = self.endTimeData, font = self.bodyFont)
		self.endTime.pack(side = LEFT, padx = 10)


		self.localdata = Frame(master)
		self.localdata.pack(fill = X, padx = 5, pady = 10)

		self.localLabel = Label(self.localdata, text = "Location:", font = self.subtitle)
		self.localLabel.pack(side = LEFT)

		self.location = StringVar() #holds the location of the event (if any)
		self.locationData = Label(self.localdata, textvariable = self.location)
		self.locationData.pack(side = LEFT, padx = 5)


		self.buttonboxinfo = Frame(master)
		self.buttonboxinfo.pack(side=BOTTOM, fill = X)

		self.editButton = Button(self.buttonboxinfo, text = "Edit")
		self.editButton.pack(side = RIGHT)

	##############handlers##############

	def listhandler(self, event):

		self.lisboxliss = event.widget #find the index of that list box
		self.index = int(self.lisboxliss.curselection()[0])
		#print self.index

		self.listEvent = SQLdata.getDataFromSQLITE()[self.index]

		self.EventName.set(self.listEvent[0])#gets the event name form the data base
		self.dateOfEvent.set(self.listEvent[2])#gets the dat
		self.startTimeData.set(timeing.convertToTime(self.listEvent[3])) #gets the start time and runs it though the time code
		self.endTimeData.set(timeing.convertToTime(self.listEvent[4])) #gets the end time and same
		self.location.set(self.listEvent[1])#gets the location of the event (you guessed it) from the data base

class DataReadRight:

	def __init__(self):

		self.openDatabase()
		
	def getDataFromSQLITE(self):

		self.listofdata = []
		for self.rowData in self.EventData.execute("SELECT * FROM events"):
			self.indexedrange = len(self.rowData)
			self.smallerlist = []

			for self.indexofDB in range(self.indexedrange):
				self.smallerlist = self.smallerlist + [self.rowData[self.indexofDB]]
	
			self.listofdata = self.listofdata + [self.smallerlist]

		return timeing.rankData(self.listofdata, 21)

	def openDatabase(self):

		self.EventData = sqlite3.connect('events.db')#connects to the db file giveing me the ablity to save and request data
		self.selecter = self.EventData.cursor()#alows me to qeary the data in the .db file
		
class timeing:

	def convertToTime(self, oldtime): #converts 24 hour time to 12 hour time with AM or PM

		if ((oldtime - int(oldtime)) != 0):
			self.minets = int((oldtime - int(oldtime)) *100)
			if (self.minets < 0.10):
				self.minets = "0" + str(self.minets)
			else:
				self.minets = str(self.minets)
		elif ((oldtime - int(oldtime)) == 0):
			self.minets = "00"

		self.hours = str(int(oldtime))

		if (int(self.hours) < 12 and int(self.hours) != (12 or 24)):
			self.hours = str(int(oldtime))
			self.fulltime = self.hours + ":" + self.minets + 'am'
		elif (int(self.hours) > 12 and int(self.hours) != (12 or 24)):
			self.hours = str(int(self.hours) - 12)
			self.fulltime = self.hours + ":" + self.minets + 'pm'
		elif (int(self.hours) == 12):
			self.fulltime = self.hours + ":" + self.minets + "pm"
		elif (int(self.hours) == 24):
			self.fulltime = str(int(self.hours) - 12) + ":" + self.minets + 'am'

		return self.fulltime

	def rankData(self, listOfEvents, timeAlocated):

		self.rankedlist = sorted(listOfEvents, key = lambda event: event[5])#sorts the events by their 'rank'
		self.rankedlist.reverse()#cnages the list form smallest to largest to largest to smallest 'rank'

		self.amountOfTime = []#list the corestponds to the list of events but holds the time that is alocated to each event

		for i in range(len(self.rankedlist)): #finds the time that is alocated to each event
			self.amountOfTime = self.amountOfTime + [self.rankedlist[i][4] - self.rankedlist[i][3]]

		self.startTimeOfEvent = 10
		self.DayTimeStorage = timeAlocated
		self.counter = 0
		self.daysInFuture = 0


		for self.counter in range(len(self.rankedlist)):
			self.fulltime = 10

			for i in range(self.counter+1):
				self.fulltime = self.fulltime + self.amountOfTime[i]

			if not(self.fulltime <= self.DayTimeStorage):
				self.DayTimeStorage = self.DayTimeStorage + timeAlocated
				self.startTimeOfEvent = 10
				self.daysInFuture = self.daysInFuture + 1

			#if self.fulltime <= self.DayTimeStorage:
			self.rankedlist[self.counter][3] = self.startTimeOfEvent
			self.rankedlist[self.counter][4] = self.startTimeOfEvent + self.amountOfTime[self.counter]
			self.startTimeOfEvent = self.rankedlist[self.counter][4]
			self.rankedlist[self.counter][2] = self.dateInDays(self.daysInFuture)
			self.counter = self.counter + 1

			

		return self.rankedlist

	def dateInDays(self, days):

		#self.rawymd = str(time.strftime("%Y%m%d"))
		#self.dateList = [self.rawymd[0:3], self.rawymd[4:6], self.rawymd[7:]]

		return str(datetime.date.today() + datetime.timedelta(days=days))



		
root = Tk()#Tk (GUI library) Object is created 
root.title("clone planer") # title is made for the Tk Object
root.geometry("550x455") #the size is created

#other objects are created

timeing = timeing()
SQLdata = DataReadRight()
Gui = mainGui(root)


root.mainloop()#run the GUI in a loop