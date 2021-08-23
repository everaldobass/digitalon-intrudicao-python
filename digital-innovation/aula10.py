# Aprenda a utilizar informações de data, horário e relacionar datas diferentes
from datetime import date

def trabalhando_date():
    data_atual = date.today()
# converter data
    print(data_atual.strftime('%d/%m/%y'))
# Y Maiusculo
    print(data_atual.strftime('%d-%m-%Y'))
# Dia Mês e Ano - String
    print(data_atual.strftime('%A - %B- %Y'))

if __name__ == '__main__':
    trabalhando_date()