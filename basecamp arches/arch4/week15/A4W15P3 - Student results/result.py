class Result:
    def __init__(self, student_id, course_id, mark, achieved):
        self.student_id = student_id
        self.course_id = course_id
        self.mark = mark
        self. achieved = achieved

    # Representation method
    # This will format the output in the correct order
    # Format is @dataclass-style: Classname(attr=value, attr2=value2, ...)
    def __repr__(self) -> str:
        return "{}({})".format(type(self).__name__, ", ".join([f"{key}={value!r}" for key, value in self.__dict__.items()]))
