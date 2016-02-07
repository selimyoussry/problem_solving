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

    def __repr__(self):
        return '<ProblemGenerator: {} / {} / {}>'.format(
            self.problem_type, self.problem_name, self.problem_description
        )

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

    @staticmethod
    def clear_db():
        json.dump(
            [],
            open(ProblemGenerator.get_db_path(), 'w')
        )

    def del_entry_from_db(self):
        i0 = -1
        for i in range(len(self.db)):
            item = self.db[i]
            if item['type'] == self.problem_type and item['name'] == self.problem_name:
                i0 = i
                break

        if i0 == -1:
            print 'Could not find {} in the database'.format(self)
            raise ValueError

        del self.db[i0]
        self.save_db()
        print '{} deleted from db'.format(self)

    def check_problem_solved(self):
        for item in self.db:
            if item['type'] == self.problem_type and item['name'] == self.problem_name:
                item['solved'] = not item['solved']
                return True
        print 'Could not find the problem {}'.format(self)
        return False

    def create_new_problem(self):
        # Create problem_type directory if it does not exist
        problem_type_dir = os.path.join(config.ROOT, self.problem_type)
        if not os.path.isdir(problem_type_dir):
            os.mkdir(problem_type_dir)
            print 'Created directory {}'.format(problem_type_dir)

        dir_path = self.dir_structure(config.ROOT, self.problem_type, self.problem_name)

        if os.path.isdir(dir_path):
            print 'Problem {} already exists'.format(self)
            raise NameError

        # Create folder
        os.mkdir(dir_path)
        print 'Created directory {}'.format(dir_path)

        # Create files
        self.create_files(dir_path)

        # Add the problem to the database
        self.add_to_db()

        print 'ProblemGenerator {} added'.format(self)

    def create_files(self, dir_path):
        # Now create readme.md and solution.py
        readme = open(
            os.path.join(dir_path, 'readme.md'),
            'w'
        )
        readme.write('# {} - Problem {}\n'.format(self.problem_type, self.problem_name))
        readme.write('{}\n'.format(self.problem_description))
        readme.close()

        solution = open(
            os.path.join(dir_path, 'solution.py'),
            'w'
        )
        solution.write('# solution.py')
        solution.close()

        init = open(
            os.path.join(dir_path, '__init__.py'),
            'w'
        )
        init.write('\n')
        init.close()


    def add_to_db(self, save_db=True):
        # Add the problem to database
        self.db.append(
            {
                'type': self.problem_type,
                'name': self.problem_name,
                'description': self.problem_description,
                'solved': False
            }
        )
        if save_db:
            self.save_db()

    @staticmethod
    def dir_structure(root, problem_type, problem_name):
        return os.path.join(root, problem_type, problem_name)
