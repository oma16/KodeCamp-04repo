command1 = ["vagrant", "init", "ubuntu/focal64"]
command2 = ["vagrant", "up"]
command = ["vagrant", "ssh"]

dirPath = "/home/oma16/KodeCamp-04repo/Assignment/kodecampstorestask4"

users_and_groups = [
    ('Andrew', 'System_Administrator'),
    ('Julius', 'Legal'),
    ('Chizi', 'Human_Resource_Manager'),
    ('Jeniffer', 'Sales_Manager'),
    ('Adeola', 'Business_Strategist'),
    ('Bach', 'CEO'),
    ('Gozie', 'IT_intern'),
    ('Ogochukwu', 'Finance_Manager')
]

# List of directories to be created
directories = [
    'Finance_Budgets',
    'Contract_Documents',
    'Business_Projections',
    'Business_Models',
    'Employee_Data',
    'Company_Vision_and_Mission_Statement',
    'Server_Configuration_Script'
]