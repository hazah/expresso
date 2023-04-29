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
  throw methodName(T, OtherConcept) == method;
}
```

### Templates

```
type TemplateType<type T> {
  // Template body
}

method TemplateMehtod<type T> {
  // Template body
}

subjcet TemplateSubject<type T> {
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

## Domain-Driven Design in Expresso

Expresso embraces Domain-Driven Design principles to improve code readability and to help developers focus on the high-level concepts of their application domain. By using DDD-specific constructs, you write code that better reflects your specific problem.

### Example: Online Store

The following is a simple online store domain model using the DDD constructs:

```expresso
// Value objects
value Email {
  String address;
}

value FullName {
  String firstName;
  String lastName;
}

// Entity objects
entity Customer {
  FullName fullName;
  Email email;
}

entity Product {
  String name;
  String description;
  Double price;
}

// Aggregate root
aggregate Order {
  Customer customer;
  List<OrderItem> items;
}

entity OrderItem {
  Product product;
  Integer quantity;
}

// Repository
repository OrderRepository {
  method save(Order order);
  method findById(UUID id);
  method findAll();
}

// Domain Service
service OrderService {
  method placeOrder(Customer customer, List<OrderItem> items);
}

// Application Service
service OrderApplicationService {
  method createOrder(Customer customer, List<Product> products);
}
```

In this example, we defined value objects (Email and FullName), entity objects (Customer, Product, OrderItem), an aggregate root (Order), a repository (OrderRepository), a domain service (OrderService), and an application service (OrderApplicationService). Expresso will internally rewrite these DDD constructs using its core language constructs, such as types, subjects, and aspects.

In Expresso, you can create code that is more focused on the domain logic, making it easier to focus on the problem being addressed.

### Benefits of DDD in Expresso

- Improved code readability and maintainability
- A focus on high-level domain concepts
- Easier communication between developers and domain experts
- A natural fit for complex and evolving domain models

By incorporating DDD principles of the Expresso language, you can better reflect the underlying domain.

## Test-Driven Development in Expresso

Expresso supports Test-Driven Development (TDD) as a first-class citizen by providing built-in constructs for defining tests, cases, and expectations. With Expresso's TDD features, you can create an automatic testing and code coverage step during compilation, ensuring that your code is well-tested and robust.

### Example: Testing a Calculator

Let's build a simple calculator and write tests for its functionality using Expresso's TDD constructs:

```expresso
type Calculator {
  method add(Double a, Double b) {
    throw a + b;
  }

  method subtract(Double a, Double b) {
    throw a - b;
  }

  method multiply(Double a, Double b) {
    throw a * b;
  }

  method divide(Double a, Double b) {
    throw a / b;
  }
}

test Calculator {
  Calculator {}
  before {}
  after {}

  case addition {
    expect target.add(2, 3) to throw 5;    
    expect target.add(-1, 4) to throw 3;
  }

  case subtraction {
    expect target.subtract(7, 3) to throw 4;
    expect target.subtract(2, -2) to throw 4;
  }

  case multiplication {
    expect target.multiply(3, 4) to throw 12;
    expect target.multiply(-2, 3) to throw -6;
  }

  case division {
    expect target.divide(10, 2) to throw 5;
    expect target.divide(9, -3) to throw -3;
  }
}
```

In this example, we defined a Calculator type and then created a test suite called CalculatorTests with test cases for addition, subtraction, multiplication, and division. The test cases use Expresso's TDD constructs, such as `expect`, to define their expectations. Expresso will rewrite these TDD constructs using its core language constructs during compilation and generate an automatic testing and code coverage report.

### Benefits of TDD in Expresso

- Ensures well-tested and robust code
- Encourages writing tests before implementing functionality
- Improved code quality and maintainability
- Automatic testing and code coverage during compilation

By integrating TDD principles into the Expresso language, you can build more reliable and maintainable applications while enjoying the benefits of a streamlined testing process.