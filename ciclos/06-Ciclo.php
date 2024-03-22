<?php

$alto = 9;
$cont = 1;

for ($colum=1; $column <= $alto ; $column++) { 

    for ($fil = 1; $fil <= $cont; $fil++) {
        echo "* "; 
    }

    if ($colum < 5) {
        $cont = $cont + 1;
    } else {
        $cont = $cont - 1;
    }

    echo "\n";

    
}



?>