import argparse
from problem_generator import ProblemGenerator


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('description', type=str, help='Problem description')
    parser.add_argument('-t', '--type', type=str, default='')
    parser.add_argument('-n', '--name', type=str, default='')

    args = parser.parse_args()

    pg = ProblemGenerator(
        problem_type=args.type,
        problem_name=args.name,
        problem_description=args.description
    )

    pg.create_new_problem()
