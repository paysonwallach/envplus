import cleo

class PauseCommand(cleo.Command):
    """
    Temporarily remove environments from the active virtual environment

    pause
        {environments?* : Virtual environments to temporarily remove from the currently-active environment}
    """

    def __init__(self, pf, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pf = pf

    def handle(self):
        environments = self.argument("environments")

        for environment in [environment if len(environments) else self.pf.ls()
                for environment in environments]:
            self.pf.pause_env(environment)

        self.pf.save()
