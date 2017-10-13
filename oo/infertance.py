'''
  __bases__:  

  __subclasses__:

  __mro__:
'''
class Pet(object):
  def __init__(self, name, species):
    self.name = name
    self.species = species

  def getName(self):
    return self.name

  def getSpecies(self):
    return self.species

  def __str__(self):
    return "%s is a %s"%(self.name, self.species)

class Dog(Pet):
  def __init__(self, name, chases_cats):
    super().__init__(name, "Dog")
    self.chases_cats = chases_cats

  def getName(self):
    return self.name

  def getSpecies(self):
    return self.species

  def __str__(self):
    return "%s is a %s"%(self.name, self.species)


if __name__ == "__main__":
  p = Pet('Polly', 'parrot')
  print p.__str__()

