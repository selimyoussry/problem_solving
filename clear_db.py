from problem_generator import ProblemGenerator


if __name__ == '__main__':

    yn = raw_input('Are you sure you want to clear the database? y/n\n')

    if yn.lower() == 'y':
        print 'Cleared db'
        ProblemGenerator.clear_db()
    else:
        print 'OK. We won\'t touch it then!'
