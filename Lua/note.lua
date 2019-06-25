-- hello world
print("Hello World")

-- defines a factorial function
function fact(n)
	if n < 0 then
		return "please enter a postive number"
	end

	if n == 0 then
		return 1
	else
		return n * fact(n - 1)
	end
end

print("enter a number:")
a = io.read("*n")
print(fact(a))

-- Chunks
-- a chunk is simply a sequence of commands(or statements)

