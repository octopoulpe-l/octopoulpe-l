import datetime
import pendulum
prochain_samedi = pendulum.now().next(pendulum.SATURDAY).strftime('%m/%d/%y %H:%M:%S')
prochain_samedi = datetime.datetime.strptime(prochain_samedi, '%m/%d/%y %H:%M:%S')
prochain_17 = prochain_samedi + datetime.timedelta(hours = 17)
datetime_object = datetime.datetime.now()
result = (prochain_17-datetime_object).total_seconds() / 60.0
result=result // 3.30
print('Tu peux regarder ' + str(int(result)) + ' clips de Lorie avant le prochain live de Dork !')