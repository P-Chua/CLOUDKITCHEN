products = {
    100: {"name":"Americano","price":125},
    200: {"name":"Brewed Coffee","price":110},
    300: {"name":"Cappuccino","price":120},
    400: {"name":"Espresso","price":120},
    500: {"name":"Latte","price":140},
    600: {"name":"Cold Brew","price":200}
}

def get_product(code):
    return products[code]

def get_products():
        product_list = []
        
        for i,v in products.items():
            product = v
            product.setdefault("code", i)
            product_list.append(product)
            
        return product_list
    
branches = {
    100: {"name":"Katipunan","number":140},
    200: {"name":"Tomas Morato","number":140},
    300: {"name":"Eastwood","number":140},
    400: {"name":"Tiendesitas","number":150},
    500: {"name":"Arcovia","number":150},
}

def get_branch(code):
    return branches[code]

def get_branches():
    branch_list = []

    for i,v in branches.items():
        branch = v
        branch.setdefault("code", i)
        branch_list.append(branch)

    return branch_list

users = {
    "paul":{"password":"170521","first_name":"Paul","last_name":"Chua"}
}

def get_user(username):
    try:
       return users[username]
    except KeyError:
       return None
