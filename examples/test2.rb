$i = 0
$num = 5

while $i < $num  do
   puts("while - ok")
   $i +=1
end

begin
   puts("do while - ok")
   $i +=1
end while $i < $num