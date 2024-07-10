 # Virtual Private Cloud (VPC) with both public and private subnets,Implement routing,   security groups, and network access control lists (NACLs)


 ### Create a VPC

 A virtual private cloud (VPC) is a secure, isolated private cloud hosted within a public cloud.

 ##### Advantages of using a VPC

 * Scalability 
 * Better performance
 * Better Security


##### Process

On the VPC Dashboard in the AWS Management Console, I Clicked on VPCs in the left navigation pane,Clicked Create VPC and entered the following details:
* Name tag: KCVPC
* IPv4 CIDR block: 10.0.0.0/16
Left other settings as default and Clicked on Create VPC.

 ![VPC]('/Assignment/KodeCamptask5/VPCImg/VPC.png')


 ### Create Subnets

 A subnet is a network within a network. It is a division of network into two or more networks. It's purpose is to improve network performance and security by dividing a network into smaller parts.

 ##### Process

On the VPC Dashboard, I Clicked on Subnets in the left navigation pane,Clicked Create subnet and entered the following details:
* Name tag: PublicSubnet
* VPC: KCVPC
* Availability Zone: eu-west-1a
* IPv4 CIDR block: 10.0.1.0/24


* Name tag: PrivateSubnet
* VPC: KCVPC
* Availability Zone: eu-west-1a
* IPv4 CIDR block: 10.0.2.0/24
Clicked Create subnet.

 ![createsubnets]('/Assignment/KodeCamptask5/VPCImg/createSubnets.png')

 ![subnets]('/Assignment/KodeCamptask5/VPCImg/pubAndPriSubnet.png')



 ### Configure an Internet Gateway (IGW)

 An internet gateway is a VPC component that allows communication between the VPC and the internet. It enables resources in the public subnets (such as EC2 instances) to connect to the internet if the resource has a public IPv4 address or an IPv6 address.

 ##### process


On the VPC Dashboard, I clicked on Internet Gateways in the left navigation pane,Clicked Create internet gateway and entered the following details:
* Name tag: KCVPC-IGW and Clicked Create internet gateway.

![IGWcreated]('/Assignment/KodeCamptask5/VPCImg/IGWCreated.png')

Selected the newly created IGW and click Actions -> Attach to VPC and Selected KCVPC and click Attach internet gateway.

 ![IGWAttached]('/Assignment/KodeCamptask5/VPCImg/IGWAttached.png')


 ### Configure Route Tables

 A route table contains a set of rules, called routes, that determine where network traffic from subnet or gateway is directed.The main purpose of a routing table is to help routers make effective routing decisions.

 #### PublicRouteTable

 ##### process

 On the VPC Dashboard, I clicked on Route Tables in the left navigation pane,Clicked Create route table and entered the following details:
* Name tag: PublicRouteTable
* VPC: KCVPC
Clicked Create route table.
Selected the newly created route table, clicked on the Routes tab, and then click Edit routes,Clicked Add route, and entered the following details:
* Destination: 0.0.0.0/0
* Target: Select the Internet Gateway (KCVPC-IGW)
Clicked Save routes,Clicked on the Subnet associations tab, and then click Edit subnet associations, Selected PublicSubnet and click Save associations.

 ![PublicRouteTable]('/Assignment/KodeCamptask5/VPCImg/pubRouteTab.png')

 ![SubAssPublicRouteTable]('/Assignment/KodeCamptask5/VPCImg/subasspubroutetab.png')

 ![updatedIGWPublicrouteTable]('/Assignment/KodeCamptask5/VPCImg/updatedIGWPubroutetable.png')

#### PrivateRouteTable

 ##### process

 Clicked Create route table again and entered the following details:
* Name tag: PrivateRouteTable
* VPC: KCVPC
Clicked Create route table,Clicked on the Subnet associations tab, and then click Edit subnet associations,Selected PrivateSubnet and click Save associations.

 ![PrivateRouteTable]('/Assignment/KodeCamptask5/VPCImg/priRouteTab.png')

 ![SubAssPrivatRouteTable]('/Assignment/KodeCamptask5/VPCImg/subassprivroutetab.png')


 ### Configure NAT Gateway

 A NAT gateway is a Network Address Translation (NAT) service.  NAT gateway is used so that instances in a private subnet can connect to services outside VPC but external services cannot initiate a connection with those instances.

 ##### Process

 On the VPC Dashboard,I clicked on NAT Gateways in the left navigation pane,Clicked Create NAT gateway and entered the following details:
* Subnet: Select PublicSubnet
* Elastic IP allocation ID: Click Allocate Elastic IP and then Allocate.
Clicked Create NAT gateway and Wait for the NAT Gateway to become available,went back to Route Tables, selected PrivateRouteTable, and clicked on the Routes tab, then Edit routes.
Clicked Add route, and entered the following details:
* Destination: 0.0.0.0/0
* Target: Select the NAT Gateway created earlier.
Clicked Save routes.

 ![NATGW]('/Assignment/KodeCamptask5/VPCImg/NatGW.png')

 ![PrivateRouteTableWithNATGW]('/Assignment//KodeCamptask5/VPCImg/priRouteTabwithNATGW.png')



### Security Groups

security group acts as a virtual firewall for EC2 instances to control incoming and outgoing traffic,operate at the instance level and are stateful. Both inbound and outbound rules control the flow of traffic to and traffic from instance, respectively thereby enhancing network security and access control.

#### Security Group for public instances
 
 ##### process

 In the VPC Dashboard,I clicked on Security Groups in the left navigation pane, clicked Create security group and entered the following details:
* Name tag: PublicSG
* VPC: KCVPC
Clicked Create security group, Selected the newly created security group, clicked on the Inbound rules tab, and then click Edit inbound rules and added the following rules:HTTP HTTPS from anywhere and SSH from my local IP, Clicked Save rules and Clicked on the Outbound rules tab, and ensured All traffic is allowed.

 ![PublicSG]('/Assignment/KodeCamptask5/VPCImg/publicSG.png')

 #### Security Group for private instances

 ##### process

 In the VPC Dashboard, I clicked on Security Groups in the left navigation pane, clicked Create security group and entered the following details:
* Name tag: PrivateSG
* VPC: KCVPC
Clicked Create security group, Selected the newly created security group, clicked on the Inbound rules tab, and then click Edit inbound rules and added the following rules:HTTP HTTPS, SSH from  PublicSubnet CIDR block (10.0.1.0/24), Clicked Save rules and Clicked on the Outbound rules tab, and ensured All traffic is allowed.

 ![PrivateSG]('/Assignment/KodeCamptask5/VPCImg/privateSG.png')


 ### Network ACLs

 Network Access Control Lists define inbound and outbound rule for subnets present in VPC, operate at the subnet level and are stateless



![PublicSubnetNACL]('/Assignment/KodeCamptask5/VPCImg/pubSNACL.png')

![PublicSubnetNACL]('/Assignment/KodeCamptask5/VPCImg/')

 #### Public Subnet NACL

 ##### process

 In the VPC Dashboard,I clicked on Network ACLs in the left navigation pane, clicked Create Network ACLs and entered the following details:
* Name tag: PublicSubnetNACL
* subnet Association: PublicSubnet
Clicked Create Network ACLs, Selected the newly created Network ACLs, clicked on the Inbound rules tab, and then click Edit inbound rules and added the following rules:HTTP HTTPS from anywhere and SSH from my local IP, Clicked Save rules and Clicked on the Outbound rules tab, and ensured All traffic is allowed.

![InboundPublicSubnetNACL]('/Assignment/KodeCamptask5/VPCImg/inboundPubSNACL.png')

![OutboundPublicSubnetNACL]('/Assignment/KodeCamptask5/VPCImg/outboundPubSNACL.png')

#### Private Subnet NACL

##### process

 As Above:
* Name tag: PrivateSubnetNACL
* subnet Association: PrivateSubnet
Clicked Create Network ACLs, Selected the newly created Network ACLs, clicked on the Inbound rules tab, and then click Edit inbound rules and added the following rules:HTTP HTTPS, SSH from  PublicSubnet CIDR block (10.0.1.0/24), Clicked Save rules and Clicked on the Outbound rules tab, and ensured All traffic is allowed from PublicSubnet CIDR block (10.0.1.0/24) and internet.

![InboundPrivateSubnetNACL]('/Assignment/KodeCamptask5/VPCImg/inboundPriSNACL.png')

![outboundPrivateSubnetNACL]('/Assignment/KodeCamptask5/VPCImg/outboundPriSNACL.png')


### Deploy Instances

##### Proess

In the AWS Management Console, went to the EC2 Dashboard,Clicked Launch Instance and entered the following details:
* Name: FEServer and BEServer
* AMI:Ubuntu
* keyPair:kc-sshkey
* Clicked on edit network and entered the following:
     * VPC: Selected KCVPC
     * Subnet:PublicSubnet and PrivateSubnet respectively 
* Clicked on launch Instance

![keypair]('/Assignment/KodeCamptask5/VPCImg/keyPair.png')

#### FrontEnd Instance

![LaunchFEInstance]('/Assignment/KodeCamptask5/VPCImg/FEInstance.png')

![FEServer]('/Assignment/KodeCamptask5/VPCImg/FEServer.png')

![ConnectedServer]('/Assignment/KodeCamptask5/VPCImg/launchedFEServer.png')

#### BackEnd Instance

![LaunchBEInstance]('/Assignment/KodeCamptask5/VPCImg/BEInstance.png')

![BEServer]('/Assignment/KodeCamptask5/VPCImg/BEServer.png')


### Diagram of the VPC architecture

![VPCDiagram]('/Assignment/KodeCamptask5/VPCImg/VPCArch.png')