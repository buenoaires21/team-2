  
def preformat_data(data):
    #formatted_data = preformat_data(data)
    pass

def save_to_db(preformatted_data):
    pass

def save_to_text_file(data_list):
    
    with open("scraped.txt", 'w') as output:
        for row in data_list:
            output.write(str(row) + '\n')