class Sample
   @@i=9
   def hello
      puts("Hello Ruby!")
   end
   def function(a, b)
    d=true
    table=[false, true]
    if d==true
        arrr=[1,5,7,8]
        for i in arrr
            for j in arrr
                if j<i
                   z=i+j
                   puts(z)
                end
            end
         end
     end
   end
end

# Now using above class to create objects
object = Sample.new
object.hello
object.function(1,2)