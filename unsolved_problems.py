from problem_generator import ProblemGenerator


if __name__ == '__main__':
    db = ProblemGenerator.get_db(
        ProblemGenerator.get_db_path()
    )

    unsolved = []

    for problem in db:
        if not problem['solved']:
            unsolved.append(problem)

    print 'There are {} unsolved problems'.format(len(unsolved))
    for problem in unsolved:
        print '- {} / {} / {}'.format(problem['type'], problem['name'], problem['description'])
