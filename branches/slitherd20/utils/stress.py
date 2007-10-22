class StressTest():
    """
    A stress-test class for our dynamic database structure.
    """
    def __init__(self):
        """
        Here, we're going to make a default info dictionary to contain everything,
        we'll include various datatypes as well as other data structures such as
        sub-dictionaries and lists.
        """
        self.info = {}
        self.info["name"] = "Test Dummy"
        self.info["age"] = 99
        self.info["items"] = []
        self.info["items"].append("A sword!")
        self.info["items"].append("An apple!")
        self.info["items"].append(42)
        self.info["subway"] = {}
        self.info["subway"]["route1"] = "Boston to New York"
        self.info["subway"]["route2"] = "LA to SF"
        self.info["subway"]["departure1"] = 1735
        self.info["subway"]["conductors"] = {}
        self.info["subway"]["conductors"]["Jim"]["info"] = {}
        self.info["subway"]["conductors"]["Jim"]["info"]["desc"] = "A jolly-good fellow!"
        self.info["subway"]["conductors"]["Jim"]["info"]["clothing"] = []
        self.info["subway"]["conductors"]["Jim"]["info"]["clothing"].append("A funny hate!")
        self.info["subway"]["conductors"]["Jim"]["info"]["clothing"].append("Overalls!")

        