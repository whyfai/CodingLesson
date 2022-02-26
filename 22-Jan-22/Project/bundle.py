class Bundle():
    bundles = []
    def __init__(self, id, name, bundle):
        self.__id = id
        self.__name = name
        self.__bundle = bundle
        Bundle.bundles.append(self)
    
    def __repr__(self):
        services = [f", {service}" for service in self.bundle].join("")
        return f"{self.id}, {self.name}{services}"
    
    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, id):
        self.__id = id
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def bundle(self):
        return self.__bundle
    
    @bundle.setter
    def bundle(self, bundle):
        self.__bundle = bundle