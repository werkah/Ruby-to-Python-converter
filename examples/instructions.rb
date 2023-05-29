x = (1 * 8) - 3
for i in arrr
    if x > 2
       x+=1
    elsif x <= 2 and x!=0
       x-=1
    else
       next
    end
    x = 1
    ## unless
    unless x>=2
       puts("less")
    else
       puts("greater")
    end
end;

