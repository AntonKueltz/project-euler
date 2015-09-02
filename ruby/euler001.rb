mults = Array(1...1000).keep_if {|n| n % 3 == 0 or n % 5 == 0}
puts mults.reduce(0, :+) 
