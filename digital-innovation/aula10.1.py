from datetime import date, time, datetime

def trabalhando_time():
    hora = time(hour=22, minute=10, second=30)
    print(hora)
    # Converter em String
    print(hora.strftime('%A - %B- %Y'))

def trabalhando_datetime():
    datahora = datetime(year=2021, month=8, day=22, hour=9, minute=48, second=40)
    print(datahora)
    data_atual = datetime.now()
    print(data_atual)
    # Pegando por String - Dia, Mês e Ano
    print(data_atual.strftime('%A - %B- %Y'))
    # Pegando apenas a Hora
    print(data_atual.strftime('%H - %M- %S'))
    # Formatando
    print(data_atual.strftime('%d/ %m/ %y - %H - %M- %S'))
    # Formatando com o C
    print(data_atual.strftime('%c'))
    # Traduzindo
    tupla = ('segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sabado', 'domingo')
    print(tupla[data_atual.weekday()])
    #Criando uma data
    data_criada = datetime(2021 , 8, 22, 10,6,30)
    print(data_criada)
    print(data_criada.strftime('%c'))
    # Data Em String
    data_string = "22/08/2021"
    data_converter = datetime.strptime(data_string, '%d/%m/%Y')# Y tem que ser maiusculo
    print(data_converter)


if __name__ == '__main__':
    #trabalhando_time()
    trabalhando_datetime()