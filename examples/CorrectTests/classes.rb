class Sample
    i=0
    def hello(o)
        puts(o)
        puts("Hello")
    end
    def function(a, b)
        d=a+b
        table=[false, true]
        if d==0
            arrr=[1,5,7,8]
            for i in arrr
                for j in arrr
                    if j<i
                        z=i+j
                        puts(z)
                        puts(table)
                    end
                end
            end
        end
    end
end
object = Sample.new
object.hello("ala")
object.function(1,2)
