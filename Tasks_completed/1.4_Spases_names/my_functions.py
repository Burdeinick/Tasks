import global_var as g_v


def call_fun(ar_1, ar_2, ar_3):
    """This is a function for call other functions.

    Value of the first argument (ar_1) determines
    that function will be called.

    Are arguments:
    ar_1 can make value only 'add', 'create' or 'get',
    ar_2, ar_3 can make value name namespase or name variable

    """

    if ar_1 == 'add':
        add(ar_2, ar_3)

    elif ar_1 == 'create':       
        create(ar_2, ar_3)

    elif ar_1 == 'get':
        get(ar_2, ar_3)


def create(ar_2, ar_3):
    """This is a function that adds new namespaces."""

    g_v.dic[ar_3].append(ar_2)
    g_v.dic.setdefault(ar_2,[ar_3])

def add(ar_2, ar_3):
    """This is a function that adds to namespaces a new variable."""
    
    g_v.dic[ar_2].append(ar_3) 

def get(ar_2, ar_3):
    """This is a function that can get the name variable of namespace.

    If in namespace non this variable then go in namespace higher,
    but when in namespaces higher this a variable not find, function 
    will append to 'itog_list' - 'None'.
    
    """

    if ar_3 in g_v.dic[ar_2]:
        g_v.itog_list.append(ar_2)

    elif ar_3 not in g_v.dic[ar_2] and g_v.dic[ar_2][0] != None:
        get(g_v.dic[ar_2][0], ar_3)

    else:
        g_v.itog_list.append('None')
       
