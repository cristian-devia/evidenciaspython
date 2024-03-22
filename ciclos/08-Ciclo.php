<?php

$tamanioPiramide = 4;
$contador = 0;

for ($i=1; $i <= $tamanioPiramide; $i++) { 
    
    for ($j=1; $j <= $tamanioPiramide; $j++) { 
        
        switch ($i) {
            case 1:
                if($j == 3){
                    $contador = $contador + 1;
                    echo $contador;
                } else {
                    echo " ";
                }
                break;
            case 2:
                if($j == 2 or $j == 3){
                    $contador = $contador + 1;
                    echo $contador;
                } else {
                    echo " ";
                }
                break;
            case 3:
                if($j <> 1){
                    $contador = $contador + 1;
                    echo $contador;
                } else {
                    echo " ";
                }
                break;
            case 4:
                $contador = $contador + 1;
                echo $contador;
        }

    }
    
    echo "\n";

}




?>