import requests
import json
import xlsxwriter


api = 'https://developers.hotmart.com/'

# credenciais
CLIENT_ID = ''
CLIENT_SECRET = ''
BASIC = ''
TOKEN = ''

# fazer o requerimento de dados
subdomain = ''

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
