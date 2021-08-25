import requests
import json
import xlsxwriter


api = 'https://developers.hotmart.com/'

# credenciais
CLIENT_ID = 'e2318b81-6fa7-4ec3-9421-3d53a69d07e5'
CLIENT_SECRET = 'f9bd838a-fa42-4089-977b-213e06af2ec0'
BASIC = 'ZTIzMThiODEtNmZhNy00ZWMzLTk0MjEtM2Q1M2E2OWQwN2U1OmY5YmQ4MzhhLWZhNDItNDA4OS05NzdiLTIxM2UwNmFmMmVjMA=='
TOKEN = 'H4sIAAAAAAAAAB2PWZdrQACEf5E5liHxKLa0pQ2Npl9yLEFbk4kQfv1157WqvjpV981qcrOgHrVQtAMOUvACYyAWKpBA90hi1ZK%2F7pu1p7y8EgQkvFkbwUYH6EpLwXqUZkQTtFKSNCtopw9s3dUNFRZq%2Bu6oVlMmwZT%2F5fq%2B2P54EHIB9GMrSljDR8gqj9yzNLtjBBAgNhrSxj1BXAP3pnNCf0v3bvZCV0g3lodazbo8bFyc8p6p04Nt86M7H4Mqw%2F7%2FI73buh%2FPBN8uYnky6IITBn26u0eHvx3aTrRoT8NUJJoikDCilf9VwY195U%2FvaXUBqy%2BtIiiDXilkDn8In0%2FSu3cU%2F3Li4dv4keccGNXwVCv4xCTO9GkTrfamC3JxbuuYtZtJOZ8eOArlMo9vqCXotWsnkUOMPSnVPAy%2FoaSFXsZoKMKq8kr96pzDy3ev4qd2fYyZONokuPLzkjgSLtdUNqly85DP9E0HQ85jhJE6YybNrLSNayX1bkGolH742kYDI%2BoGveYDFkunWWQQFnfb6%2BluGFodNxYhgcq59cIR5jDKAr%2FtYNGFFyo6zipO5CGmaXtW8MywSKFxTJfPNsli%2FE5eu%2BlkTEZMQi9vzajYQjSSCwB0tJc9TuAZdUodXDyjuDtx3Nu%2F9T%2FxdQqrXgIAAA%3D%3D'

# fazer o requerimento de dados
subdomain = 'vbmappnapratica'

headers = {
    'Content-Type': 'application/json',
    'Authorization': 'bearer ' + TOKEN
}

url = api + 'club/api/v1/users?subdomain=' + subdomain


res = requests.get(url, headers=headers)

data = res.json()
data = data['items']

# coletar apenas o id, nome e email dos alunos
students_datas = []
for c in range(0, len(data)):
    infos = {
        data[c]['user_id']: [data[c]['name'], data[c]['email']]
    }
    students_datas.append(infos)

workbook = xlsxwriter.Workbook('Dados-dos-alunos.xlsx')
worksheet = workbook.add_worksheet()

for i in range(0, len(students_datas)):
    if i == 1:
        worksheet.write('A1', 'ID')
        worksheet.write('B1', 'NOME')
        worksheet.write('C1', 'EMAIL')
    else:
        for key, value in students_datas[i].items():
            worksheet.write(f'A{i}', key)
            worksheet.write(f'B{i}', value[0])
            worksheet.write(f'C{i}', value[1])


workbook.close()
print(students_datas[0].items())
