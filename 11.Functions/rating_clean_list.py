
def rating_list_clean(rating_list):
    """ clean list of rating and return numeric rating list
    Args:
        rating_list(list):list of text string
    Returns:
        list:list of integer
    """
    
    number_list =[]
    for i in rating_list:
        number =int(i[0])
        number_list.append(number)
    return number_list

def rating_clean(rating):
    """gets numeric portion from web rating
    Args:
        rating(str):text rating from web
        
    Returns
        int:integer portion of rating
    """
    
    rating_number =int(rating[0])
    return rating_number


