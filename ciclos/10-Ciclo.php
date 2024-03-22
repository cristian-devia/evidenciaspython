<?php

    $tamanioA = 7;

    for ($i = 1; $i <= $tamanioA ; $i++) { 
        
        for ($j=$tamanioA; $j >= 1; $j--) { 

            if ($i == 1 or $i == 7) {
                echo "*";
            } elseif($i == $j) {
                echo "*";
            } else{
                echo " ";
            }
        }

        echo "\n";
    }

?>