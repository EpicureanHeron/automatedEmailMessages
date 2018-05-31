name = raw_input("Please name the file this will be output to: ")

fileName = name + ".txt"

file_1= open(fileName, "w")

voucherOrReceipt = raw_input("Is the PO missing a voucher or receipt: ")

def noVoucher (): 

	PONumber = raw_input("PO Number: ")

	receipt = raw_input("Receipt Number: ")

	receiptDate = raw_input("Receipt Date: ")

	supplierName = raw_input("supplier name: ")

	preparersFirstName = raw_input("Preparer's first Name: ")

	preparersLastName = raw_input("Preparer's Last Name: ")
	
	firstLine = "Hello," + "\n"


	message = "Supplier " + supplierName + " reached out to the EFS helpline today concerning payment from PO " + PONumber + ". The PO sourced from a req created by " + preparersFirstName + " " + preparersLastName + " like the PO has been received against by " + preparersFirstName + " via receipt " + receipt + " on " +  receiptDate + ". However, not voucher exists on the system. not voucher exists on the system. If you have the invoice still, please send it to your cluster for imaging. Otherwise, if you need the invoice, I have CC'd the supplier on this email so they should be able to facilitate this. Let us know if we can be of any help, "


	file_1.write(firstLine + message)

def noReceipt:

	
	
def whichToRun():
	
	if voucherOrReceipt === "voucher":
		noVoucher()
	
	elif voucherOrReceipt === "receipt":

		noReceipt()
	
	else:
		voucherOrReceipt = raw_input("")
		whichToRun()