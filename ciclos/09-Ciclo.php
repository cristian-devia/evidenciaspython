<?php

$facts = 1;

$num = readline("Digite numero para calcular factorial : ");

for ($i = 1; $i <= $num; $i++) {
    $facts = $facts * $i;
}

echo "El factorial de $num es $facts";

?>