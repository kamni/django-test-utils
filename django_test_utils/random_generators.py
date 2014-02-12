"""
A module to generate various pseudo-random values for use in tests and model 
fields.
"""
import random

from django.contrib.webdesign.lorem_ipsum import words


def lorem_ipsum(word_count):
    """
    Generates a 'lorem ipsum' string of the specified length in words.
    
    :param words: number of words to generate
    :return: string
    """
    return words(word_count, common=False)

def random_name():
    """ 
    Returns a tuple of a pseudo-randomly selected first and last name.
    
    Names come from top 100 baby names for girls, boys in 2013 and top 125 
    last names in the U.S.
    
    :return: (string, string)
    """
    _first_names = ['Aaliyah', 'Aaron', 'Abigail', 'Adalyn', 'Adam', 'Addison', 
                    'Adeline', 'Adrian', 'Aiden', 'Alaina', 'Alex', 'Alexander', 
                    'Alexandra', 'Alexis', 'Alice', 'Allison', 'Alyssa', 
                    'Amelia', 'Andrew', 'Anna', 'Annabelle', 'Anthony', 'Aria', 
                    'Arianna', 'Asher', 'Aubrey', 'Audrey', 'Austin', 'Ava', 
                    'Avery', 'Bailey', 'Bella', 'Benjamin', 'Bentley', 'Blake', 
                    'Brayden', 'Brody', 'Brooklyn', 'Caden', 'Caleb', 'Callie', 
                    'Camden', 'Cameron', 'Camilla', 'Caroline', 'Carson', 
                    'Carter', 'Charlie', 'Charlie', 'Charlotte', 'Chase', 
                    'Chloe', 'Christian', 'Christopher', 'Claire', 'Cole', 
                    'Colin', 'Colton', 'Connor', 'Cooper', 'Daniel', 'David', 
                    'Declan', 'Dominic', 'Dylan', 'Elena', 'Eli', 'Eliana', 
                    'Elijah', 'Elizabeth', 'Ella', 'Ellie', 'Elliot', 'Emily', 
                    'Emma', 'Ethan', 'Eva', 'Evan', 'Evelyn', 'Gabriel', 
                    'Gabriella', 'Gavin', 'Gianna', 'Grace', 'Grayson', 
                    'Hailey', 'Hannah', 'Harper', 'Henry', 'Hudson', 'Hunter', 
                    'Ian', 'Isaac', 'Isabella', 'Isabelle', 'Isaiah', 'Jack', 
                    'Jackson', 'Jacob', 'Jake', 'James', 'Jasmine', 'Jason', 
                    'Jayce', 'Jayden', 'Jeremiah', 'John', 'Jonathan', 'Jordan', 
                    'Jordyn', 'Joseph', 'Joshua', 'Josiah', 'Julia', 'Julian', 
                    'Juliana', 'Kaelyn', 'Kaitlyn', 'Katherine', 'Kayla', 
                    'Kaylee', 'Keira', 'Kennedy', 'Kylie', 'Landon', 'Lauren', 
                    'Layla', 'Leah', 'Leo', 'Levi', 'Liam', 'Lila', 'Liliana', 
                    'Lillian', 'Lily', 'Lincoln', 'Logan', 'London', 'Lucas', 
                    'Lucy', 'Luke', 'Mackenzie', 'Madelyn', 'Madison', 
                    'Makayla', 'Maria', 'Mason', 'Mateo', 'Matthew', 'Max', 
                    'Maya', 'Mia', 'Micah', 'Michael', 'Mila', 'Miles', 'Molly', 
                    'Muhammad', 'Natalie', 'Nathan', 'Nathaniel', 'Nicholas', 
                    'Noah', 'Nolan', 'Nora', 'Oliver', 'Olivia', 'Owen', 
                    'Parker', 'Penelope', 'Peyton', 'Reagan', 'Riley', 'Riley', 
                    'Ruby', 'Ryan', 'Sadie', 'Samantha', 'Samuel', 'Sarah', 
                    'Savannah', 'Scarlett', 'Sebastian', 'Skyler', 'Sophia', 
                    'Sophie', 'Stella', 'Sydney', 'Taylor', 'Thomas', 'Tristan', 
                    'Tyler', 'Victoria', 'Violet', 'Vivian', 'William', 'Wyatt', 
                    'Xavier', 'Zachary', 'Zoe']    
    _last_names = ['Adams', 'Alexander', 'Allen', 'Anderson', 'Bailey', 'Baker', 
                   'Barnes', 'Bell', 'Bennett', 'Brooks', 'Brown', 'Bryant', 
                   'Butler', 'Campbell', 'Carter', 'Clark', 'Cole', 'Coleman', 
                   'Collins', 'Cook', 'Cooper', 'Cox', 'Cruz', 'Davis', 'Diaz', 
                   'Edwards', 'Ellis', 'Evans', 'Fisher', 'Flores', 'Ford', 
                   'Foster', 'Freeman', 'Garcia', 'Gibson', 'Gomez', 'Gonzales', 
                   'Gonzalez', 'Graham', 'Gray', 'Green', 'Griffin', 'Hall', 
                   'Hamilton', 'Harris', 'Harrison', 'Hayes', 'Henderson', 
                   'Hernandez', 'Hill', 'Howard', 'Hughes', 'Jackson', 'James', 
                   'Jenkins', 'Johnson', 'Jones', 'Jordan', 'Kelly', 'King', 
                   'Lee', 'Lewis', 'Long', 'Lopez', 'Marshall', 'Martin', 
                   'Martinez', 'Mcdonald', 'Miller', 'Mitchell', 'Moore', 
                   'Morgan', 'Morris', 'Murphy', 'Murray', 'Myers', 'Nelson', 
                   'Ortiz', 'Owens', 'Parker', 'Patterson', 'Perez', 'Perry', 
                   'Peterson', 'Phillips', 'Powell', 'Price', 'Ramirez', 'Reed', 
                   'Reynolds', 'Richardson', 'Rivera', 'Roberts', 'Robinson', 
                   'Rodriguez', 'Rogers', 'Ross', 'Russell', 'Sanchez', 
                   'Sanders', 'Scott', 'Simmons', 'Smith', 'Stewart', 
                   'Sullivan', 'Taylor', 'Thomas', 'Thompson', 'Torres', 
                   'Turner', 'Walker', 'Wallace', 'Ward', 'Washington', 
                   'Watson', 'Webb', 'Wells', 'West', 'White', 'Williams', 
                   'Wilson', 'Wood', 'Woods', 'Wright', 'Young']

    return random.choice(_first_names), random.choice(_last_names)