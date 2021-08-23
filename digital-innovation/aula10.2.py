from datetime import date, time, datetime, timedelta

# Data Em String
def caulculo_data():
    data_string = "22/08/2021"
    data_converter = datetime.strptime(data_string, '%d/%m/%Y')# Y tem que ser maiusculo
    print(data_converter)
    # Somar com data
    nova_data = data_converter + timedelta(days=365, hours=2, minutes=15)
    print(nova_data)

    # Subtração com data
    nova_data = data_converter - timedelta(days=365, hours=2, minutes=15)
    print(nova_data)


if __name__ == '__main__':
    print(caulculo_data())
