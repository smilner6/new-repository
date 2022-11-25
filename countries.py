input_filename = 'country_info.txt'

countries = {}

with open(input_filename) as country_file:
    country_file.readline()
    for row in country_file:
        data = row.strip('\n').split('|')
        country, capital, code, code3, dialing, timezone, currency = data
        # print(country, capital, code, code3, dialing, timezone, currency, sep='\n\t')
        country_dict = {
            'name': country,
            'capital': capital,
            'country_code': code,
            'cc3': code3,
            'dialing_code': dialing,
            'timezone': timezone,
            'currency': currency,
        }


        countries[country.casefold()] = country_dict
        # countries[code.casefold()] = country_dict
    print(countries)

    for country_name, country_info in countries.items():
        for key, value in country_info.items():
            if not value:
                print(country_name.capitalize() + " does not have a " + key)
                # print(f"{country_info[key]} does not have a {value}")
        # if not country_info['capital']:
        #     print(f"{country_info['name']} does not have a capital.")


# while True:
    # user_country = input("Please enter a country or country code to get the capital city: ")
    # country_key = user_country.casefold()
    # if country_key in countries:
    #     country_data = countries[country_key]
    #     print(f"The capital of {user_country} is {country_data['capital']}")
    # elif country_key == 'quit':
    #     break
    # else:
    #     print(f"{country_key} is not a valid county.")





