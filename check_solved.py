import argparse
from problem_generator import ProblemGenerator


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('type', type=str)
    parser.add_argument('name', type=str)

    args = parser.parse_args()

    pg = ProblemGenerator(
        problem_type=args.type,
        problem_name=args.name,
        problem_description=args.description
    )

    if pg.check_problem_solved():
        print 'Problem {} - {} solved'.format(args.type, args.name)
        pg.save_db()
