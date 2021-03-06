import datetime

def whichToRun():
	# prompts the user for what type of email message this is 
	voucherOrReceipt = raw_input("Is the PO missing a voucher[1], receipt[2], or no receipt AND no voucher [3]? Please enter 1, 2, or 3:  ")
	
	# checks the value, and runs the necessary function to generate the message
	if voucherOrReceipt == "1":
		noVoucher()
	
	elif voucherOrReceipt == "2":
		noReceipt()
	#if neither 1 or 2 is passed, then exits the program with this message

	elif voucherOrReceipt == "3":
		noReceiptOrVoucher()
	else:
		print "Run this file again, you chose wrong! Either enter 1, 2, or 3."
				
def noVoucher(): 
	
	#first line plus formatting
	firstLine = "Hello," + "\n" + "\n"
	
	#prompts the user for inputs
	PONumber = raw_input("PO Number: ")

	supplierName = raw_input("Supplier Name: ")

	preparersFirstName = raw_input("Preparer's first name: ")

	preparersLastName = raw_input("Preparer's last name: ")
	
	receipt = raw_input("Receipt Number: ")

	receiptDate = raw_input("Receipt Date: ")
	
	#gets the date 
	date = str(datetime.datetime.now().date())
	
	#sets the path of the file in the outputFiles folder and adds the appropriate suffix
	fileName = "outputFiles/" +  preparersLastName +  date + "-novoucher" +  ".txt"
	
	#opens a file on the specified path with the name
	file_1= open(fileName, "w")


	#creates the message with the user's inputs
	message = "Supplier " + supplierName + " reached out to the EFS helpline today concerning payment from PO " + PONumber + ". The PO sourced from a req created by " + preparersFirstName + " " + preparersLastName + ". It looks like the PO has been received against by " + preparersFirstName + " via receipt " + receipt + " on " +  receiptDate + ". " + "\n" + "\n" + "However, no voucher exists on the system as of yet. If you have the invoice still, please send it to your cluster for imaging. Otherwise, if you need the invoice, I have CC'd the supplier on this email so they should be able to facilitate this. Let us know if we can be of any help, "

	#writes the message to the folder 
	file_1.write(firstLine + message)
	
	#closes the folder
	file_1.close
	
	#lets the caller know where the file is ready
	print "Success! Your file is ready! Just follow the path: " + fileName 

def noReceipt():

	
	firstLine = "Hello," + "\n" + "\n"

	PONumber = raw_input("PO Number: ")

	supplierName = raw_input("Supplier Name: ")

	preparersFirstName = raw_input("Preparer's first name: ")

	preparersLastName = raw_input("Preparer's last name: ")
	 
	voucher = raw_input("Voucher Number: ")
	
	message = "Supplier " + supplierName + " reached out to the EFS helpline today concerning payment from PO " + PONumber + ". The PO sourced from a req created by " + preparersFirstName + " " + preparersLastName + ". There is a voucher created against this PO, voucher " + voucher + "." + "\n" + "\n" + "However, no receipt has been created against the PO. "+ preparersFirstName + ", please go in and receive against the PO. Once a receipt has been created, the system will match the voucher and a payment should go out. If you need an invoice, I recommend you reach out the supplier who is  CC'd in this email. Otherwise, if you have questions or concerns about the receiving process, please let us  know. Have a great day."
	
	date = str(datetime.datetime.now().date())

	fileName = "outputFiles/" +  preparersLastName +  date +  "-noReceipt" ".txt"

	file_1= open(fileName, "w")
	
	file_1.write(firstLine + message)
	
	file_1.close()
	
	print "Success! Your file is ready! Just follow the path: " + fileName 

def noReceiptOrVoucher():

	
	firstLine = "Hello," + "\n" + "\n"

	PONumber = raw_input("PO Number: ")

	supplierName = raw_input("Supplier Name: ")

	preparersFirstName = raw_input("Preparer's first name: ")

	preparersLastName = raw_input("Preparer's last name: ")
	
	message = "A representative from supplier " + supplierName + " contacted the University Financial Helpline inquiring about payment from PO " + PONumber + "." + "\n" + "\n" + "PO " + PONumber +" was created from a requisition that " + preparersFirstName + " " + preparersLastName + " created. There has been no receipt or voucher against this PO yet." + "\n" + "\n" + "I have CC'd the supplier on this email. " + preparersFirstName + ", if you have received the items, but have not created a receipt in EFS yet, please go ahead and do so. Then send the invoice to your cluster for imaging. If you need either the invoice or have a problem with the order, please reach out the supplier." + "\n" + "\n" + "Let us know if our helpline can assist in anyway."
	
	date = str(datetime.datetime.now().date())

	fileName = "outputFiles/" +  preparersLastName + date + "-noReceiptNovoucher" ".txt"

	file_1= open(fileName, "w")

	file_1.write(firstLine + message)
	file_1.close()
	
	print "Success! Your file is ready! Just follow the path: " + fileName

whichToRun()