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

```rust
type TypeName {
  public {
    // Properties and methods
  }
}

type Derived(TypeName) {
  public {
    // Properties and methods
  }
}
```

### Methods

```rust
method MethodName(ConceptName valueName) {
  // Method body
}
```

### Subjects

```rust
subject SubjectName(ConceptName argValue) {
  // Type declarations, aspects, and imports
}
```

### Aspects

```rust
aspect AspectName {
  // Methods, pointcuts and advice
}
```

### Concepts

```rust
concept ConceptName<ConceptOrType T> {
  throw methodName(T, OtherConcept) == method;
}
```

### Templates

```rust
type TemplateType<ConceptName T> {
  // Template body
}

method TemplateMehtod<ConceptName T>() {
  // Template body
}

subject TemplateSubject<ConceptName T>() {
  // Template body
}
```

### Capturing

```rust
capture {
  // Expressions that throw values
} catch(ValueType valueName) {
  // Handle captured value
  continue valueName;
}
```

## Example

The following example demonstrates the key features of Expresso, including types, methods, subjects, aspects, concepts, templates, and capturing:

```rust
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
    pointcut feedable(Farmer farmer, Animal animal, Food food): execution(feed) && within(Farm) && args(farmer, animal, food);
    pointcut observable(Farmer farmer, Animal animal): execution(observe) && within(Farm) && args(farmer, animal);

    before(Farmer farmer, Animal animal, Food food): feedable(farmer, animal, food) {
      log("Farmer " + farmer + " feeding " + animal + " with " + food);
    }
    before(Farmer farmer, Animal animal): observable(farmer, animal) {
      log("Farmer " + farmer + " observing " + animal);
    }

    after(Farmer farmer, Animal animal, Food food): feedable(farmer, animal, food) {
      log("Farmer " + farmer + " fed " + animal + " with " + food);
    }
    after(Farmer farmer, Animal animal): observable(farmer, animal) {
      log("Farmer " + farmer + " observed " + animal);
    }

    around(Farmer farmer, Animal animal, Food food): feedable(farmer, animal, food) {
      proceed(farmer, animal, food);
    }
    around(Farmer farmer, Animal animal): observable(farmer, animal) {
      proceed(farmer, animal);
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

subject Farm() {
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

subject InsideFarm() {
  import DomesticAnimals();
}

subject OutsideFarm() {
  import WildAnimals();
}

subject FencedFarm() {
  compose Farm() || Logging();
}

method main() {
  Animal dog, cat, cheetah, bear;
  Farmer farmer;

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
```

## Domain-Driven Design in Expresso

Expresso embraces Domain-Driven Design principles to improve code readability and to help developers focus on the high-level concepts of their application domain. By using DDD-specific constructs, you write code that better reflects your specific problem.

### Example: Online Store

The following is a simple online store domain model using the DDD constructs:

```rust
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
  OrderItem[] items;

  // lifecycle methods triggered by repositories
  create(/* parameters */) {
    publish OrderCreated(); // Automatically persists the event to the event store
  }
  retrieve(/* parameters */) {
    // Retrieve the order from the store
  }
  update(/* parameters */) {
    // Update the order in the store
  }
  delete(/* parameters */) {
    // Delete the order from the store
  }
}

aggregate Cart {
  CartItem[] items;
}

entity OrderItem {
  Product product;
  Integer quantity;
}

entity CartItem {
  Product product;
  Integer quantity;
}

// provides crud operations for entity data. 
data DatabaseIO {
  create Order(dto Order order) {
    // Uses Order factory to transform the dto back to entity
  }

  retrieve Order(id Order) {
    // Uses Order factory to transform the dto back to entity
  }

  retrieve Order(dto Order order) {
    // Uses Order factory to transform the dto back to entity
  }

  retrieve all Order() {
    // Uses Order factory to transform the dto back to entity
  }

  retrieve EligibleForDiscount Order(dto Order order) {
    // Uses Order factory to transform the dto back to entity
  }

  update Order(Order order) {
    // Uses Order factory to transform the dto back to entity
  }

  delete Order(id Order order) {
    // Uses Order factory to transform the dto back to entity
  }
}

data ConsoleIO {
  create Order(dto Order order) {
    // print the dto to the console
  }

  retrieve Order() {
    // generates dto from console and Order factory transforms it into entity
  }
}

// Repository
repository Order {
  create save using DatabaseIO; // Adds save method to database that creates the order
  
  retrieve find id using DatabaseIO; // Adds find method to database that finds the order by id
  retrieve find dto using DatabaseIO; // Adds find method to database that finds the orders that matches the DTO
  retrieve find all using DatabaseIO; // Adds find method to database that finds all orders
  retrieve findForDiscount EligibleForDiscount(dto) using DatabaseIO; // Adds find method to database that finds all orders that are eligible for discount

  create print dto using ConsoleIO; // Adds print method to console that prints the order
  retrieve get using ConsoleIO; // Adds get method to get order from the console

  update save dto using DatabaseIO; // Adds save method to database that updates the order
  delete delete id using DatabaseIO; // Adds delete method to database that deletes the order
}

// Domain Event
event ItemsAddedToCart(Cart cart, CartItem[] items);

// Domain Service
service AddToCart(Cart cart, CartItem[] items) {
  cart.items.append(items);
  publish ItemsAddedToCart(cart, items)
}

// Application Service
application CreateOrder(Customer customer, Cart cart) {
  
}

factory Order {
  create from dto; // Automatically maps the DTO to the Order aggregate
  create from dto OrderLikeEntity; // Automatically maps the DTO to the OrderLikeEntity entity
}

listener OrderCreatedListener {
  subscribe OrderEventChannel;

  on OrderCreated(event) {
    // Perform actions in response to the OrderCreated event
    // Example: send a confirmation email, update the inventory, etc.
  }
}

repository EventStore {
  create save OrderCreated using DatabaseIO; // Adds save method to database that saves the event
  create print dto OrderCreated using ConsoleIO; // Adds print method to console that prints the event

  create save OrderShipped using DatabaseIO; // Adds save method to database that saves the event
  create print dto OrderShipped using ConsoleIO; // Adds print method to console that prints the event
}

// Define a custom channel for connecting to an event store
channel EventStoreChannel {
  inject EventStore eventStore; // Automatically injects an instance of event store

  on OrderCreated(event) {
    // Save the event to the event store
    eventStore.save(event);
  }

  on OrderShipped(event) {
    // Save the event to the event store
    eventStore.save(event);
  }
}

saga OrderManagement {
  on OrderPlaced(event) {
    // Process the order
  }

  on PaymentReceived(event) {
    // Ship the order
  }

  on OrderShipped(event) {
    // Notify the customer
  }
}

specification EligibleForDiscount(Order order) {
  throw order.total >= 5; // can be used in queries
}

context Sales {
  import Customers;
  import Orders;
  import Discounts;
}

context Shipping {
  import Orders;
  import Deliveries;

  // uses Sales context as the source of the Order aggregate
  // providing context mapping directly for bounded contexts
  repository Order {
    create save dto using Sales; // Adds save method to context that creates the order
    retrieve find id using Sales; // Adds find method to context that finds the order by id
    retrieve find dto using Sales; // Adds find method to context that finds the orders that matches the DTO
    retrieve find all using Sales; // Adds find method to context that finds all orders
    retrieve findForDiscount dto && EligibleForDiscount using Sales; // Adds find method to context that finds all orders that are eligible for discount
    create print dto using Sales; // Adds print method to context that prints the order
    update save dto using Sales; // Adds save method to context that updates the order
    delete delete using Sales; // Adds delete method to context that deletes the order
  }
}
```

In this example, we defined value objects (Email and FullName), entity objects (Customer, Product, OrderItem), an aggregate root (Order), a repository (OrderRepository), a domain service (AddToCart), and an application service (CreateOrder). Expresso will internally rewrite these DDD constructs using its core language constructs, such as types, subjects, and aspects.

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

```rust
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
