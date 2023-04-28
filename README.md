# # Expresso Programming Language

Expresso is a work-in-progress programming language aimed at providing a modern, expressive, and powerful syntax. The language is designed with simplicity and flexibility in mind, making it easy to learn and extend.

This README provides an overview of the current state of Expresso's grammar, which is subject to change as the language evolves.

## Grammar

The grammar for Expresso is defined using ANTLR notation. It currently supports type declarations, method declarations, variable declarations, and statements.

### Type Declarations

Types can be declared using the `type` keyword, followed by an identifier and an optional body enclosed in curly braces (`{}`).

```expresso
type TypeName {
  // Type body
}
```

### Method Declarations

Methods can be declared using the `method` keyword, followed by an identifier, parameter list enclosed in parentheses (`()`), and an optional body enclosed in curly braces (`{}`).

```expresso
method methodName(typeName paramName, ...) {
  // Method body
}
```

### Variable Declarations

Variables can be declared using a type name, followed by an identifier, an optional assignment, and a semicolon (`;`).

```expresso
typeName varName = expression;
```

### Statements

Statements are terminated with a semicolon (`;`). Currently, Expresso supports expressions as statements.

```expresso
expression;
```

### Expressions and Logic

Expresso supports various expressions, including arithmetic, logic, and method calls.

#### Arithmetic

The language supports addition, subtraction, multiplication, and division.

```expresso
expression + term;
expression - term;
term * factor;
term / factor;
```

#### Logic

The language provides logical constructs such as `and`, `or`, and comparison operators.

```expresso
value and value;
value or value;
value == value;
value != value;
value < value;
value <= value;
value > value;
value >= value;
```

#### Method Calls

Method calls can be made by specifying an identifier, followed by a parameter list enclosed in parentheses (`()`).

```expresso
methodName(value, ...);
```

## Future Development

As Expresso is a work-in-progress language, its grammar and features will continue to evolve. Some potential future additions include support for control structures (if/else, loops, etc.), advanced types, and other language constructs.

Feel free to contribute to the project by submitting issues, pull requests, or participating in discussions.

## License

The Expresso language and its associated code are released under an open-source license. For more information, see the `LICENSE` file in the repository.
