import pandas as pd
import numpy as np

np.random.seed(42)
n = 10000

records = []

# Patterns derived from sample data
sector_size_configs = {
    ('Banking', 'Small'):      dict(inv=(15,50),  att=(8,20),   succ_ratio=(0.1,0.3), stock_yes=0.4),
    ('Banking', 'Medium'):     dict(inv=(10,25),  att=(5,25),   succ_ratio=(0.1,0.25),stock_yes=0.5),
    ('Banking', 'Large'):      dict(inv=(10,85),  att=(8,22),   succ_ratio=(0.1,0.2), stock_yes=0.4),
    ('Hospitality', 'Small'):  dict(inv=(20,130), att=(30,320), succ_ratio=(0.3,0.6), stock_yes=0.85),
    ('Hospitality', 'Medium'): dict(inv=(15,450), att=(10,330), succ_ratio=(0.3,0.65),stock_yes=0.85),
    ('Hospitality', 'Large'):  dict(inv=(80,230), att=(20,90),  succ_ratio=(0.3,0.6), stock_yes=0.75),
    ('Health Care', 'Small'):  dict(inv=(25,40),  att=(15,60),  succ_ratio=(0.2,0.5), stock_yes=0.7),
    ('Health Care', 'Medium'): dict(inv=(12,150), att=(12,65),  succ_ratio=(0.25,0.55),stock_yes=0.6),
    ('Health Care', 'Large'):  dict(inv=(35,90),  att=(25,55),  succ_ratio=(0.3,0.6), stock_yes=0.65),
}

sectors = ['Banking', 'Hospitality', 'Health Care']
sizes   = ['Small', 'Medium', 'Large']
genders = ['Male', 'Female']
ratings = ['Low', 'Medium', 'High']
exp_lvls= ['Low', 'Medium', 'High']

for _ in range(n):
    sector = np.random.choice(sectors, p=[0.35, 0.33, 0.32])
    size   = np.random.choice(sizes,   p=[0.33, 0.34, 0.33])
    cfg    = sector_size_configs[(sector, size)]

    inv  = int(np.random.randint(cfg['inv'][0],  cfg['inv'][1]+1))
    att  = int(np.random.randint(cfg['att'][0],  cfg['att'][1]+1))
    ratio= np.random.uniform(cfg['succ_ratio'][0], cfg['succ_ratio'][1])
    succ = int(att * ratio)

    gender  = np.random.choice(genders, p=[0.65, 0.35])
    rating  = np.random.choice(ratings)
    exp     = np.random.choice(exp_lvls)
    lot     = int(np.random.randint(1, 26))
    stock   = 'Yes' if np.random.random() < cfg['stock_yes'] else 'No'

    records.append([sector, gender, size, inv, att, succ, rating, exp, lot, stock])

df = pd.DataFrame(records, columns=[
    'Sector','CEO_Gender','Size','Security_Invest','Security_Breach_Att',
    'Succ_Sec_Breaches','Sec_Rating','CEO_Sec_Exp','LOT_in_Business','Stock_Market'
])

df.to_csv('/Users/gauravkumardani/Documents/ml-code-samples/handson-ml3/iris/security_data_10000.csv', index=False)
print(f"Generated {len(df)} records")
print(df.head())
print("\nValue counts - Sector:")
print(df['Sector'].value_counts())
print("\nValue counts - Stock_Market:")
print(df['Stock_Market'].value_counts())
