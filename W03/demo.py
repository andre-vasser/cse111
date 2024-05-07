def main():
    print('Hello from main')
    hello()
    
#def hello():
 #   print('Hello World')
    
def hello(name: str) -> str:
    """Welcome a new user.
    
    Args
        name (str): The persons name.
        
    Returns:
        str: The welcome message with the users name."""
        
return f'Hello, {name}!'
    
if __name__ == '__main__':
    main()