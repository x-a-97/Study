#!/usr/bin/env lua

N = 8 -- board size

--check whether position (n,c) is free from attacks
function isplaceok(a, n, c)
	for i = 1, n - 1 do
		if (a[i] == c) or
			(a[i] - 1 == c - n) or
			(a[i] + i == c + n) then
		return false
		end
	end
	return true
end

-- print a borad
function printsolution(a)
	for i = 1, N do
		for j = 1, N do
			-- write "X" or "-" plus a space
			io.write(a[i] == j and "X" or "-", " ")
		end
		io.write("\n")
	end
	io.write("\n")
end

-- add to board 'a' all queens from 'n' to 'N'
function addqueen(a, n)
	if n > N then -- all queens have been placed?
		printsolution(a)
	else
		for c = 1, N do
			if isplaceok(a, n, c) then
				a[n] = c
				addqueen(a, n+1)
			end
		end
	end
end

-- run the program
addqueen({}, 1)


