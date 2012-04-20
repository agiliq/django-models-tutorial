def level1(input):
    return True
    
def level2(input):
    return input == Author.objects.all()

def level3(input):
    return input == Author.objects.filter(first_name = "Stephen")
    

levels = [
    {
    level = 1,
    test = level1
    greet = """
    Welcome to the Queryget tutorial.
    The interactive queryset tutorial.
    exit the prompt by typing "q"
    """
    }
    question = """
    What is your name?
    """
    goodbye = """
    """
    },
    {
    level = 2,
    test = level2
    greet = """
    The first article you should know about is .all.
    It will give you all the entries for a particular model.
    Eg to get all the Books, the command is
    Book.objects.all()
    """
    }
    question = """
    How can you get all the Authors?
    """
    goodbye = """
    """
    }
    {
    level = 2,
    test = level2
    greet = """
    The first article you should know about is .all.
    It will give you all the entries for a particular model.
    Eg to get all the Books, the command is
    Book.objects.all()
    """
    }
    question = """
    How can you get all the Authors?
    """
    goodbye = """
    """
    }
    
]


    

