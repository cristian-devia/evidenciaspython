<?php

$numer = readline ("Ingresa la cantidad de numero que deseas mostrar: ");

$suma = 0;
$penultimo = 0;
$ultimo = 1;

$suma = $penultimo + $ultimo;

echo "$penultimo - $ultimo" ;

for ($i = 2; $i < $numer; $i++) {
    
    $siguiente = $penultimo + $ultimo;

    echo " - $siguiente ";

    $penultimo = $ultimo;
    $ultimo = $siguiente;

    $suma = $suma + $siguiente;
}

echo "\nLa suma de los términos es: $suma";


?>