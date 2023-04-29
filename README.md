# Expresso Programming Language

Expresso is a versatile, powerful, and expressive programming language that combines multiple programming paradigms, including object-oriented programming, generic programming, subject-oriented programming, and aspect-oriented programming. The language is designed to enable developers to create highly modular, reusable, and maintainable code.

## Key Features

- **Types**: Define custom data types with their own properties and methods.
- **Methods**: Encapsulate functionality within methods that can be called with various arguments.
- **Subjects**: Organize related types and aspects within subjects, facilitating modular development.
- **Aspects**: Add behavior to existing types without modifying their source code using aspect-oriented programming.
- **Concepts**: Specify and enforce constraints on types, ensuring that only appropriate types are used in specific contexts.
- **Templates**: Create reusable code templates that can be instantiated with different types.
- **Capturing**: Capture and handle thrown values using the `capture`, `catch`, and `continue` constructs.

## Language Syntax

### Types

```
type TypeName {
  public {
    // Properties and methods
  }
}
```

### Methods

```
method MethodName(ConceptName valueName) {
  // Method body
}
```

### Subjects

```
subject SubjectName {
  // Type declarations, aspects, and imports
}
```

### Aspects

```
aspect AspectName {
  // Pointcuts and advice
}
```

### Concepts

```
concept ConceptName<type T> {
  throw T::methodName == method (OtherConcept valueName);
}
```

### Templates

```
template TemplateName<type T> {
  // Template body
}
```

### Capturing

```
capture {
  // Expressions that throw values
} catch(ValueType valueName) {
  // Handle captured value
  continue valueName;
}
```

## Example

The following example demonstrates the key features of Expresso, including types, methods, subjects, aspects, concepts, templates, and capturing:

```expresso
type Animal {
  public {
    // Animal-specific properties and methods
  }
}

type Food {
  public {
    // Food-specific properties and methods
  }
}

subject DomesticAnimals {
  type Animal {
    // Domestic animal-specific properties and methods
  }

  type Food {
    // Food-specific properties and methods
  }

  aspect DomesticAnimalAspect {
    method eat(Animal animal, Food food) {
      throw "Eating the food"
    }
  }
}

subject WildAnimals {
  type Animal {
    // Wild animal-specific properties and methods
  };

  aspect WildAnimalAspect {
    method hunt(Animal animal) {
      throw "Hunting the prey"
    }
  }
}

subject Logging {
  method log(String message) {
    // Log the message
  }
  aspect LoggingAspect {
    pointcut feedable(): execution(feed(Farmer, Animal, Food)) && within(Farm) && args(farmer, animal, food);
    pointcut observable(): execution(observe(Farmer, Animal)) && within(Farm) && args(farmer, animal);

    before {
      feedable(Farmer farmer, Animal animal, Food food) {
        log("Farmer " + farmer + " feeding " + animal + " with " + food);
      }
      observable(Farmer farmer, Animal animal) {
        log("Farmer " + farmer + " observing " + animal);
      }
    }

    after {
      feedable(Farmer farmer, Animal animal, Food food) {
        log("Farmer " + farmer + " fed " + animal + " with " + food);
      }
      observable(Farmer farmer, Animal animal) {
        log("Farmer " + farmer + " observed " + animal);
      }
    }
  }
}

type Farmer {
  public {
    // Farmer-specific properties and methods
  }
}

concept Eater<type T> {
  throw eat(T, Food) == method;
}

concept Hunter<type T> {
  throw hunt(T) == method;
}

subject Farm {
  type Farmer {
    // Farmer-specific properties and methods
  }

  aspect FarmAspect {
    method feed(Farmer farmer, Eater animal, Food food) {
      animal.eat(food);
    }

    method observe(Farmer farmer, Hunter animal) {
      animal.hunt();
    }
  }
}

subject InsideFarm {
  import DomesticAnimals;
}

subject OutsideFarm {
  import WildAnimals;
}

subject FencedFarm {
  compose Farm || InsideFarm || OutsideFarm || Logging;
}

method main() {
  Animal dog, cat, cheetah, bear;
  Farmer farmer;

  Logging() {
    FencedFarm() {
      capture {
        InsideFarm() {
          farmer.feed(dog, Food()).log();
          farmer.feed(cat, Food()).log();
        }

        OutsideFarm() {
          farmer.observe(cheetah).log();
          farmer.observe(bear).log();
        }
      } catch(String message) {
        continue message;
      }
    }
  }
}
```