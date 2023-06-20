def test(a1, a2, a3)
    puts(a3)
    if a1 > a2
      puts("a1 is bigger than a2");puts("a1 is bigger than a3")
    else
      puts("a1 is smaller than a2")
    end
    arrr=[1,5,7,8]
    for i in arrr
      if i> a1
        puts(i)
      end
    end
end
test(2,3, "ala");
