// origin URL: https://docs.scala-lang.org/tour/basics.html

val x = 1 + 1 //name results of expressons with val
println(x)

x = 3 //error, values cannot be re-assigned

val x: Int = 1 + 1 //explicitly state the type

var x = 1 + 1 // variable
x = 3 //variable can be re-assign
println(x * x) //9
var x: Int = 1 + 1 // explicityly state the type

// combine expressions by surrounding them with {}
println({
  val x = 1 + 1
  x + 1
})

// Fucntions
// lambda
(x: Int) => x + 1 

// named  function
val addOne = (x: Int) => x + 1
println(addOne(1))

// multiple parameters
val add = (x: Int, y: Int) => x + y
println(add(1, 2))

//no parameters
val getTheAnswer = () => 42
println(getTheAnser())

// Methods
def add(x: Int, y: Int): Int = x + y
println(add(1, 2))

// can take multiple parameter lists
def addThenMultiply(x: Int, y: Int)(multiplier: Int): Int = (x + y) * multiplier
println(addThenMultiply(1, 2)(2))

// or no parameter lists at all
def name: String = System.getProperty("user.name")
println("Hello, " + name + "!")

// can have multi-line expressions
def getSquareString(input: Double): String = {
  val Square = input * input
  square.toString
}

// Classes
class Greeter(prefix: String, suffix: String) {
  def greet(name: String): Unit =
    println(prefix + name + suffix)
}

// make instance
val greeter = new Greeter("Hello, ", "!")
greeter.greet("Scala developer")

// Case Classes
case class Point(x: Int, y: Int)

// instantiate case classes without new keyword
val point = Point(1, 2)
val anotherPoint = Point(1, 2)
val yetAnotherPoint = Point(2, 2)

// compared by value
if (point == anotherPoint) {
  println(point + " and " + anotherPoint + " are the same.")
} else {
  println(point + " and " + anotherPoint + " are different.")
}


// Objects
object IdFactory {
  private var counter = 0
  def create(): Int = {
    counter += 1
    counter
  }
}

// access an object
val newId: Int = IdFactory.create()
println(newId)
val newerId: Int = IdFactory.create()
println(newerId)

// Traits
trait Greeter {
  def greet(name: String): Unit
}
// can have default  implementations
trait Greeter  {
  def greet(name: String): Unit = 
    print("Hello, " + name + "!")
}

// can extend and override an implemetation
class DefaultGreeter extends Greeter

class CustomizableGreeter(prefix: String, postfix: String) extends Greeter {
  override def greet(name: String): Unit = {
    println(prefix + name + postfix)
  }
}

// Main Method
object Main {
  def main(args: Array[String]): Unit = 
    println("Hello, Scala developer!")
}

// Scala Type Hierarchy
// origin URL: https://docs.scala-lang.org/tour/unified-types.html
val list: List[Any] = List(
  "a string",
  732,
  'c',
  true,
  () => "an anonymous function returning a string"
)

list.foreach(element => println(element))

// Type Casting
val x: Long = 987654321
val y: Float = x // 9.87654E8 some percision is lost in this case
val face: Char = '☺'
val number: Int = face //9876

// Nothing and Null

// Classes
// Defining a class
class user
val user1 = new user

// an example class definition for a point
class Point(var x: Int, var y: Int) {

  def move(dx: Int, dy: Int): Unit = {
    x = x + dx
    y = x + dy
  }

  override def toString: String =
    s"($x, $y)"
}

val point1 = new Point(2, 3)
point.x
println(point1)

// Constructors
// can have optional parameters by providing a default value
class Point(var x: Int = 0, var y: Int = 0)
val origin = new Point
val point1 = new Point(1)
println(point1.x)

// pass value to y
val point2 = new Pint(y=2)
println(pint2.y)

// Private Members and Getter/Setter Syntax
// Members are public by default, 
// use the private access modifier to hide them
class Point {
  private var _x = 0
  private var _y = 0
  private val bound = 100

  def x = _x
  def x_= (newValue: Int): Unit = {
    if (newValue < bound) _x = newValue else printWarning
  }

  def y = _y
  def y_=(newValue: Int): Unit = {
    if (newValue < bound) _y = newValue else printWarning
  }

  private def printWarning = println("WARNING: Out of bounds")
}

val Point1 = new Point
point1.x = 99
point1.y = 101





