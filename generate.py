import argparse
import os
import json
import config
import uuid as gen_uuid


class ProblemGenerator:

    def __init__(self, problem_type='', problem_name='', problem_description=''):
        self.db = self.get_db(self.get_db_path())
        self.problem_type = problem_type if problem_type != '' else config.DEFAULT_PROBLEM_TYPE
        self.problem_name = problem_name if problem_name != '' else str(gen_uuid.uuid4())
        self.problem_description = problem_description

    @staticmethod
    def get_db_path():
        return os.path.join(config.ROOT, config.DB_FILE)

    @staticmethod
    def get_db(db_path):
        return json.load(
            open(db_path, 'r')
        )

    def save_db(self):
        json.dump(
            self.db,
            open(self.get_db_path(), 'w')
        )

    def create_new_problem(self):
        # Create problem_type directory if it does not exist
        problem_type_dir = os.path.join(config.ROOT, self.problem_type)
        if not os.path.isdir(problem_type_dir):
            os.mkdir(problem_type_dir)
            print 'Created directory {}'.format(problem_type_dir)

        dir_path = self.dir_structure(config.ROOT, self.problem_type, self.problem_name)

        if os.path.isdir(dir_path):
            print 'Problem {}/{} already exists'.format(self.problem_type, self.problem_name)
            raise NameError

        # Create folder
        os.mkdir(dir_path)
        print 'Created directory {}'.format(dir_path)

        # Create files
        self.create_files(dir_path)

        # Add the problem to the database
        self.add_to_db()

    def create_files(self, dir_path):
        # Now create readme.md and solution.py
        readme = open(
            os.path.join(dir_path, 'readme.md'),
            'w'
        )
        readme.write('# {} - Problem {}\n'.format(self.problem_type, self.problem_name))
        readme.write(self.problem_description)
        readme.close()

        solution = open(
            os.path.join(dir_path, 'solution.py'),
            'w'
        )
        solution.write('# solution.py')
        solution.close()

    def add_to_db(self, save_db=True):
        # Add the problem to database
        self.db.append(
            {
                'type': self.problem_type,
                'name': self.problem_name,
                'description': self.problem_description
            }
        )
        if save_db:
            self.save_db()

    @staticmethod
    def dir_structure(root, problem_type, problem_name):
        return os.path.join(root, problem_type, problem_name)


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

