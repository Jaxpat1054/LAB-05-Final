from poke_api import get_specific_pokemon
from pastebin_api import post_new_paste
import sys


def main():
    search_term = get_search_term()
    pokemon_ability = get_specific_pokemon(search_term = 'pikachu' )
    if pokemon_ability :
        title , body_text = get_paste_content(pokemon_ability, search_term)
        paste_url =  post_new_paste(title, body_text)
        print(f'URL of pokemon abilities: {paste_url}')   
    


def get_search_term():
    parameters = len(sys.argv)  
    if parameters > 0:
        return sys.argv[1]
    else:
        print("No search term")
        sys.exit(1)
    

def get_paste_content(pokemon_ability, search_term):
    title = f'Abilities of "{search_term}" Pokemon'
    body_text = ''
    for ability in pokemon_ability:
        body_text = f'-{ability}' , pokemon_ability
    return title, body_text
 

if __name__ == "__main__":
    main()
