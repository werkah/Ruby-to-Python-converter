$i = 0
$num = 5

until $i > $num  do
   puts("until - ok")
   $i +=1;
end

begin
   puts("do until - ok")
   $i +=1;
end until $i > $num