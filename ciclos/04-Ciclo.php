<?php

$suma = 0;

for ($i=1; $i < 11; $i++) { 
    $numer = readline ("Ingresa el número $i ");

    $suma = $numer + $suma;
}

echo "El promedio de la suma de los números ingresados es de: " , $suma / 10;
?>