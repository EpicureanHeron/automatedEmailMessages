name = raw_input("Please name the file this will be output to: ")

fileName = name + ".txt"

file_1= open(fileName, "w")

voucherOrReceipt = raw_input("Is the PO missing a voucher[1] or receipt[2]? Please enter 1 or 2:  ")


def whichToRun():
	global voucherOrReceipt
	print voucherOrReceipt
	if voucherOrReceipt == "1":
		noVoucher()
	
	elif voucherOrReceipt == "2":
		noReceipt()
	
	else:
		print "run this again, you chose wrong"

def noVoucher(): 

	firstLine = "Hello," + "\n"

	PONumber = raw_input("PO Number: ")

	supplierName = raw_input("supplier name: ")

	preparersFirstName = raw_input("Preparer's first Name: ")

	preparersLastName = raw_input("Preparer's Last Name: ")
	
	receipt = raw_input("Receipt Number: ")

	receiptDate = raw_input("Receipt Date: ")

	message = "Supplier " + supplierName + " reached out to the EFS helpline today concerning payment from PO " + PONumber + ". The PO sourced from a req created by " + preparersFirstName + " " + preparersLastName + ". It looks like the PO has been received against by " + preparersFirstName + " via receipt " + receipt + " on " +  receiptDate + ". However, not voucher exists on the system. not voucher exists on the system. If you have the invoice still, please send it to your cluster for imaging. Otherwise, if you need the invoice, I have CC'd the supplier on this email so they should be able to facilitate this. Let us know if we can be of any help, "


	file_1.write(firstLine + message)
	
	print "Success!"

def noReceipt():

	firstLine = "Hello," + "\n"

	PONumber = raw_input("PO Number: ")

	supplierName = raw_input("supplier name: ")

	preparersFirstName = raw_input("Preparer's first Name: ")

	preparersLastName = raw_input("Preparer's Last Name: ")
	 
	voucher = raw_input("voucher number: ")
	
	message = "Supplier " + supplierName + " reached out to the EFS helpline today concerning payment from PO " + PONumber + "The PO sourced from a req created by " + preparersFirstName + " " + preparersLastName + "There is a voucher created against this PO, voucher " + voucher + ". However, no receipt has been created against the PO."+ preparersFirstName + ", please go in and receive against the PO. Once a receipt has been created, the system will match the voucher and a payment should go out. If you need an invoice, I recommend you reach out the supplier who I have CC'd to this email. Otherwise, if you have questions or concerns about the receiving process, please let me know. Have a great day."
	
	file_1.write(firstLine + message)
	
	print "Success!"

whichToRun()
