<?php

$cont = 1;
$x = 1;

for ($columna=1; $columna <= 5 ; $columna++) { 
    
    for ($fila = 1; $fila <= $cont; $fila++) {
        echo "$x";
        $x = $x + 1;
    }

    $cont = $cont + 1;
    $x = 1;
    echo "\n";
}

?>