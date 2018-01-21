def Enabled(cls):
    """
    Decorator to tag an application as enabled. An enabled application will be installed
    on a system install.
    """
    return EnabledApplication(cls)


class EnabledApplication:
    """ Helper class used to signal an application as enabled """

    def __init__(self, cls):
        self._cls = cls

    def __call__(self, *args, **kwargs):
        return self._cls(*args, **kwargs)
