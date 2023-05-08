def test(a1, a2, a3)
    puts(a3)
    if a1 > a2
      puts("a1 is bigger")
    else
      puts("a2 is bigger")
    end

    arrr=[1,5,7,8]
    for i in arrr
      if i> a1
        puts(i)
      end
    end
end

test(2,3, "ala ma kota")