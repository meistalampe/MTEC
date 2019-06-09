class Sample:
    def __init__(self, tag, time, value):
        self.tag = tag
        self.time = time
        self.value = value

    @staticmethod
    def create_from_dict(rec):
        return Sample(
            rec['tag'],
            float(rec('time')),
            float(rec('value'))
        )
