import pandas as pd

path_to_file = '/Users/Desktop/mechanical_engineer_LinkedIn_test_scrape.csv'

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 500)
pd.set_option('display.width', 400)
pd.set_option('max_colwidth', 100)

data = pd.read_csv(path_to_file)


data['Job Function'] = data['Job Function'].str.strip()
data['Seniority'] = data['Seniority'].str.strip()
data['Seniority'] = data['Seniority'].replace('Full-time', 'N/A')
data['Employment Type'] = data['Employment Type'].fillna('Full-Time')
data['Job Description'] = data['Job Description'].str.strip().replace(' ', '')
data['Employment Type'] = data['Employment Type'].str.strip().replace('\n', '')
data = data.replace({'Job Title': {'.*Mechanical.*Engineer.*': 'Mechanical Engineer',
                                   '.*Design.*Engineer.*': 'Design Engineer',
                                   '.*Project.*Engineer.*': 'Project Engineer',
                                   '.*Mech.*Design.*Engineer.*': 'Mechanical Design Engineer',
                                   '.*Mech.*Design.*Engr.*': 'Mechanical Design Engineer',
                                   '.*Engineer.*Mechanical.*': 'Mechanical Engineer',
                                   '.*Engineer.*Design.*': 'Design Engineer',
                                   '.*Project.*Engr.*': 'Project Engineer',
                                   '.*Reliability.*Engineer.*': 'Reliability Engineer',
                                   '.*Mech.*Engineer.*': 'Mechanical Engineer',
                                   '.*Piping.*Engineer.*': 'Mechanical Engineer',
                                   '.*Quality.*Engineer.*': 'Quality Engineer',
                                   '.*APC.*Engineer.*': 'APC Engineer',
                                   '.*Electro.*mechanical.*Engineer.*': 'Electro mechanical Engineer',
                                   '.*Lead.*Engineering.*Associate': 'MechanicalEngineer',
                                   '.*Converting.*&.*Assembly.*': 'Assembly Engineer',
                                   '.*CAD.*Drafter.*': 'CAD Drafter',
                                   '.*Patent.*Attorney.*': 'Patent Engineer',
                                   '.*Maintenance.*Manager.*': 'Maintenance Engineer',
                                   '.*Project.*Manager.*Wastewater.*': 'Project Engineer',
                                   '.*Systems.*Engineer.*': 'Systems Engineer',
                                   '.*Electrical.*Engineer.*': 'Electrical Engineer',
                                   '.*Software.*Engineer.*': 'Software Engineer',
                                   '.*Maintenance.*Supervisor.*': 'Maintenance Engineer',
                                   '.*Mine.*Maintenance.*': 'Mechanical Engineer',
                                   '.*Facilities.*Manager.*': 'Facilities Engineer',
                                   '.*Patent.*Analyst.*': 'Patent Engineer',
                                   '.*RCDD.*Technology.*Designer.*': 'Technology Designer',
                                   '.*Controls.*Systems.*Engineer.*': 'Systems Engineer',
                                   '.*Project.*Manager.*': 'Project Engineer',
                                   '.*Software.*Staff.*Engineer': 'Software Engineer',
                                   '.*Regional.*Practice.*Leader.*': 'Mechanical Engineer',
                                   '.*Maintenance.*Engineer.*': 'Maintenance Engineer',
                                   '.*Environmental.*Health.*Safety.*': 'EHS Engineer',
                                   '.*Site.*Manager.*': 'Project Engineer',
                                   '.*Senior.*Distribution.*Engineer.*': 'Distribution Engineer',
                                   '.*Plant.*Operator.*': 'Plant Operator',
                                   '.*SYSTEMS.*ENGINEER.*': 'Systems Engineer',
                                   '.*Integrity.*Engineer.*': 'Integrity Engineer',
                                   '.*Process.*Engineer.*': 'Process Engineer',
                                   '.*PM.*Engineering.*': 'Project Management Engineer',
                                   '.*Procurement.*Engineer.*': 'Procurement Engineer',
                                   '.*design.*engineer.*': 'Design Engineer',
                                   '.*Flight.*Test.*Engineer.*': 'Flight Test Engineer',
                                   '.*Analysis.*Engineer.*': 'Analysis Engineer',
                                   '.*HVAC.*PM.*Mobile.*Engineer': 'Project Engineer',
                                   '.*Engineering.*Liaison.*Truck.*': 'Automotive Engineer',
                                   '.*DC.*PM.*': 'Project Engineer',
                                   '.*Engineering.*Reliability.*Department.*': 'Reliability Engineer',
                                   '.*DESIGN.*ENGINEER.*': 'Design Engineer',
                                   '.*Engineer.*Plant.*Maintenance.*': 'Maintenance Engineer',
                                   '.*Civil.*Engineer.*': 'Civil Engineer',
                                   '.*Computational.*Electromagnetic.*Codes.*': 'CEM Engineer',
                                   '.*Sales.*Engineer.*': 'Sales Engineer',
                                   '.*Engineer.*Project.*Administrator.*': 'Project Engineer',
                                   '.*Engineer.*Civil.*': 'Civil Engineer',
                                   '.*Field.*Engineer.*': 'Field Engineer',
                                   '.*Installations.*System.*Integration.*': 'Systems Engineer',
                                   '.*Project.*Handler': 'Project Engineer',
                                   '.*Chief.*Engineer.*': 'Mechanical Engineer',
                                   '.*ENVIRONMENTAL.*ENGINEERING.*': 'Environmental Engineer',
                                   '.*Automation.*Engineer.*': 'Automation Engineer',
                                   '.*Quality.*Assurance.*': 'Quality Engineer',
                                   '.*Repair.*Development.*Engineer.*': 'Development Engineer',
                                   '.*Low.*Observable.*': 'CEM Engineer',
                                   '.*Thermal.*Spray.*Coatings.*': 'Mechanical Engineer',
                                   '.*Principal.*Materials.*Engineering.*': 'Materials Engineer',
                                   '.*Manufacturing.*Engineer.*': 'Manufacturing Engineer',
                                   '.*Electrician.*Focus.*': 'Electrical Engineer',
                                   '.*Building.*Automation.*and.*': 'Automation Engineer',
                                   '.*Medical.*Devices.*': 'Medical Device Engineer',
                                   '.*Engineer.*III.*': 'Mechanical Engineer',
                                   '.*Engineer.*II.*': 'Mechanical Engineer',
                                   '.*Control.*System.*Engineer.*': 'Systems Engineer'}}, regex=True)
data = data.drop([data.index[310], data.index[336], data.index[334], data.index[407], data.index[409], data.index[384],
                   data.index[494], data.index[399], data.index[429], data.index[502], data.index[504], data.index[507],
                   data.index[511], data.index[515], data.index[520], data.index[530], data.index[528], data.index[527],
                   data.index[523], data.index[524], data.index[532], data.index[537], data.index[579], data.index[573],
                   data.index[571], data.index[566], data.index[567], data.index[568], data.index[569], data.index[562],
                   data.index[558], data.index[559], data.index[556], data.index[548], data.index[549], data.index[550],
                   data.index[544], data.index[545], data.index[542], data.index[539], data.index[540], data.index[541],
                   data.index[574]])

print(data.head(100))
print(data['Job Description'].head(50))
print(data.describe())
print(data['Employment Type'].head(100))

data.to_excel(r'C:\Users\Desktop\Mechanical Engineer LinkedIn1.xlsx',
              index=False, header=True)
