from countryapp.models import Country

countries = [
        {'name': 'Albania', 'flag': 'https://upload.wikimedia.org/wikipedia/commons/3/36/Flag_of_Albania.svg', 'continent': 'Europe'},
        {'name': 'Andorra', 'flag': 'https://upload.wikimedia.org/wikipedia/commons/1/19/Flag_of_Andorra.svg', 'continent': 'Europe'},
        {'name': 'Australia', 'flag': 'https://upload.wikimedia.org/wikipedia/commons/b/b9/Flag_of_Australia.svg', 'continent': 'Oceania'},
        {'name': 'Brazil', 'flag': 'https://upload.wikimedia.org/wikipedia/commons/0/05/Flag_of_Brazil.svg', 'continent': 'South America'},
        {'name': 'Belgium', 'flag': 'https://upload.wikimedia.org/wikipedia/commons/6/65/Flag_of_Belgium.svg', 'continent': 'Europe'},
        {'name': 'Canada', 'flag': 'https://upload.wikimedia.org/wikipedia/commons/c/cf/Flag_of_Canada.svg', 'continent': 'North America'},
        {'name': 'China', 'flag': 'https://upload.wikimedia.org/wikipedia/commons/5/53/Flag_of_China.svg', 'continent': 'Asia'},
        {'name': 'France', 'flag': 'https://upload.wikimedia.org/wikipedia/commons/c/c3/Flag_of_France.svg', 'continent': 'Europe'},
        {'name': 'Germany', 'flag': 'https://upload.wikimedia.org/wikipedia/commons/b/ba/Flag_of_Germany.svg', 'continent': 'Europe'},
        {'name': 'India', 'flag': 'https://upload.wikimedia.org/wikipedia/commons/4/41/Flag_of_India.svg', 'continent': 'Asia'},
        {'name': 'Indonesia', 'flag': 'https://upload.wikimedia.org/wikipedia/commons/9/9f/Flag_of_Indonesia.svg', 'continent': 'Asia'},
        {'name': 'Ireland', 'flag': 'https://upload.wikimedia.org/wikipedia/commons/4/45/Flag_of_Ireland.svg', 'continent': 'Europe'},
        {'name': 'Italy', 'flag': 'https://upload.wikimedia.org/wikipedia/commons/0/03/Flag_of_Italy.svg', 'continent': 'Europe'},
        {'name': 'Japan', 'flag': 'https://upload.wikimedia.org/wikipedia/commons/9/9e/Flag_of_Japan.svg', 'continent': 'Asia'},
        {'name': 'Kenya', 'flag': 'https://upload.wikimedia.org/wikipedia/commons/4/49/Flag_of_Kenya.svg', 'continent': 'Africa'},
        {'name': 'Luxembourg', 'flag': 'https://upload.wikimedia.org/wikipedia/commons/6/63/Flag_of_Luxembourg.svg', 'continent': 'Europe'},
        {'name': 'Mexico', 'flag': 'https://upload.wikimedia.org/wikipedia/commons/f/fc/Flag_of_Mexico.svg', 'continent': 'North America'},
        {'name': 'New Zealand', 'flag': 'https://upload.wikimedia.org/wikipedia/commons/6/64/Flag_of_New_Zealand.svg', 'continent': 'Oceania'},
        {'name': 'Nigeria', 'flag': 'https://upload.wikimedia.org/wikipedia/commons/7/79/Flag_of_Nigeria.svg', 'continent': 'Africa'},
        {'name': 'Portugal', 'flag': 'https://upload.wikimedia.org/wikipedia/commons/5/5c/Flag_of_Portugal.svg', 'continent': 'Europe'},
        {'name': 'Russia', 'flag': 'https://upload.wikimedia.org/wikipedia/commons/f/f3/Flag_of_Russia.svg', 'continent': 'Europe/Asia'},
        {'name': 'South Africa', 'flag': 'https://upload.wikimedia.org/wikipedia/commons/a/af/Flag_of_South_Africa.svg', 'continent': 'Africa'},
        {'name': 'South Korea', 'flag': 'https://upload.wikimedia.org/wikipedia/commons/0/0f/Flag_of_South_Korea.svg', 'continent': 'Asia'},
        {'name': 'Spain', 'flag': 'https://upload.wikimedia.org/wikipedia/commons/9/9a/Flag_of_Spain.svg', 'continent': 'Europe'},
        {'name': 'Sweden', 'flag': 'https://upload.wikimedia.org/wikipedia/commons/4/4c/Flag_of_Sweden.svg', 'continent': 'Europe'},
        {'name': 'Thailand', 'flag': 'https://upload.wikimedia.org/wikipedia/commons/a/a9/Flag_of_Thailand.svg', 'continent': 'Asia'},
        {'name': 'Ukraine', 'flag': 'https://upload.wikimedia.org/wikipedia/commons/4/49/Flag_of_Ukraine.svg', 'continent': 'Europe'},
        {'name': 'United Kingdom', 'flag': 'https://upload.wikimedia.org/wikipedia/commons/a/a5/Flag_of_the_United_Kingdom.svg', 'continent': 'Europe'},
        {'name': 'United States of America', 'flag': 'https://upload.wikimedia.org/wikipedia/commons/a/a4/Flag_of_the_United_States.svg', 'continent': 'North America'},
        {'name': 'Vietnam', 'flag': 'https://upload.wikimedia.org/wikipedia/commons/2/21/Flag_of_Vietnam.svg', 'continent': 'Asia'},
        {'name': 'Zambia', 'flag': 'https://upload.wikimedia.org/wikipedia/commons/0/06/Flag_of_Zambia.svg', 'continent': 'Africa'}
     ]

def run():
    for country in countries:
        Country.objects.get_or_create(
            name=country['name'],
            flag=country['flag'],
            continent=country['continent']
        )
    print("Countries loaded successfully!")
