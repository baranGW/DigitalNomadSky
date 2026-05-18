#Parameters to find your VM. 
tenantid = "0907bb1e-21fc-476f-8843-02d09ceb59a7"  # your tenant-id, this is used to find VMs.

#Parameters to upload your VM.
location = "westeurope"  # The VM will be created in this location.
destionationtenantid = "0907bb1e-21fc-476f-8843-02d09ceb59a7" # the VM will be creaed in this tenant
subscription_id = "a9979e3a-54dc-43b9-8334-f70e19842a54" # the VM will be created in this subscription
resource_group = "VirtualMachineTests" # the VM will be created in this resource group. 

storage_account_name = "vmteststoragebaran"   # a temp storage account to upload the disk file. 
container_name = "$logs"  # the temp container name to upload the disk file.  
