import cleo

class DescribeCommand(cleo.Command):
    """
    Describe the active virtual environment

    describe
    """

    def __init__(self, pf, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pf = pf

    def handle(self):
        self.line(self.pf.to_string())
