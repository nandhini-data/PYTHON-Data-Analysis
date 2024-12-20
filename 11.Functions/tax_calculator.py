
def tax_calculator1(subtotal,tax_rate=0.06):
    
    """ takes in subtotal ,default tax rate and return list of subtotal,
    tax and total.
    
    Args:
        subtotal(float,int):cost of item.
        tax_rate(optioanl):tax rate of store location,by default here tax_rate 
        is 0.06
    
    Return:
        list:list containing subtotal,total and tax."""
    
    tax = subtotal * tax_rate
    total = subtotal + tax
    return [subtotal,round(tax,2),round(total,2)]
