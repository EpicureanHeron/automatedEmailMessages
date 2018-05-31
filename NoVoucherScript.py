PONumber = raw_input("PO Number: ")

receipt = raw_input("Receipt Number: ")

receiptDate = raw_input("Receipt Date: ")

supplierName = raw_input("supplier name: ")

preparersFirstName = raw_input("Preparer's first Name: ")

preparersLastName = raw_input("Preparer's Last Name: ")


message = "Hello, Supplier " + supplierName + " reached out to the EFS helpline today concerning payment from PO " + PONumber + ". The PO sourced from a req created by " + preparersFirstName + " " + preparersLastName + " like the PO has been received against by " + preparersFirstName + " via receipt " + receipt + " on " +  receiptDate + ". However, not voucher exists on the system. not voucher exists on the system. If you have the invoice still, please send it to your cluster for imaging. Otherwise, if you need the invoice, I have CC'd the supplier on this email so they should be able to facilitate this. Let us know if we can be of any help, "


print message