from clients.exercises.exercises_schema import CreateExerciseRequestSchema, CreateExerciseResponseSchema, \
    ExerciseSchema, GetExerciseResponseSchema
from tools.assertions.base import assert_equal


def assert_create_exercise(actual: CreateExerciseResponseSchema, expected: CreateExerciseRequestSchema):
    """
    Проверяет что созданное упражнение соответствует ожидаемом модели данных
    :param actual: ответ полученный от API который нужно проверить
    :param expected: запрос переданный в API
    :return: AssertionError если хотя бы одно значение не совпадает
    """
    assert_equal(actual.exercise.title, expected.title, "title")
    assert_equal(actual.exercise.course_id, expected.course_id, "course_id")
    assert_equal(actual.exercise.max_score, expected.max_score, "max_score")
    assert_equal(actual.exercise.min_score, expected.min_score, "min_score")
    assert_equal(actual.exercise.order_index, expected.order_index, "order_index")
    assert_equal(actual.exercise.description, expected.description, "description")
    assert_equal(actual.exercise.estimated_time, expected.estimated_time, "estimated_time")


def assert_exercise(actual: ExerciseSchema, expected: ExerciseSchema):
    """
    Сравнение данных двух моделей упражнения
    :param actual: Полученный от API ответ
    :param expected: Ожидаемый от API ответ
    :return: AssertionError если хотя бы одно значение не совпадает
    """
    assert_equal(actual.id, expected.id, "id")
    assert_equal(actual.title, expected.title, "title")
    assert_equal(actual.course_id, expected.course_id, "course_id")
    assert_equal(actual.max_score, expected.max_score, "max_score")
    assert_equal(actual.min_score, expected.min_score, "min_score")
    assert_equal(actual.order_index, expected.order_index, "order_index")
    assert_equal(actual.description, expected.description, "description")
    assert_equal(actual.estimated_time, expected.estimated_time, "estimated_time")


def assert_get_exercise(actual: CreateExerciseResponseSchema, expected: GetExerciseResponseSchema):
    """
    Проверка ответа полученного от API на запрос получения упражнения
    :param actual: Ответ полученный от API при создании упражнения
    :param expected: Ответ полученный от API при запросе упражнения по id
    :return: AssertionError если хотя бы одно значение не совпадает
    """
    assert_exercise(actual.exercise, expected.exercise)