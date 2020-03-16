from os import listdir, path
import time

'Specify the path to quiz directory, default relative path maybe won`t work on every machine'
QUIZ_DIRECTORY_PATH = r'.\quiz'


class QuizManager:
    def __init__(self, filename, mode='r'):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        print(f'{self.filename} was opened.\n')
        return self.file

    def __exit__(self, exc_type, exc_value, exc_traceback):
        print(f'\n{self.filename} is closing ...\n')
        self.file.close()


def time_section_and_quiz(func):
    def wrapper(*args, **kwargs):
        result = {}
        name = func.__name__
        start_time = time.time()
        result['func_result'] = func(*args, **kwargs)
        finish_time = round(time.time() - start_time, 2)
        result['finish_time'] = finish_time
        print("{} took {} secs.".format(name, finish_time))
        return result
    return wrapper


def get_quizes(quiz_path):
    onlyfiles = [f for f in listdir(quiz_path) if path.isfile(path.join(quiz_path, f))]
    return onlyfiles


@time_section_and_quiz
def ask_question(question):
    answer = input(question)
    return answer


def ask_quiz(quiz_path, quiz):
    quiz_file = path.join(quiz_path, quiz)
    if path.isfile(quiz_file):
        return quiz_file


def quiz_writer(quiz_file):
    with QuizManager(quiz_file) as quiz_f, \
            open('answers.txt', 'w') as answers_file, \
            open('timing.txt', 'w') as timing_file:
        for question in quiz_f.readlines():
            result = ask_question(question)
            answers_file.writelines(f'Qusetion: {question.strip()} - '
                                    f'Answer: {result["func_result"]}\n')

            timing_file.writelines(f'Qusetion: {question.strip()} - '
                                   f'Answer took: {result["finish_time"]} seconds\n')


if __name__ == "__main__":
    print('Hallo, Mr/Ms!')
    quiz = input('Which quiz you want to choose?\n'
                 f'Possible quizes: {get_quizes(QUIZ_DIRECTORY_PATH)}\n'
                 '(Enter full name of quiz without brackets)\n')

    quiz_file = ask_quiz(QUIZ_DIRECTORY_PATH, quiz)
    if quiz_file:
        time_wrapper = time_section_and_quiz(quiz_writer)
        time_for_quiz = time_wrapper(quiz_file)['finish_time']
        with open('timing.txt', 'a') as timing_file:
            timing_file.writelines(f'For passing entire quiz you spent {time_for_quiz} seconds!')
        print('Thanks for your time!')
    else:
        print('Sorry, such quiz doesn`t exist')
