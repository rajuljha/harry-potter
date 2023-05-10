from requests_html import HTMLSession

s = HTMLSession()

url = 'https://screenrant.com/patronuses-harry-potter-characters/'

r = s.get(url)

products = r.html.find('h2')

patronus_list = []

for item in products:
    patronus_list.append(item.find()[1].text.strip())

patronus_dict = {}

def get_patronus():        
    for item in patronus_list:
        patronus,character = item.split(' - ')
        if ' and ' in character:
            char1, char2 = character.split(' and ')
            patronus_dict[f'{char1}'] = patronus
            patronus_dict[f'{char2}'] = patronus
        else:
            patronus_dict[f'{character}'] = patronus
    return patronus_dict

# print(get_patronus())
if __name__ == '__main__':
    get_patronus()