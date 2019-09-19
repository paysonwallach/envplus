import cleo

class AddCommand(cleo.Command):
    """
    Add environments to the active virtual environment

    add
        {environments* : Virtual environments to add to the currently-active environment}
    """

    def __init__(self, pf, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pf = pf

    def handle(self):
        environments = self.argument("environments")

        for environment in environments:
            self.pf.add_env(environment)

        self.pf.save()
