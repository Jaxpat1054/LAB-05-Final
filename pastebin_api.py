import requests

API_POST_URL = 'https://pastebin.com/api/api_post.php'
DEVELOPER_API_KEY = '-n4m02N14kueaD-GilftOw4bfHzkMb20'
def main():
    paste_url = post_new_paste('whatever paste', 'a bunch of crap')
    pass

def post_new_paste(title, body_text, expiration='1M', listed=True):
    """Creates a new PasteBin paste

    Args:
        title (str): Paste title
        body_text (str): Paste body text
        expiration (str, optional): How long the paste will last.(See https://pastebin.com/doc_api) Defaults to '10M'.
        listed (bool, optional): Whether the paste is listed or not. Defaults to True.

    Returns:
        str: URL of the new paste. None if unsuccessful.
    """
    #Create dictonary of parameter value
    parameters = {
        'api_dev_key' : {DEVELOPER_API_KEY},
        'api_option' : 'paste',
        'api_paste_code' : body_text,
        'api_paste_name' : title,
        'api_paste_expire_date' : expiration,
        'api_paste_private': 0 if listed else 1
    }  
    # Send the POST request to the PasteBin API
    print("Posting a new paste to Pastebin...", end='')
    resp_message = requests.post(API_POST_URL, data=parameters)
    #if resp_message.status_code == requests.codes.ok:
    #Check if paste was created successfully
    if resp_message.ok:
        print('success')
        #think about it
        #print(f'URL of new paste: {resp_message.text}')
        return resp_message.text
    else:
        print('fail')
        print(f'Response code: {resp_message.status_code} ({resp_message.reason})')     
        print(f"Error: {resp_message.text}")
    pass

if __name__ == "__main__":
    main()