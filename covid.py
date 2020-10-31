from covid import Covid
covid=Covid(source ='worldometer')
data = covid.get_data()
data

countries = covid.get_status_by_country_name('India')