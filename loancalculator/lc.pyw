from tkinter import *

class LoanCalculator:

    def __init__(self):
        window =Tk()
        window.title("Loan Calculator")
        window.configure(background="light green")

        #add label
        Label(window, font="Helvetica 12 bold",bg="light green",text="Anual Intrest Rate").grid(row=1,column=1,sticky=W)
        Label(window, font="Helvetica 12 bold",bg="light green",text="Number of Year").grid(row=2,column=1,sticky=W)
        Label(window, font="Helvetica 12 bold",bg="light green",text="Loan Amount").grid(row=3,column=1,sticky=W)
        Label(window, font="Helvetica 12 bold",bg="light green",text="Monthly Payment").grid(row=4,column=1,sticky=W)
        Label(window, font="Helvetica 12 bold",bg="light green",text="Total Payment").grid(row=5,column=1,sticky=W)


        #create object for accepting inputs
        self.annualInterestRateVar = StringVar()
        Entry(window, textvariable=self.annualInterestRateVar,justify=RIGHT).grid(row=1,column=2)

        self.numberofYearsVar = StringVar()
        Entry(window, textvariable=self.numberofYearsVar,justify=RIGHT).grid(row=2,column=2)

        self.loanAmountVar = StringVar()
        Entry(window, textvariable=self.loanAmountVar,justify=RIGHT).grid(row=3,column=2)

        self.monthlyPaymentVar = StringVar()
        lblMonthlyPayment= Label(window, font="Helvetica 12 bold",bg="Light green",textvariable=self.monthlyPaymentVar).grid(row=4,column=2, sticky=E)

        self.totalPaymentVar = StringVar()
        lblTotalPayment= Label(window, font="Helvetica 12 bold",bg="Light green",textvariable=self.totalPaymentVar).grid(row=5,column=2, sticky=E)

        #create a button to compute value and clear input

        btComputePayment=Button(window,text="Compute Payment",bg="red",fg="WHite",font="Helvetica 14 bold", command=self.computePayment).grid(row=6,column=2,padx=10,pady=10,sticky=E)
        btClear=Button(window, text="Clear",bg="blue",fg="White",font="Helvetica 14 bold",command=self.delete_all).grid(row=6,column=3,padx=20,pady=20,sticky=E)

        window.mainloop()
   
    #create method to compute payment and clear screen
    def computePayment(self):
        monthlyPayment=self.getMonthlyPayment(
            float(self.loanAmountVar.get()),
            float(self.annualInterestRateVar.get())/1200,
            int(self.numberofYearsVar.get()))

        self.monthlyPaymentVar.set(format(monthlyPayment,'10.2f'))
        totalPayment=float(self.monthlyPaymentVar.get())*12\
            * int(self.numberofYearsVar.get())

        self.totalPaymentVar.set(format(totalPayment,'10.2f'))

    def getMonthlyPayment(self,loanAmount,monthlyInterestRate,numberofYears):
        monthlyPayment=loanAmount*monthlyInterestRate/(1-1/(1+monthlyInterestRate)**(numberofYears*12))
        return monthlyPayment

    def delete_all(self):
        self.monthlyPaymentVar.set("")
        self.loanAmountVar.set("")
        self.annualInterestRateVar.set("")
        self.numberofYearsVar.set("")
        self.totalPaymentVar.set("")

LoanCalculator()




    




