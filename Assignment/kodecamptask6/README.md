# Virtual Private Cloud (VPC) with both public and private subnets,Implement routing, security groups,network access control lists (NACLs),script to install Nginx and script to install PostgreSQL using Terraform

## Terraform

Terraform is an infrastructure as code (IaC) software tool that allows DevOps teams to automate infrastructure provisioning using reusable, shareable, human-readable configuration files. The tool can automate infrastructure provisioning in both on-premises and cloud environments

### Process

Created a directory. Inside this directory(Root), I created the following configuration files.

- Main Configuration File (main.tf): Define the Provider and its associated resources(modules).[main.tf](main.tf)

- Variables File (variables.tf): Define variables for configuration.[variables.tf](variables.tf)

- Outputs File (outputs.tf): Define outputs to get the details of the created resources.[output.tf](output.tf)

### modules

Created a modules directory which house VPC and EC2 directories and created configuration files(main.tf,variables.tf,outputs.tf) in each of the directories

#### VPC

- main.tf: Define the VPC and its associated resources.[main.tf](modules/vpc/main.tf)

- variables.tf: Define variables for VPC configuration.[variables.tf](modules/vpc/variables.tf)

- outputs.tf: Define outputs to get the details of the created resources.[output.tf](modules/vpc/output.tf)

#### EC2

- main.tf: Define the EC2 [main.tf](modules/ec2/main.tf)

- variables.tf: Define variables for EC2 configuration.[variables.tf](modules/ec2/variables.tf)

- outputs.tf: Define outputs to get the details of the created resources.[output.tf](modules/ec2/output.tf)

### Script to install Nginx

NGINX is open-source web server software used for reverse proxy, load balancing, and caching.[Nginx](scripts/install_nginx.sh)

### Script to install PostgreSQL

PostgreSQL is an object-relational database management system (ORDMBS), which means that it has relational capabilities and an object-oriented design.[PostgreSQL](scripts/install_postgresql.sh)

### Terraform init

Terraform init command initializes a working directory and downloads the necessary provider plugins and modules and setting up the backend for storing infrastructure's state.

Initialize the configuration with command "terraform init" in the directory to initialize the configuration.

![terraformInit](Img/terraforminit.png)

### Terraform plan

Terraform plan command creates a plan consisting of a set of changes that will make the resources match your configuration. This allows to preview the actions Terraform would take to modify infrastructure before applying them.

Create an execution plan with command "terraform plan -out tfplan.txt" to create the executionplan and save the output

![terraformPlan](Img/tfplan1.png)

![terraformPlan](Img/tfplan2.png)

![terraformPlan](Img/tfolan8.png)

![terraformPlan](Img/tfplan8.png)

### Terraform apply

The terraform apply command executes planned actions, creating, updating, or deleting infrastructure resources to match the new state outlined in the IaC.

Apply the changes with command "terraform apply" to create the VPC and associated resources and EC2

![terraformapply](Img/tfapply1.png)

![terraformapply](Img/tfapplybtw.png)

![terraformapply](Img/tfapply2.png)

## Output

### Create a VPC

![VPC](Img/VPC.png)

### Create Subnets

![subnets](Img/subnets.png)

#### Public Subnet

![publicSubnet](Img/publicSubnet.png)

#### Private Subnet

![privateSubnet](Img/privateSubnet.png)

### Configure an Internet Gateway (IGW)

![IGWcreated](Img/IGW.png)

![IGWAttached](Img/IGWAttach.png)

### Configure Route Tables

![RouteTable](Img/routeTable.png)

#### PublicRouteTable with Subnet association and Internet Gateway

![PublicRouteTable](Img/publicRT.png)

#### PrivateRouteTable with Subnet association

![PrivateRouteTable](Img/privateRT.png)

### Configure NAT Gateway

![NATGW](Img/NATGW.png)

### Security Groups

![PublicSG](Img/pubicSG.png)

#### Security Group for private instances

![PrivateSG](Img/privateSG.png)

### Network ACLs

![NACL](Img/NACL.png)

#### Public Subnet NACL

![PublicSubnetNACL](Img/PublicNACL.png)

#### Private Subnet NACL

##### process

![PrivateSubnetNACL](Img/privateNACL.png)

### Deploy Instances

![Instance](Img/instance.png)

#### FrontEnd Instance

![FEServer](Img/publicServer.png)

![ConnectedServer](Img/tfserver.png)

#### BackEnd Instance

![BEServer](Img/privateServer.png)

### Terraform destroy

Clean up resources with command terraform destroy to delete all the resources

![terraformdestroy](Img/tfdestroy1.png)

![terraformdestroy](Img/tfdestroy2.png)

![terraformdestroy](Img/tfdestroy3.png)

### Output

![IntanceTerminated](Img/instanceTerminated.png)

![VPCTerminated](Img/vpcTerminated.png)
